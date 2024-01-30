<template>
    <div class="chat">
        <div class="chat-window">

            <deep-chat class="chat-area" id="deepChatComponent" ref="chatElementRef" :mixedFiles="true" :directConnection='{
                "openAI": {
                    "key": "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",
                    "chat": { "max_tokens": 2000, "system_prompt": "Assist me with anything you can" }
                }
            }' :initialMessages='[
    { "text": "Hey, who are you?", "role": "user" },
    { "text": "I am your AI self-regulated learning assistant. It is nice to meet you and help you with your studies~", "role": "ai" },
]' :messageStyles='{
    "default": {
        "shared": { "bubble": { "color": "black" } },
        "user": { "bubble": { "backgroundColor": "#EEE1C7A2" } },
    },
    "file": {
        "shared": {
            "bubble": { "backgroundColor": "grey" }
        }
    }
}' :inputAreaStyle='{ "backgroundColor": "#EEE1C7A2" }' style="border-radius: 5px;width:30vw;height:93vh">
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
        };
    },
    watch: {

    },
    mounted() {
        this.setupDeepChat();
        //this.$nextTick(() => {
        //    setTimeout(() => {
        //        this.fetchHistoryMessages();
        //    }, 1000);
        //})

    },

    methods: {
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
        },
        fetchHistoryMessages() {
            const deepChatComponent = this.$refs.chatElementRef;
            if (deepChatComponent) {
                const messages = deepChatComponent.getMessages();
                console.log("历史消息: ", messages);
                // 在这里处理历史消息，例如将其保存到组件的数据属性中
            }
        },



    }
};
</script>
  
<style scoped>
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
