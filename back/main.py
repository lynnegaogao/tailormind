import json
import os
import time
from werkzeug.utils import secure_filename
from flask_cors import CORS
from flask import Flask,request
from requests.exceptions import ConnectionError
from services.custom import Custom
from openai import OpenAI
import json,re,time
from services.sft import MinderLLM
from flask import Flask, request
from dotenv import load_dotenv
from flask_cors import CORS
import jieba
from collections import Counter
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

# open_ai = OpenAI()

# @app.route("/openai-chat", methods=["POST"])
# def openai_chat():
#     body = request.json
#     return open_ai.chat(body)

# @app.route("/openai-chat-stream", methods=["POST"])
# def openai_chat_stream():
#     body = request.json
#     return open_ai.chat_stream(body)

# @app.route("/openai-image", methods=["POST"])
# def openai_image():
    files = request.files.getlist("files")
    return open_ai.image_variation(files)

# ------------------ MinderLLM API ------------------

    
# minderllm=MinderLLM(model_path='E:\Vis24-TailorMind\sftmodel\llama_factory\sft_v1.0',device='cuda:0')
historical=True
# historical=False
@app.route('/get-customziednotedata', methods=["POST"])
def sft_chat():
    if historical:
        with open('./history/8-markdown.md', 'r', encoding='utf-8') as file:
                content = file.read()
        return [content]
    else:
        data = request.json
        content=json.dumps(data.get('submitChatData', ''))
        print(content)
        
        prompt = """
        Please generate summarised and structured notes in markdown form based on multiple rounds of dialogue chats.
        Please ignore the content about Self-Regulated Learning(SRL) and guided dialogues. 
        Only process chat content related to deep learning or AI knowledge points.
        Generate rich markdown forms, such as tables, etc., where possible, and add underlining if there are key statements that need to be highlighted.
        Only return markdown data, the format is as follows: 
        ```markdown 
        ```
        """
        user_input=prompt+content
        OPENAI_API_KEY="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"
        client = OpenAI(api_key=OPENAI_API_KEY)

        assistant = client.beta.assistants.create(
                    name="Education Specialist",
                    instructions="You are an educational expert who specializes in tutoring beginners in self-study, deleting processed data while giving beginners advice on how to learn. If you cannot parse the required Json output, you can give an empty structure that contains only keys.",
                    tools=[{"type": "code_interpreter"}],
                    model="gpt-4-0125-preview"
                )

        thread = client.beta.threads.create()

        # 创建消息
        message = client.beta.threads.messages.create(
                        thread_id=thread.id,
                        role="user",
                        content=user_input
                    )

                    # 4. run thread
                    # Thread 默认不会运行，需要创建一个 Run 任务来执行 Thread。
        run = client.beta.threads.runs.create(
                        thread_id=thread.id,
                        assistant_id=assistant.id,
                    )

                    # 等待运行任务完成
                    # Thread 是异步执行的，需要轮询检查是否执行完成。
                    # Thread 执行时会上锁，在执行完成前不可以再添加 message 或者提交新的 Run 任务。
        while True:
            run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
            if run.status not in ["queued", "in_progress"]:
                break
        time.sleep(1)

                    # 获取 AI 输出结果
        messages = client.beta.threads.messages.list(thread_id=thread.id)
                    # 从消息中取出 AI 输出的 markdown 字符串
        ai_output = messages.data[0].content[0].text.value
        pattern = r'```markdown(.*?)```'
        markdownData = re.findall(pattern, ai_output, re.DOTALL)
        print("markdown data:",markdownData)
        return markdownData
    
    


# ------------------ Other API ------------------
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