<template>
    <div id="container">
        <router-view :key="$route.fullPath"></router-view>
        <div class="system-header">
            Tailor-Mind
            <div class="system-introduction"> Advancing Your Self-Regulated Learning Journey </div>
        </div>

        <div class="system-component">
            <!-- 对话 -->
            <div id="column-1">
                <!-- 对话 -->
                <div id="chat-view" class="module-block">
                    <div class="module-header">
                        <img src="./assets/Chats.png" alt="Icon" class="icon" />
                        CHAT
                    </div>
                    <div class="module-component">
                        <chat :isReflection="isReflection" :key="componentKey"/>
                    </div>
                </div>
            </div>

            <!-- 笔记 + 思维导图 + 学习路径前后比较 -->
            <div id="column-2">
                <!-- 笔记+知识点思维导图 -->
                <div id="row-1" class="row">
                    <!-- 笔记 -->
                    <div id="notes-view" class="module-block">
                        <div class="module-header">
                            <img src="./assets/Note.png" alt="Icon" class="icon" />
                            NOTES
                        </div>
                        <div class="module-component">
                            <markdownRenderer style="padding:10px" />
                        </div>
                    </div>

                    <!-- 知识点思维导图 -->
                    <div id="knowledge-mindmap-view" class="module-block">
                        <div class="module-header">
                            <img src="./assets/Mindmap.png" alt="Icon" class="icon" />
                            KNOWLEDGE MINDMAP
                        </div>
                        <div class="module-component">
                            <mindmap :mindMapData='mindMapData' :isReflection="isReflection" :key="componentKey"/>
                        </div>
                    </div>

                </div>

                <!-- 学习路径前后比较 -->
                <div id="row-2" class="row">
                    <div id="learning-path-view" class="module-block">
                        <div class="module-header">
                            <img src="./assets/Learningpath.png" alt="Icon" class="icon" />
                            LEARNING PATH -- BEFORE
                        </div>
                        <div class="module-component">
                            <learningPath :learningPathData="learningPathData" :isReflection="isReflection" :key="componentKey"/>
                        </div>
                    </div>

                    <div id="learning-path-view" class="module-block">
                        <div class="module-header">
                            <img src="./assets/Learningpath.png" alt="Icon" class="icon" />
                            LEARNING PATH -- AFTER
                        </div>
                        <div class="module-component">
                            <learningPath :learningPathData="learningPathData" />
                        </div>
                    </div>

                </div>

            </div>

        </div>

    </div>
</template>

<script>
import filePreview from './components/FilePreview.vue'
import chat from './components/Chat.vue'
import mindmap from './components/Mindmap.vue'
import noteEditor from './components/NoteEditor.vue'
import learningPath from './components/LearningPath.vue'
import questionRmd from './components/QuestionRmd.vue'
import markdownRenderer from './components/MarkdownRenderer.vue'

import DataService from "./utils/data-service"

export default {
    name: 'forethought',
    components: {
        filePreview,
        chat,
        mindmap,
        noteEditor,
        learningPath,
        questionRmd,
        markdownRenderer
    },
    data() {
        return {
            learningPathData: [],
            submitChatData: [],
            mindMapData: [],
            isReflection: true,

        }
    },
    mounted() {
        this.isReflection=true
        console.log(this.learningPathData,this.submitChatData,this.mindMapData)
    },
    created() {
        this.$store.watch((state) => {
            this.learningPathData = state.learningPathData
            this.submitChatData = state.submitChatData
            this.mindMapData = state.mindMapData

        })

    },
    methods: {

    },

}
</script>

<style scoped>
#container {
    display: flex;
    flex-direction: column;
    width: 100vw;
    height: 100vh;
}

.system-header {
    display: flex;
    margin-bottom: 5px;
    background-color: #4c5874d1;
    color: #ffffff;
    text-align: left;
    font-weight: bold;
    font-size: 18px;
    padding: 5px;
    flex-grow: 1;
}

.system-introduction {
    color: #c5d0ea;
    font-size: 15px;
    padding-left: 10px;
    padding-top: 4px;
    font-family: 'Arial', sans-serif;
    font-weight: 100;
    font-style: italic;
}

.system-component {
    display: flex;
    width: 100vw;
    height: 100vh;
    flex-grow: 1;
}

.column {
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100%;
    flex-grow: 1;
}

.module-header {
    color: #565d6bb7;
    font-size: 0.8em;
    margin-top: 5px;
    /*margin-bottom: 20px;*/
    width: 100%;
    font-weight: bold;
    display: flex;
    justify-content: flex-start;
    /* 使所有元素居左 */
    border-bottom: 2px solid #eee;
    /* 添加分界线 */
}

.module-block {
    display: flex;
    border-radius: 5px;
    box-shadow: 0 3px 8px rgba(0, 0, 0, 0.2);
    background-color: #fff;
    margin-bottom: 5px;
    margin-right: 3px;
    background: #fff;
    flex-direction: column;
    height: 100%
}

.module-component {
    display: flex;
    width: 100%;
    height: 100%;
}

.icon {
    width: 25px;
    height: 25px;
    margin-left: 10px;
    margin-right: 10px;
}

#column-1 {
    flex: 2;
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
}

#column-2 {
    flex: 6.5;
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
}

#row-1 {
    flex: 7;
    display: flex;
    height: 100%;
    width: 100%;
    flex-direction: row;
}

#row-2 {
    flex: 4;
    display: flex;
    height: 100%;
    width: 100%;
    flex-direction: row;
}


#notes-view {
    flex: 1;
    /* max-height: 700px; */
}


#knowledge-mindmap-view {
    flex: 1;
    /* max-height: 700px; */
}

#learning-path-view {
    flex: 1;
}

#question-recommendation-view {
    flex: 1;
}

#chat-view {
    flex: 1;
}
</style>