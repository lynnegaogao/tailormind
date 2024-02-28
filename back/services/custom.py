from flask import Response
import time
import json
from flask import jsonify
from .sft import MinderLLM
import base64
import io

minderllm=MinderLLM(model_path='E:\Vis24-TailorMind\sftmodel\llama_factory\sft_v1.0',device='cuda:0')

class Custom:
    def chat(self, body):
        # Text messages are stored inside request body using the Deep Chat JSON format:
        # https://deepchat.dev/docs/connect
        print(body)
        # Sends response back to Deep Chat using the Response format:
        # https://deepchat.dev/docs/connect/#Response
        #return {"text": "This is a respone from a Flask server. Thank you for your message!"}
        response = {'text': "This is a response from a Flask server. Thank you for your message!"}
        return response

    def chat_stream(self, body):
        # Text messages are stored inside request body using the Deep Chat JSON format:
        # https://deepchat.dev/docs/connect
        print(body)
        response_chunks = "This is a response from a Flask server. Thank you for your message!".split(
            " ")
        response = Response(self.send_stream(response_chunks), mimetype="text/event-stream")
        response.headers["Content-Type"] = "text/event-stream"
        response.headers["Cache-Control"] = "no-cache"
        response.headers["Connection"] = "keep-alive"
        response.headers["Access-Control-Allow-Origin"] = "*"
        return response

    def send_stream(self, response_chunks, chunk_index=0):
        if chunk_index < len(response_chunks):
            chunk = response_chunks[chunk_index]
            yield f"data: {json.dumps({'text': f'{chunk} '})}\n\n"
            time.sleep(0.07)
            yield from self.send_stream(response_chunks, chunk_index + 1)
        else:
            yield ""

    def files(self, request):
        # 文件传输
        files = request.files.getlist("files")
        file_data = []
        if files:
            for file in files:
                print("Files:",file.filename)
                file_content = base64.b64encode(file.read()).decode('utf-8')
                file_data.append({
                    'filename': file.filename,
                    'content': file_content
            })
            # text_messages = list(request.form.items())
            # if len(text_messages) > 0:
            #     print("Text messages:")
            #     for key, value in text_messages:
            #         print(key, value)
            
            # 请求openai api获取file structure
            fileStructure=[
                {
                    "key": "1",
                    "title": "凸集",
                    "page": "1-3",
                    "children": [
                        { "key": "1-1", "title": "凸集定义", "page": "1" },
                        { "key": "1-2", "title": "凸集的例子", "page": "2-3" },
                    ]
                },
                {
                    "key": "2",
                    "title": "凸函数",
                    "page": "3-7",
                    "children": [
                        { "key": "2-1", "title": "凸性的一阶条件", "page": "4" },
                        { "key": "2-2", "title": "凸性的二阶条件", "page": "5" },
                        { "key": "2-3", "title": "Jensen不等式", "page": "5" },
                        { "key": "2-4", "title": "子级集", "page": "6" },
                        { "key": "2-5", "title": "凸函数的应用", "page": "6-7" },
                    ]
                },
                {
                    "key": "3",
                    "title": "凸优化问题",
                    "page": "7-12",
                    "children": [
                        { "key": "3-1", "title": "凸优化定义", "page": "7-8" },
                        { "key": "3-2", "title": "凸问题的全局优化", "page": "9-10" },
                        { "key": "3-3", "title": "凸优化问题的例子", "page": "11-12" }
                    ]
                }
            ],
            
            response={
                'chatdata':{"text": "Get files! Loading..."},
                'filestructure':fileStructure,
                'file':file_data
            }
            return response
        
        else:
            # When sending text messages without any files - they are stored inside a json
            
            body = request.json["messages"][0]['text']
            print("Text messages:",body )
            if body=='What is Self-Regulated Learning (SRL)?':
                response={"text":"Self-Regulated Learning (SRL) consists of 3 phases:\n 1. **Forethought**, planning and activation \n 2. **Performance**, monitoring and control \n 3. Reaction and **reflection**","html":"<div class=\"deep-chat-temporary-message\"><button class=\"deep-chat-button deep-chat-suggestion-button\" style=\"margin-top: 6px\">What does each view of Tailor-Mind do?</button><button class=\"deep-chat-button deep-chat-suggestion-button\" style=\"margin-top: 6px\">How can I start my SRL journey?</button></div>"}
            elif body=='What does each view of Tailor-Mind do?':
                response={"text":"Some guidances will be coming...","html":"<div class=\"deep-chat-temporary-message\"><button class=\"deep-chat-button deep-chat-suggestion-button\" style=\"margin-top: 6px\">How can I start my SRL journey?</button></div>"}
            elif body=='How can I start my SRL journey?':
                response={"text":"**Upload your learning material** and start your SRL journey!"}
            else:
                response=minderllm.generate(query=body)
           
            return {'chatdata':response}

        # Sends response back to Deep Chat using the Response format:
        # https://deepchat.dev/docs/connect/#Response
        