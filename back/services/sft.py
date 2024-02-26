import sys
sys.path.append('e:/Vis24-TailorMind')
sys.path.append('E:\Vis24-TailorMind\sftmodel\llama_factory\src\cli_demo_backend.py')
from sftmodel.llama_factory.src.llmtuner import  ChatModel
from sftmodel.llama_factory.src.llmtuner.extras.misc import torch_gc


class ChatCLI:
    def __init__(self):
        self.chat_model = ChatModel()
        self.messages = []
    
    def get_response(self, query: str) -> str:
        print("Welcome to the chat model.")
        self.messages.append({"role": "user", "content": query})
        response = ""
        for new_text in self.chat_model.stream_chat(self.messages):
            response += new_text
        self.messages.append({"role": "assistant", "content": response})
        return response

    def run_chat_session(self):
        print("Welcome to the CLI application, use `clear` to remove the history, use `exit` to exit the application.")

        while True:
            try:
                query = input("\nUser: ")
            except UnicodeDecodeError:
                print("Detected decoding error at the inputs, please set the terminal encoding to utf-8.")
                continue
            except Exception:
                raise

            if query.strip() == "exit":
                break

            if query.strip() == "clear":
                self.messages = []
                torch_gc()
                print("History has been removed.")
                continue

            self.messages.append({"role": "user", "content": query})
            print("Assistant: ", end="", flush=True)

            response = ""
            for new_text in self.chat_model.stream_chat(self.messages):
                print(new_text, end="", flush=True)
                response += new_text
            self.messages.append({"role": "assistant", "content": response})


chat_cli = ChatCLI()

# 使用get_response方法获取回复
response = chat_cli.get_response("你的问题")
