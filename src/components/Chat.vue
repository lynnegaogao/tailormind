<template>
    <div class="chat">
        <div class="chat-window">
            <deep-chat class="chat-area" id="deepChatComponent" ref="chatElementRef" :mixedFiles="true"
                :request="requestConfig" :introMessage="introMessage" :initialMessages="initialMessages"
                :messageStyles="messageStyles" :inputAreaStyle="inputAreaStyle"
                style="border-radius: 1px 1px 5px 5px;border: #fff;width:24vw;height:94vh">
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
    },
    mounted() {
        this.setupDeepChat();
        this.initializeChat();
        this.setupRequestInterceptor();
        this.setupResponseInterceptor()
    },
    emits: ['getFileData','changeMindmapToDefault'],
    methods: {
        // 初始化
        initializeChat() {
            this.introMessage = {
                text: "Hi! I am your **AI Self-Regulated Learning (SRL)** assistant of Tailor-Mind~",
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
                //
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
            this.inputAreaStyle = { backgroundColor: "#EEE1C7A2" };
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
            // console.log("新消息: ", message);
            this.historyMessages.push(message)
            // console.log(this.historyMessages)
        },

        // request拦截器
        setupRequestInterceptor() {
            const chatElementRef = this.$refs.chatElementRef;
            // 定义同步请求拦截器
            var historyMessages = this.historyMessages
            chatElementRef.requestInterceptor = (requestDetails) => {
                // 拦截是否接受推荐mindmap的请求
                if (historyMessages[historyMessages.length - 2]&&historyMessages[historyMessages.length - 2].message.text == "Will you take the **Mindmap View** recommended by Tailor-Mind and make the next step in the **Learning Path View**?") {
                    if (historyMessages[historyMessages.length - 1].message.text == 'Yes') {
                        requestDetails.body.messages[0].text = 'keep mindmap data'
                        // console.log(historyMessages[historyMessages.length - 2])
                    }
                    else if (historyMessages[historyMessages.length - 1].message.text == 'No') {
                        requestDetails.body.messages[0].text = 'change mindmap data to default'
                    }
                }

                return requestDetails
            }
            //     if(historyMessages[historyMessages.length-1].message.text=='Yes'){
            //         requestDetails.body.messages[0].text='keep mindmap data'
            //         console.log(historyMessages[historyMessages.length-2])
            //     }else if(historyMessages[historyMessages.length-1].message.text=='No'){
            //         requestDetails.body.messages[0].text='change mindmap data to default'
            //     }
            // if(this.historyMessages[-1]){
            //     console.log('请求:',requestDetails);
            // }

            // return requestDetails; // 返回修改后的请求详情



        },

        // response拦截器
        setupResponseInterceptor() {
            const chatElementRef = this.$refs.chatElementRef;
            chatElementRef.responseInterceptor = (response) => {
                if (response['file']) {
                    // console.log('file-structure:',response['filestructure'])
                    // console.log('file:',response['file'])
                    this.$emit('getFileData', [response['file'], response['filestructure'], response['filesummary'], response['mindmap'],response['questionrmd']])
                    // console.log({ 'text': response['chatdata']['text'], 'text': response['filesummary'] })
                    return { 'text': response['chatdata']['text'], 'text': response['filesummary'] }
                }

                if(response['chatdata']['text']=='Changing the Mindmap View to default...'){
                    console.log('changeMindmapToDefault')
                    this.$emit('changeMindmapToDefault')
                }
                return response['chatdata']
            }

        },

        // interact with mindmap：对知识点进行问题推荐
        setupUserRequestQuestionRmd() {
            const chatElementRef = this.$refs.chatElementRef;
            chatElementRef.submitUserMessage({ 'text': `Recommend some questions about **${this.nodeToQuestionRmd}** for learning.` });

        },

        // interact with mindmap：选择推荐的mindmap还是自定义mindmap
        setupMindMapRmd() {
            const chatElementRef = this.$refs.chatElementRef;
            chatElementRef.submitUserMessage({ 'text': 'The learning material information has been loaded.' });

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
