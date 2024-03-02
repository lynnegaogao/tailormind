import time
import json
import base64
import io
import re
import os
from flask import Response
from flask import jsonify
from .sft import MinderLLM
from openai import OpenAI

historical=True
# historical=False

OPENAI_API_KEY="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"
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

    def save_file_locally(self, file):
        upload_folder = 'uploads'
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)  # 如果目录不存在，则创建目录
        file_path = os.path.join(upload_folder, file.filename)
        file.save(file_path)  # 保存文件到本地目录
        return file_path

    def files(self, request):
        # 文件传输
        files = request.files.getlist("files")
        file_data = []
        file_paths = []
        if files:
            for file in files:
                print("Files:",file.filename)
                file_path = self.save_file_locally(file)  # 保存文件并获取文件路径
                print("Save to file path:",file_path)
                file_paths.append(file_path)

                file.seek(0)

                file_content = base64.b64encode(file.read()).decode('utf-8')
                print(file_content[:100])
                file_data.append({
                    'filename': file.filename,
                    'content': file_content
                })

                # 请求openai api获取file structure
                # 调用openAI.py的get_file_structure函数
                
                # 使用历史数据
                if historical==True:
                    with open('E:/Vis24-TailorMind/tailormind/back/history/1_material_overview.json', 'r') as file:
                        file_openai_response=json.load(file)
                # 用户实际数据
                else:
                    file_openai_response=self.get_file_structure_in_english(file_path)
                # file_openai_response=self.get_file_structure_in_english(file_path)
                print("history结果:",file_openai_response)
                fileStructure = file_openai_response['file_structure']
                fileSummary=file_openai_response['summary']

            response={
                'chatdata':{"text": "Get files! Loading..."},
                'filestructure':fileStructure,
                'file':file_data,
                'filesummary':fileSummary
            }
            # print("File_structure:",response['filestructure'])
            return response

        else:
            # When sending text messages without any files - they are stored inside a json

            body = request.json["messages"][0]['text']
            print("Text messages:",body )
            # 引导问题
            if body=='What is Self-Regulated Learning (SRL)?':
                response={"text":"Self-Regulated Learning (SRL) consists of 3 phases:\n 1. **Forethought**, planning and activation \n 2. **Performance**, monitoring and control \n 3. Reaction and **reflection**","html":"<div class=\"deep-chat-temporary-message\"><button class=\"deep-chat-button deep-chat-suggestion-button\" style=\"margin-top: 6px\">What does each view of Tailor-Mind do?</button><br><button class=\"deep-chat-button deep-chat-suggestion-button\" style=\"margin-top: 6px\">How can I start my SRL journey?</button></div>"}
            elif body=='What does each view of Tailor-Mind do?':
                response={"text":"Some guidances will be coming...","html":"<div class=\"deep-chat-temporary-message\"><button class=\"deep-chat-button deep-chat-suggestion-button\" style=\"margin-top: 6px\">How can I start my SRL journey?</button></div>"}
            elif body=='How can I start my SRL journey?':
                response={"text":"**Upload your learning material** and start your SRL journey!"}
            # 问题推荐
            elif body.startswith("Recommend some questions"):
                response=minderllm.generate(query=body)
                # 需要删除，暂时使用
                # response={"text":"1. What is Self-Regulated Learning (SRL)?\n2. What does each view of Tailor-Mind do?\n3. How can I start my SRL journey?"}
                html_response=self.convert_rmdText_to_html(response)
                response=html_response
            # 其他正常问答
            else:
                response=minderllm.generate(query=body)
                # 需要删除，暂时使用
                # response={"text":"Some guidances will be coming...","html":"<div class=\"deep-chat-temporary-message\"><button class=\"deep-chat-button deep-chat-suggestion-button\" style=\"margin-top: 6px\">What does each view of Tailor-Mind do?</button><br><button class=\"deep-chat-button deep-chat-suggestion-button\" style=\"margin-top: 6px\">How can I start my SRL journey?</button></div>"}

            print("Response:",response)
            return {'chatdata':response}

        # Sends response back to Deep Chat using the Response format:
        # https://deepchat.dev/docs/connect/#Response

    # 获取文件结构，输入文件，返回json
    def get_file_structure(self, file_path):

        client = OpenAI(api_key=OPENAI_API_KEY)
        # 示例数据
        sample = {
            "overview": "这是一个关于凸优化的教学资料，侧重于定义和解决机器学习中的优化问题，如支持向量机(SVM)、最小二乘问题和逻辑回归的最大似然估计等。",
            "summary": "资料首先介绍了凸集、凸函数、凸优化问题和拉格朗日对偶问题的基本概念。接着，它探讨了不同类型的凸优化问题，包括线性规划、二次规划、QCQP和SDP，并提供了这些问题在机器学习中的实际应用示例。文档末尾给出了参考文献。",
            "file_structure": [
                {
                    "key": "1",
                    "title": "凸集",
                    "content": "凸集指的是在任意两点之间的线段上的点仍然在该集合中。或者说，给定集合中的任意两点，连接这两点的线段也完全包含在该集合中。",
                    "children": [
                        {"key": "1-1", "title": "凸集定义", "content": "凸集指的是在任意两点之间的线段上的点仍然在该集合中。或者说，给定集合中的任意两点，连接这两点的线段也完全包含在该集合中。"},
                        {"key": "1-2", "title": "凸集的例子", "content": "例如，单位球是凸集，因为连接单位球内任意两点的线段也完全包含在单位球内。"},
                    ]
                },
                {
                    "key": "2",
                    "title": "凸函数",
                    "content": "凸函数指的是定义域内的任意两点连线位于函数图像上方的函数。或者说，给定定义域内的任意两点以及这两点连线上的任意一点，这个点的函数值不大于两点连线上对应点的函数值。",
                    "children": [
                        {"key": "2-1", "title": "凸性的一阶条件", "content": "函数f(x)在定义域内是凸函数，当且仅当对于定义域内的任意两点x1和x2，有f(x1) <= f(x2) + f'(x2)(x1 - x2)，其中f'(x)表示f(x)的导数。"},
                        {"key": "2-2", "title": "凸性的二阶条件", "content": "函数f(x)在定义域内是凸函数，当且仅当它的二阶导数f''(x)在定义域内始终大于等于零。"},
                        {"key": "2-3", "title": "Jensen不等式", "content": "对于凸函数f和任意的随机变量X以及X的任意凸函数φ，Jensen不等式表示φ的期望大于等于φ的参数的期望值，即E[φ(X)] >= φ(E[X])。"},
                        {"key": "2-4", "title": "子级集", "content": "凸函数的子级集也是凸函数。具体地说，给定凸函数f和其定义域内的一个凸集S，函数在S上的限制仍然是凸函数。"},
                        {"key": "2-5", "title": "凸函数的应用", "content": "凸函数在机器学习中有广泛的应用，例如，支持向量机(SVM)中的损失函数就是凸函数，这保证了SVM问题的全局最优解的存在性和唯一性。"},
                    ]
                },
                {
                    "key": "3",
                    "title": "凸优化问题",
                    "content": "凸优化问题是指目标函数和约束条件均为凸函数的优化问题。这类问题具有良好的性质，可以利用凸优化理论和算法进行高效求解。",
                    "children": [
                        {"key": "3-1", "title": "凸优化定义", "content": "凸优化问题是指目标函数和约束条件均为凸函数的优化问题。即目标函数是凸函数，约束条件是凸函数。"},
                        {"key": "3-2", "title": "凸问题的全局优化", "content": "凸优化问题的一个重要性质是全局最优解是存在且唯一的。这使得凸优化问题具有很好的求解性质。"},
                        {"key": "3-3", "title": "凸优化问题的例子", "content": "许多机器学习中常见的优化问题，如支持向量机的二次规划问题、逻辑回归的最大似然估计问题等，都可以归结为凸优化问题。"},
                    ]
                }
            ]
        }
        sample_str = "```json\n" + json.dumps(sample) + "\n```"
        # prmopts
        requirements = [
            "用简体中文描述整个文件的概要和结构目录，要求如下:",
            "- 浏览整个文件，尽可能理解文件文字内容，分析其中内容结构，忽略图片",
            "- 'summary'是文件的综述",
            "- 'overview'是文件的概要",
            "- 'file_structure'是描述文件结构的树，深度=2，每个节点代表一章或一节",
            "- 'key'是节点的索引，只允许出现数字和'-'",
            "- 'title'是节点的标题",
            "- 'content'是对该节点的描述，长度为2-3句话",
            "- Only return JSON code without any other content",
            "- 格式参考下面的例子：",
            sample_str
        ]
        user_input = "\n".join(requirements)

        # 正则表达式获取```json```内的内容
        def extract_json_from_string(input_string):
            # 使用正则表达式匹配JSON部分
            json_pattern = r'```json\n(.*?)```'
            match = re.search(json_pattern, input_string, re.DOTALL)

            if match:
                json_str = match.group(1).strip()
                # 转换为JSON对象
                json_data = json.loads(json_str)
                return json_data
            else:
                return None

        # 封装对话逻辑的函数
        def get_assistant_response(user_input, thread_id, assistant_id, file_id):
            # 创建消息
            message = client.beta.threads.messages.create(
                thread_id=thread_id,
                role="user",
                content=user_input,
                file_ids=[file_id]
            )

            # 4. run thread
            # Thread 默认不会运行，需要创建一个 Run 任务来执行 Thread。
            run = client.beta.threads.runs.create(
                thread_id=thread_id,
                assistant_id=assistant_id,
            )

            # 等待运行任务完成
            # Thread 是异步执行的，需要轮询检查是否执行完成。
            # Thread 执行时会上锁，在执行完成前不可以再添加 message 或者提交新的 Run 任务。
            while True:
                run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
                if run.status not in ["queued", "in_progress"]:
                    break
                time.sleep(1)

            # 获取 AI 输出结果
            messages = client.beta.threads.messages.list(thread_id=thread_id)

            # 从消息中取出 AI 输出的 JSON 字符串
            ai_output = messages.data[0].content[0].text.value

            return ai_output

         # 读取文件并上传到OpenAI

        with open(file_path, "rb") as file:  # 使用with语句确保文件正确关闭
            print("Open file.")
            content = file.read()

        filename = file_path.split("\\")[-1]
        print("File name:",filename)
        content_type = 'application/pdf'  # 根据文件实际类型设置
        file_response = client.files.create(
            file=(filename, content, content_type),
            purpose='assistants'
        )
        # 从响应中获取文件ID
        print("file_response:",file_response)
        # print(dir(file_response))
        file_id = file_response.id  # 使用字典访问方式获取文件ID
        print(file_id)
        # 1. Create an assistant using the file ID
        assistant = client.beta.assistants.create(
            name="File Analysis Assistant",
            instructions="You are a customer support chatbot. Use your knowledge base to best respond to customer queries.",
            tools=[{"type": "retrieval"}],
            model="gpt-4-1106-preview",
            file_ids=[file_id]
        )

        # 2. create Thread
        thread = client.beta.threads.create() # （可选）在创建时指定对话内容

        ai_output = get_assistant_response(user_input, thread.id, assistant.id, file_id)
        print(ai_output)
        ai_output_json = extract_json_from_string(ai_output)

        # 5. delete assistant
        client.beta.assistants.delete(assistant.id)

        return ai_output_json
    def get_file_structure_in_english(self, file_path):

        client = OpenAI(api_key=OPENAI_API_KEY)
        # 示例数据
        sample = {
            "summary": "The material begins with an introduction to the basic concepts of convex sets, convex functions, convex optimization problems, and Lagrangian dyadic problems. It then explores different types of convex optimization problems, including linear programming, quadratic programming, QCQP, and SDP, and provides examples of practical applications of these problems to machine learning. References are given at the end of the document.",
            "file_structure": [
                {
                    "key": "1",
                    "title": "Convex Sets",
                    "content": "A convex set is a set in which the points on a line segment between any two points are still in the set. Or, given any two points in a set, the line segment connecting those two points is also completely contained in that set.",
                    "children": [
                        {"key": "1-1", "title": "Definition of Convex Set", "content": "A convex set is a set in which the points on a line segment between any two points remain in that set. Or, given any two points in a set, the line segment connecting those two points is also completely contained in that set."} ,
                        {"key": "1-2", "title": "Examples of Convex Sets", "content": "For example, the unit ball is a convex set because the line segment connecting any two points in the unit ball is also completely contained within the unit ball."} ,
                    ]
                },
                {
                    "key": "2",
                    "title": "Convex Functions",
                    "content": "A convex function is a function in which the line connecting any two points in the domain of definition lies above the image of the function. Or, given any two points in the domain of definition and any point on the line connecting these two points, the function value at this point is not greater than the function value at the corresponding point on the line connecting the two points." ,
                    "children": [
                        {"key": "2-1", "title": "First-order conditions for convexity", "content": "A function f(x) is convex in the domain of definition if and only if for any two points x1 and x2 in the domain of definition, there is f(x1) <= f(x2) + f'(x2)(x1 - x2), where f'(x) denotes the derivative of f(x)."} ,
                        {"key": "2-2", "title": "Second-order conditions for convexity", "content": "A function f(x) is convex in the domain of definition if and only if its second-order derivative f''(x) is always greater than or equal to zero in the domain of definition."} ,
                        {"key": "2-3", "title": "Jensen's Inequality", "content": "For a convex function f and any random variable X and any convex function φ of X, Jensen's inequality states that the expectation of φ is greater than or equal to the expectation of the parameters of φ, i.e., E[φ(X)] >= φ(E[X])."} ,
                        {"key": "2-4", "title": "Sublevel sets", "content": "Sublevel sets of convex functions are also convex functions. Specifically, given a convex function f and a convex set S in its domain of definition, the restriction of the function to S is still a convex function."} ,
                        {"key": "2-5", "title": "Applications of Convex Functions", "content": "Convex functions have a wide range of applications in machine learning, for example, the loss function in a Support Vector Machine (SVM) is a convex function, which guarantees the existence and uniqueness of the globally optimal solution to the SVM problem."} ,
                    ]
                },
                {
                    "key": "3",
                    "title": "Convex Optimization Problems",
                    "content": "Convex optimization problems are optimization problems in which both the objective function and constraints are convex functions. These problems have good properties and can be solved efficiently using convex optimization theory and algorithms." ,
                    "children": [
                        {"key": "3-1", "title": "Definition of Convex Optimization", "content": "Convex optimization problems are optimization problems in which both the objective function and constraints are convex functions. That is, the objective function is convex and the constraints are convex."} ,
                        {"key": "3-2", "title": "Global Optimization of Convex Problems", "content": "An important property of convex optimization problems is that the globally optimal solution exists and is unique. This gives the convex optimization problem a good solution property."} ,
                        {"key": "3-3", "title": "Examples of Convex Optimization Problems", "content": "Many common optimization problems in machine learning, such as quadratic programming problems for support vector machines and maximum likelihood estimation problems for logistic regression, can be reduced to convex optimization problems."} ,
                    ]
                }
            ]
        }
        sample_str = "```json\n" + json.dumps(sample) + "\n```"
        # prmopts
        requirements = [
            "Describe the summary and structure of the entire document with following requirements:",
            "1.'summary' is a summary of the document",
            "2.'file_structure' is a tree that describes the structure of the file, depth = 2, and each node represents a chapter or section",
            "3.'key' is the index of the node, only numbers and '-' are allowed",
            "4.'title' is the title of the node",
            "5.'content' is a description of the node in 2-3 sentences.",
            "Only return JSON code without any other content",
            "The JSON format refers to the example below:",
            sample_str
        ]
        user_input = "\n".join(requirements)

        # 正则表达式获取```json```内的内容
        def extract_json_from_string(input_string):
            # 使用正则表达式匹配JSON部分
            json_pattern = r'```json\n(.*?)```'
            match = re.search(json_pattern, input_string, re.DOTALL)

            if match:
                json_str = match.group(1).strip()
                # 转换为JSON对象
                json_data = json.loads(json_str)
                return json_data
            else:
                return None

        # 封装对话逻辑的函数
        def get_assistant_response(user_input, thread_id, assistant_id, file_id):
            # 创建消息
            message = client.beta.threads.messages.create(
                thread_id=thread_id,
                role="user",
                content=user_input,
                file_ids=[file_id]
            )

            # 4. run thread
            # Thread 默认不会运行，需要创建一个 Run 任务来执行 Thread。
            run = client.beta.threads.runs.create(
                thread_id=thread_id,
                assistant_id=assistant_id,
            )

            # 等待运行任务完成
            # Thread 是异步执行的，需要轮询检查是否执行完成。
            # Thread 执行时会上锁，在执行完成前不可以再添加 message 或者提交新的 Run 任务。
            while True:
                run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
                if run.status not in ["queued", "in_progress"]:
                    break
                time.sleep(1)

            # 获取 AI 输出结果
            messages = client.beta.threads.messages.list(thread_id=thread_id)

            # 从消息中取出 AI 输出的 JSON 字符串
            ai_output = messages.data[0].content[0].text.value

            return ai_output

         # 读取文件并上传到OpenAI

        with open(file_path, "rb") as file:  # 使用with语句确保文件正确关闭
            print("Open file.")
            content = file.read()

        filename = file_path.split("\\")[-1]
        print("File name:",filename)
        content_type = 'application/pdf'  # 根据文件实际类型设置
        file_response = client.files.create(
            file=(filename, content, content_type),
            purpose='assistants'
        )
        # 从响应中获取文件ID
        print("file_response:",file_response)
        # print(dir(file_response))
        file_id = file_response.id  # 使用字典访问方式获取文件ID
        
        # 1. Create an assistant using the file ID
        assistant = client.beta.assistants.create(
            name="File Analysis Assistant",
            instructions="You are a customer support chatbot. Use your knowledge base to best respond to customer queries.",
            tools=[{"type": "retrieval"}],
            model="gpt-4-1106-preview",
            file_ids=[file_id]
        )

        # 2. create Thread
        thread = client.beta.threads.create() # （可选）在创建时指定对话内容

        ai_output = get_assistant_response(user_input, thread.id, assistant.id, file_id)
        print(ai_output)
        ai_output_json = extract_json_from_string(ai_output)

        # 5. delete assistant
        client.beta.assistants.delete(assistant.id)

        return ai_output_json

    def convert_rmdText_to_html(self, response):
        questions = response['text'].split('\n')
        html_str = '<div class="deep-chat-temporary-message">'
        # 遍历所有问题，将每个问题添加到HTML字符串中
        for question in questions:
            # 删除问题编号
            question_text = re.sub(r"^\d+\.\s*", "", question)
            button_html = f'<button class="deep-chat-button deep-chat-suggestion-button" style="text-align: left; margin-top: 6px;">{question_text}</button><br>'
            html_str += button_html
        html_str += '</div>'

        return {'html': html_str}