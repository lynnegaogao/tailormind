<template>
    <div class="chat">
        <div class="chat-window">
            <div v-for="message in messages" :key="message.id" class="message"
                :class="{ 'user-message': message.own, 'system-message': !message.own }">
                <div>
                    {{ message.text }}
                </div>
            </div>
        </div>
        <div class="input-area">
            <br />
            <a-textarea rows="4" placeholder="enter your question~" v-model:value="newMessage"
                @keydown="handleCommandEnter" />
        </div>
    </div>
</template>
  
<script>
import { Textarea } from 'ant-design-vue';
import { Button } from 'ant-design-vue';

export default {
    name: 'ChatComponent',
    components: {
        'a-textarea': Textarea,
        'a-button': Button,
    },
    data() {
        return {
            messages: [],
            newMessage: ''
        };
    },
    methods: {
        handleCommandEnter(event) {
            // 在 Mac 上，metaKey 是 Command 键，在 Windows/Linux 上通常是 Windows 键
            if (event.metaKey && event.key === 'Enter') {
                this.sendMessage()
            }
        },

        sendMessage() {
            //console.log("triggered!")
            console.log(this.newMessage)
            if (this.newMessage.trim() !== '') {
                console.log("triggered!")
                this.messages.push({
                    id: this.messages.length + 1,
                    text: this.newMessage,
                    own: true
                });
                console.log(this.messages)
                this.newMessage = '';
            }
        }
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
