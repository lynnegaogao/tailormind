<template>
    <div class="chat">
        <div class="chat-window">

            <deep-chat class="chat-area" id="deepChatComponent" ref="chatElementRef" :mixedFiles="true" :request='{
                //"url": "http://127.0.0.1:5000/chat-stream",
                "url": "http://127.0.0.1:5000/sft-chat",
                "method": "POST",
                //"headers": { "Content-Type": "multipart/form-data" },
                //"additionalBodyProps": { "field": "value" }
            }' :introMessage='{
    "text": "Hi! I am your **AI Self-Regulated Learning (SRL)** assistant!~"
}' :initialMessages='[
    { "text": "Hey, please introduce **Self-Regulated Learning (SRL)**?", "role": "user" },
    { "text": "**Self-Regulated Learning (SRL)** refers to the process through which learners personally activate and sustain cognitions, affects, and behaviors that are systematically oriented toward the attainment of learning goals.", "role": "ai" },

    // {
    //     "html": `
    //   <div>
    //     <div style="margin-bottom: 10px;">Here is a simple <span style="color: orange;">example</span>: hihihi～～</div>
    //   </div>`,
    //     "role": "ai"
    // },
    { "text": "**Upload your learning material** and start your SRL journey!", "role": "ai" },
]' :messageStyles='{
    "default": {
        "shared": { "bubble": { "color": "black" } },
        "user": { "bubble": { "backgroundColor": "#EEE1C7A2" } },
    },
    "file": {
        "shared": {
            "bubble": { "backgroundColor": "#EEE1C7A2" }
        }
    }
}' :inputAreaStyle='{ "backgroundColor": "#EEE1C7A2" }'
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



    }
};
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
