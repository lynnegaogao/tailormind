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

knowledgeLevel=["Concept","Principle / Math formula","Application","Implementation","Significance / Influence","Related Knowledge","Contrast Knowledge","Extended Knowledge"]
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

                # 请求openai api获取file structure + knowledge list
                # 使用历史数据
                if historical==True:
                    with open('E:/Vis24-TailorMind/tailormind/back/history/1_material_overview.json', 'r') as file:
                        file_insights=json.load(file)
                    with open('E:/Vis24-TailorMind/tailormind/back/history/2_knowledge_list.json', 'r') as file:
                        knowledgeList=json.load(file)
                    
                # 用户实际数据
                else:
                    file_openai_response=self.get_file_insights(file_path)
                    file_insights=file_openai_response['fileoverview']
                    knowledgeList=file_openai_response['knowledgelist']
                
                fileStructure = file_insights['file_structure']
                fileSummary=file_insights['summary']
                
            # 请求sft获取relations，请求openai api获取推荐的mindmap数据
            relations=[]  
            # 使用历史数据
            if historical==True:
                with open('E:/Vis24-TailorMind/tailormind/back/history/3_relations.json', 'r') as file:
                        relations=json.load(file)
                with open('E:/Vis24-TailorMind/tailormind/back/history/4-mindmap.json', 'r') as file:
                        mindmap=json.load(file)
            # 用户实际数据
            else:
                for knowledge in knowledgeList:
                    prompt="For a given AI-related knowledge point, generate a triad of knowledge points associated with it. Each triad should be expressed in the form of [Topic,Relationship,Object] as a way to form a complete knowledge representation. Topic is the given knowledge point, object is the extended knowledge point related to the topic, and relation is the logical relationship between topic and object. For example, [[\"Convolutional Networks\", \"Loss Function\", \"Cross Entropy Loss\"],...]. The knowledge point is:"
                    body=prompt+knowledge
                    print("正在处理：",knowledge)
                    response=minderllm.generate(query=body)
                    print(response['text'])
                    relations.append(eval(response['text']))
                print(str(relations))
                mindmap=self.get_mindmap(str(relations))
                #     relations.append(relation)
                # for relation in eval(response['text']): 
                #     relations.append(relation)
                # with open('E:/Vis24-TailorMind/tailormind/back/history/3_relations.json', 'w') as file:
                #     json.dump(relations, file)
            # print("mindmap数据：",mindmap)
            
            # 请求sft获取relations
            questions_rmd=[]
            # 使用历史数据
            if historical==True:
                with open('E:/Vis24-TailorMind/tailormind/back/history/5-question_rmd.json', 'r') as file:
                        questions_rmd=json.load(file)
            # 用户实际数据
            else:
                for knowledge in knowledgeList:
                    for level_index in range(0,len(knowledgeLevel)):
                        body="Please recommend 1-2 question(s) about"+knowledge+"from a"+knowledgeLevel[level_index]+"perspective."
                        response=minderllm.generate(query=body)
                        questions = response['text'].split('\n')
                        for question in questions:
                            # 删除问题编号
                            question_text = re.sub(r"^\d+\.\s*", "", question)
                            question_obj={
                                "question":question_text,
                                "knowledgepoint": knowledge,
                                "level":level_index+1
                            }
                            print(question_obj)
                            questions_rmd.append(question_obj)
            # with open('E:/Vis24-TailorMind/tailormind/back/history/5-question_rmd.json', 'w') as file:
            #     json.dump(questions_rmd, file)   
            
            # 请求openai api获取learning path数据
             # 使用历史数据
            if historical==True:
                with open('E:/Vis24-TailorMind/tailormind/back/history/6-learning_path.json', 'r') as file:
                        learningPath=json.load(file)
            # 用户实际数据
            else:
                learningPath=self.get_learningpath(mindmap)
                
            response={
                'chatdata':{"text": "Get files! Loading..."},
                'filestructure':fileStructure,
                'file':file_data,
                'filesummary':fileSummary,
                'mindmap':mindmap,
                'questionrmd':questions_rmd,
                'learningpath':learningPath
            }
            
            return response

        else:
            body = request.json["messages"][0]['text']
            print("Text messages:",body )
            # 引导问题
            if body=='What is Self-Regulated Learning (SRL)?':
                response={"text":"Self-Regulated Learning (SRL) consists of 3 phases:📑📑📑\n 1. **Forethought**, planning and activation \n 2. **Performance**, monitoring and control \n 3. Reaction and **reflection**","html":"<div class=\"deep-chat-temporary-message\"><button class=\"deep-chat-button deep-chat-suggestion-button\" style=\"margin-top: 6px\">What does each view of Tailor-Mind do?</button><br><button class=\"deep-chat-button deep-chat-suggestion-button\" style=\"margin-top: 6px\">How can I start my SRL journey?</button></div>"}
            elif body=='What does each view of Tailor-Mind do?':
                response={"text":"🎈Some guidances will be coming...","html":"<div class=\"deep-chat-temporary-message\"><button class=\"deep-chat-button deep-chat-suggestion-button\" style=\"margin-top: 6px\">How can I start my SRL journey?</button></div>"}
            elif body=='How can I start my SRL journey?':
                response={"text":"🥳**Upload your learning material** and start your SRL journey!"}
            # 问题推荐
            elif body.startswith("Recommend some questions"):
                response=minderllm.generate(query=body)
                # 需要删除，暂时使用
                # response={"text":"1. What is Self-Regulated Learning (SRL)?\n2. What does each view of Tailor-Mind do?\n3. How can I start my SRL journey?"}
                html_response=self.convert_rmdText_to_html(response)
                response=html_response
            # 询问是否接受推荐的mindmap数据
            elif body=='The learning material information has been loaded.':
                response={
                    "text": "🤲Will you take the **Mindmap View** recommended by Tailor-Mind and make the next step in the **Learning Path View**?",
                    "html": "<div class=\"deep-chat-temporary-message\"><button class=\"deep-chat-button deep-chat-suggestion-button\" style=\"border: 1px solid green; margin-right: 10px\">Yes</button><button class=\"deep-chat-button deep-chat-suggestion-button\" style=\"border: 1px solid #d80000\">No</button></div>",
                }
            # 接受推荐的mindmap数据+生成推荐的learning path
            elif body=='keep mindmap data':
                
                response={
                    "text": "👻Generating recommended Learning Path...",
                }
            # 将mindmap修改为默认数据（level=0和size=1）
            elif body=='change mindmap data to default':
                response={
                    "text": "🎈Changing the Mindmap View to default...",
                }
            # 询问是否进入reflection阶段
            elif body=='end':
                response={
                    "text": "👻Will you finish your learning? \nAnd ready to start the **Reflection** phase?🤩",
                    "html": "<div class=\"deep-chat-temporary-message\"><button class=\"deep-chat-button deep-chat-suggestion-button\" style=\"border: 1px solid green; margin-right: 10px\">Yes</button><button class=\"deep-chat-button deep-chat-suggestion-button\" style=\"border: 1px solid #d80000\">No</button></div>",
                }
            elif body=='continue learning':
                response={
                    "text": "👻Please follow the learning path to continue your learning...",
                }
            elif body=='start reflection phase':
                response={
                    "text": "🥳Let's move on to the self-reflection~",
                }
            elif body=="Let's start the last phase!🎈":
                response={
                    "text": "👻Will you finish your reviewing? \nAnd ready to do any tests?🤩",
                    "html": "<div class=\"deep-chat-temporary-message\"><button class=\"deep-chat-button deep-chat-suggestion-button\" style=\"border: 1px solid green; margin-right: 10px\">Yes</button><button class=\"deep-chat-button deep-chat-suggestion-button\" style=\"border: 1px solid #d80000\">No</button></div>",
                }
            # 其他正常问答
            else:
                response=minderllm.generate(query=body)
                # 需要删除，暂时使用
                # response={"text":"Some guidances will be coming...","html":"<div class=\"deep-chat-temporary-message\"><button class=\"deep-chat-button deep-chat-suggestion-button\" style=\"margin-top: 6px\">What does each view of Tailor-Mind do?</button><br><button class=\"deep-chat-button deep-chat-suggestion-button\" style=\"margin-top: 6px\">How can I start my SRL journey?</button></div>"}

            print("Response:",response)
            return {'chatdata':response}


    def get_file_insights(self, file_path):
        # prompt-1 file structure + overview
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
        # prompt-2 knowledge list
        sample_list=['Convex Sets',"Jensen's Inequality",'Convex Optimization','Linear Programming','Quadratic Programming','QCQP','SDP','Lagrangian dyadic problems']
        user_input_list='Give all the AI or deep learning related knowledge points contained in the file to avoid duplication.Only return Json code without any other content. The Json format refers to the example below:```json\n'+ json.dumps(sample_list) + '\n```'

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
        
        client = OpenAI(api_key=OPENAI_API_KEY)
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
            instructions="You are a personal file analyzer. When giving you a file and some questions, retrieve and analyze the content of this file as you can and answer the questions as required. If you cannot parse the required Json output, you can give an empty structure that contains only keys.",
            tools=[{"type": "retrieval"}],
            model="gpt-4-0125-preview",
            file_ids=[file_id]
        )

        # 2. create Thread
        thread = client.beta.threads.create() # （可选）在创建时指定对话内容

        # 获取file-overview
        file_overview = get_assistant_response(user_input, thread.id, assistant.id, file_id)
        print(file_overview)
        file_overview_json = extract_json_from_string(file_overview)
        
        # 获取knowledge list
        knowledge_list=get_assistant_response(user_input_list, thread.id, assistant.id, file_id)
        print(knowledge_list)
        knowledge_list_json=extract_json_from_string(knowledge_list)
        
        # 5. delete assistant
        # client.beta.assistants.delete(assistant.id)

        return {'fileoverview':file_overview_json,'knowledgelist':knowledge_list_json}

    def get_mindmap(self,content):
        sample={
        "nodes": [
        {
            "id": "Finite Horizon Markov Decision Process (MDP)",
            "label": "Finite Horizon Markov Decision Process (MDP)",
            "level": 2,
            "size": 5,
        },
        {
            "id": "Linear Quadratic Regulator (LQR)",
            "label": "Linear Quadratic Regulator (LQR)",
            "level": 6,
            "size": 3,
        },
        {
            "id": "Differential Dynamic Programming (DDP)",
            "label": "Differential Dynamic Programming (DDP)",
            "level": 4,
            "size": 2,
        }
    ],
        "links": [
        {
            "source": "Optimal Control Theory",
            "target": "Finite Horizon Markov Decision Process (MDP)",
            "relation": "includes"
        },
        {
            "source": "Finite Horizon Markov Decision Process (MDP)",
            "target": "Markov Chain",
            "relation": "extends"
        },
        {
            "source": "Linear Quadratic Regulator (LQR)",
            "target": "State Space Model",
            "relation": "uses"
        }
    ]
    }
        sample_str = "```json\n" + json.dumps(sample) + "\n```"
        prompt="Parsing the content of this paragraph, each ternary represents [subject, relationship, object], the following data conversion: 1.subject and object are both elements in nodes, \"id\" and \"label\" are the same. 2.\"level\" is an integer between [1,8], 1-8 corresponds to the relationship of learning level as {1: \"Concept\",2: \"Principle / Math formula\",3: \"Application\",4: \"Implementation\",5: \" Significance / Influence\",6: \"Related Knowledge\",7: \"Contrast Knowledge\",8: \"Extended Knowledge\"}, please make a recommendation to a beginner based on the level of knowledge a beginner need to master this knowledge; 3. \"size\" is an integer between [1,5], which indicates the importance of this knowledge, 1 means common, 5 means important, need to be differentiated, please make a recommendation to a beginner; 4. each ternary as links in the elements, \"source\" for the subject, \"target\" is the object, \"relationship\" is the relationship. Only return json data, the format is as follows:"
        user_input=content+prompt+sample_str
        
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
            # 从消息中取出 AI 输出的 JSON 字符串
        ai_output = messages.data[0].content[0].text.value
        
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
            
        ai_output_json=extract_json_from_string(ai_output)
        
        return ai_output_json
    
    def get_learningpath(self,content):
        sample=[{
          "start": 0.00,
          "level": 1,
          "milestone": "Ensemble Learning",
          "importance": 4,
          "subknowledge": [
              {
                  "level": 2,
                  "knowledge": "Concept of Ensemble Learning",
                  "importance": 5,
                  "content": "Ensemble Learning is a machine learning technique that combines several base models in order to produce one optimal predictive model."
              },
              {
                  "level": 2,
                  "knowledge": "Benefits of Ensemble Learning",
                  "importance": 2,
                  "content": "Enhances prediction accuracy and reduces the likelihood of model overfitting by leveraging the strengths of multiple models."
              },
          ]
      },   
      {
          "start": 0.6,
          "level": 5,
          "milestone": "Stacking",
          "importance": 2,
          "subknowledge": [
              {
                  "level": 6,
                  "knowledge": "Introduction to Stacking",
                  "importance": 3,
                  "content": "Stacking involves training a new model to combine the predictions of several base models for improved prediction accuracy."
              },
              {
                  "level": 6,
                  "knowledge": "How Stacking Works",
                  "importance": 3,
                  "content": "It works by using a meta-learner or blender that learns how to best combine the predictions of multiple base models."
              },
              {
                  "level": 6,
                  "knowledge": "Implementing Stacking Models",
                  "importance": 3,
                  "content": "Implementation involves selecting base models, training them on the data, and then training a meta-model to aggregate their predictions."
              },
              {
                  "level": 6,
                  "knowledge": "Use Cases and Examples of Stacking",
                  "importance": 3,
                  "content": "Stacking is widely used in various domains like finance, healthcare, and image recognition for enhancing predictive performance."
              }
          ]
      }]
        sample_str = "```json\n" + json.dumps(sample) + "\n```"
        prompt = """
        Drawing from the structured knowledge map provided, we propose a self-learning pathway tailored for beginners, comprising approximately 8-10 pivotal milestones. 
        The pathway initiates at a starting point labeled "start" ranging from 0 to 1. 
        Each learning objective is categorized under "level" with a scale from 1 to 8, where each level represents a progressive learning stage as follows:
        {1: "Concept", 2: "Principle / Math formula", 3: "Principle / Math formula", 4: "Implementation", 5: "Significance / Influence", 6: "Related Knowledge", 7: "Contrast Knowledge", 8: "Extended Knowledge"}. 
        This categorization aids in crafting a bespoke recommendation for beginners, aligning with the essential knowledge levels they must achieve.
        Furthermore, "milestone" signifies critical knowledge points within the entire knowledge map, serving as significant markers in the learning journey. 
        The "importance" of each milestone is rated on a scale from 1 to 5, with higher values indicating greater significance. 
        Additionally, "subknowledge" outlines essential subtopics under each milestone, where "knowledge" refers to the specific knowledge point, and "content" provides a concise explanation of this point.
        Please ensure the returned data is in JSON format, with the array length exceeding 8 entries, structured as outlined:
        """

        user_input=json.dumps(content)+prompt+sample_str
        
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
            # 从消息中取出 AI 输出的 JSON 字符串
        ai_output = messages.data[0].content[0].text.value
        
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
            
        ai_output_json=extract_json_from_string(ai_output)
        
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