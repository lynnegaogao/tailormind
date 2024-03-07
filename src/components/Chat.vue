<template>
    <div class="chat">
        <div class="chat-window">
            <deep-chat class="chat-area" id="deepChatComponent" ref="chatElementRef" :mixedFiles="true"
                :request="requestConfig" :introMessage="introMessage" :initialMessages="initialMessages"
                :messageStyles="messageStyles" :inputAreaStyle="inputAreaStyle"
                style="border-radius: 1px 1px 5px 5px;border: #8F939C;width:24vw;height:94vh">
            </deep-chat>
        </div>

    </div>
</template>

<script>
import { ref } from "vue";
import { Textarea } from 'ant-design-vue';
import { Button } from 'ant-design-vue';
import 'deep-chat';

export default {
    name: 'ChatComponent',
    components: {
        'a-textarea': Textarea,
        'a-button': Button,
    },
    setup() {

    },
    data() {
        return {
            historyMessages: [],
            reflectionHistoryMessages: [],
            newMessage: '',
            requestConfig: {
                url: "http://127.0.0.1:5000/files",
                method: "POST",
            },
            introMessage: {},
            initialMessages: [],
            messageStyles: {},
            inputAreaStyle: {},
            userSelection: 0,
            milestoneNum: 0,
            isTesting: false,
        };
    },
    props: {
        nodeToQuestionRmd: {
            type: String,
            default: function () { return ''; },
        },
        getFileStatus: {
            type: Boolean,
            default: false,
        },
        isReflection: {
            type: Boolean,
            default: false,
        },
        testingQuestionList: {
            type: Array,
            default: function () { return []; },
        },
        learningPathData: {
            type: Array,
            default: function () { return []; },
        },
        knowledgeCard:{
            type: String,
            default: function () { return ''; },
        }
    },
    watch: {
        nodeToQuestionRmd(newValue, oldValue) {
            console.log(newValue, oldValue)
            this.$nextTick(() => {
                this.setupUserRequestQuestionRmd()
            })
        },
        getFileStatus(newValue, oldValue) {
            console.log(newValue, oldValue)
            if (newValue) {
                this.$nextTick(() => {
                    this.setupMindMapRmd()
                })
            }

        },
        isReflection(newValue, oldValue) {
            console.log(newValue, oldValue)
            if (newValue) {
                this.$nextTick(() => {
                    this.setupReflectionStart()
                })
            }

        },
        knowledgeCard(newValue, oldValue) {
            console.log(newValue, oldValue)
            if (newValue) {
                this.$nextTick(() => {
                    this.setupAskKnowledgeCard(newValue)
                })
            }

        },
    },
    mounted() {
        this.setupDeepChat();
        this.initializeChat();
        this.setupRequestInterceptor();
        this.setupResponseInterceptor()
    },
    emits: ['getFileData', 'changeMindmapToDefault', 'submitChatHistory', 'changePathContrast','getAdjustedLearningPathData'],
    methods: {
        // 初始化
        initializeChat() {
            this.introMessage = {
                text: "Hi! I am your **AI Self-Regulated Learning (SRL)** assistant of Tailor-Mind~🤩",
            };
            this.initialMessages = [
                {
                    html: `
            <div class="deep-chat-temporary-message">
              <button class="deep-chat-button deep-chat-suggestion-button" style="margin-top: 5px">What is Self-Regulated Learning (SRL)?</button><br>
              <button class="deep-chat-button deep-chat-suggestion-button" style="margin-top: 6px">What does each view of Tailor-Mind do?</button><br>
              <button class="deep-chat-button deep-chat-suggestion-button" style="margin-top: 6px">How can I start my SRL journey?</button>
            </div>`,
                    role: 'ai',
                },
            ];
            this.messageStyles = {
                default: {
                    shared: { bubble: { color: "black" } },
                    user: { bubble: { backgroundColor: "#EEE1C7A2" } },
                },
                file: {
                    shared: {
                        bubble: { backgroundColor: "#EEE1C7A2" },
                    },
                },
                html: {
                    shared: {
                        bubble: { backgroundColor: "unset", padding: '0px' }
                    }
                }
            };
            this.inputAreaStyle = { backgroundColor: "#ADB5C7" };
        },

        // 捕捉当前返回的消息
        setupDeepChat() {
            const deepChatComponent = this.$refs.chatElementRef;
            if (deepChatComponent) {
                // 设置新消息处理器
                deepChatComponent.onNewMessage = this.handleNewMessage;
            }
        },
        handleNewMessage(message) {
            if (!this.isTesting) {
                this.historyMessages.push(message)
            } else {
                this.reflectionHistoryMessages.push(message)
            }

        },

        // request拦截器
        setupRequestInterceptor() {
            const chatElementRef = this.$refs.chatElementRef;
            // 定义同步请求拦截器
            var historyMessages = this.historyMessages
            chatElementRef.requestInterceptor = (requestDetails) => {
                // 拦截是否接受推荐mindmap的请求
                if (historyMessages[historyMessages.length - 2] && historyMessages[historyMessages.length - 2].message.text == "🤲Will you take the **Mindmap View** recommended by Tailor-Mind and make the next step in the **Learning Path View**?") {
                    if (historyMessages[historyMessages.length - 1].message.text == 'Yes') {
                        requestDetails.body.messages[0].text = 'keep mindmap data'
                    }
                    else if (historyMessages[historyMessages.length - 1].message.text == 'No') {
                        requestDetails.body.messages[0].text = 'change mindmap data to default'
                    }
                }
                // 拦截是否结束学习，进入reflection阶段
                if (historyMessages[historyMessages.length - 2] && historyMessages[historyMessages.length - 2].message.text == "👻Will you finish your learning? \nAnd ready to start the **Reflection** phase?🤩") {
                    if (historyMessages[historyMessages.length - 1].message.text == 'Yes') {
                        requestDetails.body.messages[0].text = 'start reflection phase'

                    }
                    else if (historyMessages[historyMessages.length - 1].message.text == 'No') {
                        requestDetails.body.messages[0].text = 'continue learning'
                    }
                }
                // 拦截是否开始完成自测题
                if (historyMessages[historyMessages.length - 2] && historyMessages[historyMessages.length - 2].message.text == "👻Will you finish your reviewing? \nAnd ready to do any tests?💯") {
                    if (historyMessages[historyMessages.length - 1].message.text == 'Yes') {
                        requestDetails.body.messages[0].text = 'start testing!'
                        this.isTesting = true
                        historyMessages = this.reflectionHistoryMessages
                        requestDetails.body.milestone = this.learningPathData[0].milestone
                        this.milestoneNum += 1
                        // console.log(requestDetails)
                    }
                    else if (historyMessages[historyMessages.length - 1].message.text == 'No') {
                        requestDetails.body.messages[0].text = 'continue learning'
                    }
                }
                // 拦截是否继续出选择题
                if (historyMessages[historyMessages.length - 1] && historyMessages[historyMessages.length - 1].message.text && this.startsWithABCD(historyMessages[historyMessages.length - 1].message.text) && this.milestoneNum < this.learningPathData.length) {
                    // console.log(requestDetails)
                    requestDetails.body.messages[0].text = 'continue asking selections'
                    requestDetails.body.milestone = this.learningPathData[this.milestoneNum].milestone
                    this.milestoneNum += 1
                    // 衔接出判断题
                    if (this.milestoneNum == this.learningPathData.length) {
                        requestDetails.body.messages[0].text = 'continue asking TRUE OR FALSE judgement'
                        this.milestoneNum = 0
                        requestDetails.body.milestone = this.learningPathData[this.milestoneNum].milestone
                    }
                }
                //拦截是否继续出判断题
                if (historyMessages[historyMessages.length - 1] && historyMessages[historyMessages.length - 1].message.text && this.startsWithTrueOrFalse(historyMessages[historyMessages.length - 1].message.text) && this.milestoneNum < this.learningPathData.length) {
                    requestDetails.body.messages[0].text = 'continue asking TRUE OR FALSE judgement'
                    requestDetails.body.milestone = this.learningPathData[this.milestoneNum].milestone
                    this.milestoneNum += 1
                    // 结束自测，进入评估
                    if (this.milestoneNum == this.learningPathData.length) {
                        requestDetails.body.messages[0].text = 'test finished'
                        requestDetails.body.history = this.reflectionHistoryMessages
                        requestDetails.body.learningpath = this.learningPathData
                        console.log(requestDetails)
                        this.$emit('changePathContrast')
                    }

                }
                return requestDetails
            }

        },

        // response拦截器
        setupResponseInterceptor() {
            const chatElementRef = this.$refs.chatElementRef;
            chatElementRef.responseInterceptor = (response) => {
                // 获取上传的learning material相关数据
                if (response['file']) {
                    this.$emit('getFileData',
                        [
                            response['file'],
                            response['filestructure'],
                            response['filesummary'],
                            response['mindmap'],
                            response['questionrmd'],
                            response['learningpath']
                        ]
                    )
                    return { 'text': response['chatdata']['text'], 'text': response['filesummary'] }
                }
                // 用户自定义mindmap和learning path
                if (response['chatdata'] && response['chatdata']['text'] == '🎈Changing the Mindmap View to default...') {
                    console.log('change mindmap to default')
                    this.$emit('changeMindmapToDefault')
                }
                // 提交学习阶段的对话数据
                if (response['chatdata'] && response['chatdata']['text'] == "🥳Let's move on to the self-reflection~") {
                    console.log('submit history messages')
                    this.$emit('submitChatHistory', this.historyMessages)
                }
                // 获取反馈之后的adjusted learning path数据
                if(response['reflection']&&response['learningpath']){
                    this.$emit('getAdjustedLearningPathData',response['learningpath'])
                }
                return response['chatdata']
            }

        },

        // interact with mindmap：对知识点进行问题推荐
        setupUserRequestQuestionRmd() {
            const chatElementRef = this.$refs.chatElementRef;
            chatElementRef.submitUserMessage({ 'text': `Recommend some questions about **${this.nodeToQuestionRmd}** for learning.👀` });

        },

        // interact with mindmap：选择推荐的mindmap还是自定义mindmap
        setupMindMapRmd() {
            const chatElementRef = this.$refs.chatElementRef;
            chatElementRef.submitUserMessage({ 'text': 'The learning material information has been loaded.' });

        },

        // interact with reflection router：没用呢。。。
        setupReflectionStart() {
            const chatElementRef = this.$refs.chatElementRef;
            chatElementRef.submitUserMessage({ 'text': "Let's start the last phase!🎈" });
        },

        // 继续进行自测的一些判断
        startsWithABCD(str) {
            return str.startsWith("A.") || str.startsWith("B.") || str.startsWith("C.") || str.startsWith("D.") ||
                str.startsWith("A)") || str.startsWith("B)") || str.startsWith("C)") || str.startsWith("D)");
        },
        startsWithTrueOrFalse(str) {
            return str == "True" || str == "False"
        },

        // interat with file preview: 提问knowledgeCard
        setupAskKnowledgeCard(knowledgeCard){
            const chatElementRef = this.$refs.chatElementRef;
            chatElementRef.submitUserMessage({ 'text': "Please explain the following context:"+knowledgeCard });
        }
    }
}
</script>

<style>
.chat {
    display: flex;
    flex-direction: column;
    height: 100%;
    width: 100%;
}

.chat-window {
    flex-grow: 1;
    overflow-y: auto;
}

.chat-area {
    width: 100%;
    height: 100%;
}

.input-area {
    box-sizing: border-box;
    margin-top: 5px;
    margin-bottom: 5px;
    margin-left: 5px;
    margin-right: 5px;
    width: 98%;
}

.message {
    padding: 10px 15px;
    border-radius: 15px;
    margin: 5px;
    max-width: 70%;
    word-break: break-word;
}

.system-message {
    background-color: white;
    color: #7e7d7f;
    align-self: flex-start;
}

.user-message {
    background-color: #E8D4AD91;
    color: #7e7d7f;
    align-self: flex-end;
}

.my-message {
    text-align: right;
}
</style>
