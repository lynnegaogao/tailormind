import json
import os
import time
from werkzeug.utils import secure_filename
from flask_cors import CORS
from flask import Flask,request
from requests.exceptions import ConnectionError
from services.custom import Custom
from services.openAI import OpenAI
from services.sft import MinderLLM
from flask import Flask, request
from dotenv import load_dotenv
from flask_cors import CORS
import jieba
from collections import Counter
import re
import subprocess
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer,GenerationConfig
#import simplejson

load_dotenv()

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}},supports_credentials=True)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 允许最大16MB



UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
filename=''

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/uploadfile', methods=['POST'])
def upload_file():
    print("backend gets file!")
    if 'file' not in request.files:
        return {"error": "No file part"}, 400

    file = request.files['file']
    if file.filename == '':
        return {"error": "No selected file"}, 400

    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return {"filename": filename}
    
# ------------------ EXCEPTION HANDLERS ------------------

# Sends response back to Deep Chat using the Response format:
# https://deepchat.dev/docs/connect/#Response
@app.errorhandler(Exception)
def handle_exception(e):
    print(e)
    return {"error": str(e)}, 500

@app.errorhandler(ConnectionError)
def handle_exception(e):
    print(e)
    return {"error": "Internal service error"}, 500

# ------------------ CUSTOM API ------------------
    
custom = Custom()

@app.route("/chat", methods=["POST"])
def chat():
    body = request.json
    print("api backend gets request!")
    print("response:",custom.chat(body))
    return custom.chat(body)

@app.route("/chat-stream", methods=["POST"])
def chat_stream():
    body = request.json
    print("api backend gets request!")
    return custom.chat_stream(body)

@app.route("/files", methods=["POST"])
def files():
    print("api backend gets request!")
    response=custom.files(request)
    return response

# ------------------ OPENAI API ------------------

open_ai = OpenAI()

@app.route("/openai-chat", methods=["POST"])
def openai_chat():
    body = request.json
    return open_ai.chat(body)

@app.route("/openai-chat-stream", methods=["POST"])
def openai_chat_stream():
    body = request.json
    return open_ai.chat_stream(body)

@app.route("/openai-image", methods=["POST"])
def openai_image():
    files = request.files.getlist("files")
    return open_ai.image_variation(files)

# ------------------ MinderLLM API ------------------
# class MinderLLM:
#     def __init__(self, model_path: str, device: str):
#         self.model_path = "E:\Vis24-TailorMind\sftmodel\llama_factory\sft_v1.0"
#         self.device = device
#         self.dtype = torch.float16
#         # 模型加载
#         self.model = AutoModelForCausalLM.from_pretrained(
#             self.model_path,
#             trust_remote_code=True,
#             low_cpu_mem_usage=True,
#             torch_dtype=self.dtype,
#         ).to(self.device).eval()
#         self.tokenizer = AutoTokenizer.from_pretrained(
#             model_path,
#             trust_remote_code=True,
#             use_fast=True)
#         self.model.generation_config = GenerationConfig.from_pretrained(model_path)
#         self.model.generation_config.user_token_id = 195
#         self.model.generation_config.assistant_token_id = 196

#     def generate(self, query: str):
#         # 对 query 进行编码
#         # input_prompt = '<s>' + query + '</s>'
#         input_prompt = []
#         input_prompt.append({"role":"user","content":query})
#         response = self.model.chat(self.tokenizer,input_prompt)
#         return {"text":response}
    
minderllm=MinderLLM(model_path='E:\Vis24-TailorMind\sftmodel\llama_factory\sft_v1.0',device='cuda:0')

@app.route('/sft-chat', methods=["POST"])
def sft_chat():
    body = request.json
    print(body["messages"][-1]['text'])
    # print(body["messages"]['text'])
    response=minderllm.generate(query=body["messages"][0]['text'])
    print(response)
    return response

@app.route('/get-wordclouddata',methods=["POST"])
def generate_wordcloud_data():
    data = request.json
    noteContext = data.get('noteContext', '')
    nodeId=data.get('nodeId','')
    #text_no_tags = re.sub(r'</?p>|<br>', '', noteContext)
    #text_no_punctuation = re.sub(r'[^\w\s]', '', text_no_tags)
    ##print('content来自前端:',noteContext)
    #words = jieba.lcut(text_no_punctuation)
    ##print('分词结果:',words)
    #word_count = Counter(words)
    #print('词频结果:',word_count)
    #filtered_word_count = {word: count for word, count in word_count.items() if len(word) > 1 and word not in ['的', '在', '和', '是', '了','这样']}
    
    #word_cloud_data = [{'text': word, 'size': count} for word, count in filtered_word_count.items()]
    with open('wordcloud.json', 'r', encoding='utf-8') as file:
    # 加载JSON数据
        word_cloud_data = json.load(file) 
    sorted_data = sorted(word_cloud_data, key=lambda x: x['size'], reverse=True)
    top_5_elements = sorted_data[:5]

    return top_5_elements



if __name__ == '__main__':
    app.run(debug=True)