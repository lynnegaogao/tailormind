import json
import os
import time
from werkzeug.utils import secure_filename
from flask_cors import CORS
from flask import Flask,request
from requests.exceptions import ConnectionError
from services.custom import Custom
from services.openAI import OpenAI
from flask import Flask, request
from dotenv import load_dotenv
from flask_cors import CORS
import jieba
from collections import Counter
import re
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

@app.route('/get-wordclouddata',methods=["POST"])
def generate_wordcloud_data():
    data = request.json
    noteContext = data.get('noteContext', '')
   
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
    return word_cloud_data

if __name__ == '__main__':
    app.run(debug=True)