from flask import Response
import time
import json
from flask import jsonify
from .sft import MinderLLM

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
        
        # Files are stored inside a files object
        # https://deepchat.dev/docs/connect
        files = request.files.getlist("files")
        if files:
            print("Files:")
            for file in files:
                print(file.filename)

            # When sending text messages along with files - they are stored inside the data form
            # https://deepchat.dev/docs/connect
            text_messages = list(request.form.items())
            if len(text_messages) > 0:
                print("Text messages:")
                # message objects are stored as strings and they will need to be parsed (JSON.parse) before processing
                for key, value in text_messages:
                    print(key, value)
            return {"text": "Get files! Loading..."}
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
           
            return response

        # Sends response back to Deep Chat using the Response format:
        # https://deepchat.dev/docs/connect/#Response
        