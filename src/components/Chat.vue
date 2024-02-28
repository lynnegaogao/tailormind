<template>
    <div class="chat">
        <div class="chat-window">
            <deep-chat class="chat-area" id="deepChatComponent" ref="chatElementRef" :mixedFiles="true"
                :request="requestConfig" :introMessage="introMessage" :initialMessages="initialMessages"
                :messageStyles="messageStyles" :inputAreaStyle="inputAreaStyle"
                style="border-radius: 1px 1px 5px 5px;border: #fff;width:25vw;height:94vh">
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
            messages: [],
            newMessage: '',
            requestConfig: {
                url: "http://127.0.0.1:5000/files",
                method: "POST",
                // headers: { "Content-Type": "multipart/form-data" },

            },
            introMessage: {},
            initialMessages: [],
            messageStyles: {},
            inputAreaStyle: {},
            userSelection: 0,
        };
    },
    watch: {

    },
    mounted() {
        this.setupDeepChat();
        this.initializeChat();
        // this.setupRequestInterceptor()
    },

    methods: {
        initializeChat() {
            this.introMessage = {
                text: "Hi! I am your **AI Self-Regulated Learning (SRL)** assistant of Tailor-Mind~",
            };
            this.initialMessages = [
                {
                    html: `
            <div class="deep-chat-temporary-message">
              <button class="deep-chat-button deep-chat-suggestion-button" style="margin-top: 5px" @click="handleSRLClick">What is Self-Regulated Learning (SRL)?</button>
              <button class="deep-chat-button deep-chat-suggestion-button" style="margin-top: 6px">What does each view of Tailor-Mind do?</button>
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

        handleSRLClick() {
            this.userSelection = 1
            const deepChatComponent = this.$refs.chatElementRef;

        },

        setupDeepChat() {
            const deepChatComponent = this.$refs.chatElementRef;
            if (deepChatComponent) {
                // 设置新消息处理器
                deepChatComponent.onNewMessage = this.handleNewMessage;
            }
        },
        handleNewMessage(message) {
            console.log("新消息: ", message);
            // 在这里处理新消息，例如将其添加到显示消息的数组中
            if (message.message.files) {
                console.log(message.message.files)
            }
            //console.log(message.message)
        },

        fetchHistoryMessages() {
            const deepChatComponent = this.$refs.chatElementRef;
            if (deepChatComponent) {
                const messages = deepChatComponent.getMessages();
                console.log("历史消息: ", messages);
                // 在这里处理历史消息，例如将其保存到组件的数据属性中
                console.log(messages.message)
                //if messages
            }
        },

        setupRequestInterceptor() {
            const chatElementRef = this.$refs.chatElementRef;

            // 定义同步请求拦截器
            chatElementRef.requestInterceptor = (requestDetails) => {
                console.log(requestDetails); // 打印请求详情

                if (requestDetails.body instanceof FormData) {
                    // 如果是FormData，设置特定的URL
                    // requestDetails.url = "http://127.0.0.1:5000/chat";
                    console.log(requestDetails.url)
                    return{...requestDetails,
                    url: "http://127.0.0.1:5000/chat",}
                    
                } else {
                    // 如果不是FormData，保持URL不变
                    // requestDetails.url = requestDetails.url;
                    console.log(requestDetails.url)
                }

                return requestDetails; // 返回修改后的请求详情
            };


        },
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
