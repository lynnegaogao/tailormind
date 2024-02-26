<template>
  <div id="container">

    <div class="system-header">
      Tailor-Mind
    </div>

    <div class="system-component">
      <!-- 对话 -->
      <div id="column-1" class="column">

        <!-- 对话 -->
        <div id="chat-view" class="module-block">
          <div class="module-header">
            <img src="./assets/Chats.png" alt="Icon" class="icon" />
            CHAT
          </div>
          <div class="module-component">
            <chat />
          </div>
        </div>
        <!-- 文件上传 -->
        <!--<div id="upload-file-view" class="module-block">
          <div class="module-header">
            <img src="./assets/Upload.png" alt="Icon" class="icon" />
            UPLOAD FILE
          </div>
          <div class="module-component">
            <uploadFile @getFileContent="onGetFileContent"/>
          </div>
        </div>-->


      </div>

      <!-- 文件预览+问题推荐 -->
      <div id="column-2" class="column">
        <!-- 文件预览 -->
        <div id="file-preview-view" class="module-block">
          <div class="module-header">
            <img src="./assets/Documents.png" alt="Icon" class="icon" />
            FILE PREVIEW
          </div>
          <div class="module-component">
            <filePreview/>
          </div>
        </div>

        <!-- 问题推荐 -->
        <div id="question-recommendation-view" class="module-block">
          <div class="module-header">
            <img src="./assets/Recommendation.png" alt="Icon" class="icon" />
            QUESTION RECOMMENDATION
          </div>
          <div class="module-component">

          </div>
        </div>

      </div>

      <!-- 知识点思维导图+学习路径 -->
      <div id="column-3" class="column">
        <!-- 知识点思维导图 -->
        <div id="knowledge-mindmap-view" class="module-block">
          <div class="module-header">
            <img src="./assets/Mindmap.png" alt="Icon" class="icon" />
            KNOWLEDGE MINDMAP
          </div>
          <div class="module-component">
            <mindmap style="flex: 4;" @generateWordCloud='onGenerateWordCloud' :wordCloudData='wordCloudData'
              :submitNode='submitNode' />
            <mindmapSidebar style="flex: 1;" />
          </div>
        </div>

        <!-- 学习路径 -->
        <div id="learning-path-view" class="module-block">
          <div class="module-header">
            <img src="./assets/Learningpath.png" alt="Icon" class="icon" />
            LEARNING PATH
          </div>
          <div class="module-component">

          </div>
        </div>

        <!-- 编辑笔记 -->
        <!--<div id="edit-notes-view" class="module-block">
          <div class="module-header">
            <img src="./assets/Note.png" alt="Icon" class="icon" />
            EDIT NOTES
          </div>
          <div class="module-component">

          </div>
        </div>-->

        <!-- 自测 -->
        <!--<div id="self-examination-view" class="module-block">
          <div class="module-header">
            <img src="./assets/Exam.png" alt="Icon" class="icon" />
            SELF EXAMINATION
          </div>
          <div class="module-component">

          </div>
        </div>-->

        <!-- 反馈 -->
        <!--<div id="feedback-view" class="module-block">
          <div class="module-header">
            <img src="./assets/Feedback.png" alt="Icon" class="icon" />
            FEEDBACK
          </div>
          <div class="module-component">

          </div>
        </div>-->

      </div>

    </div>

  </div>
</template>

<script>
import uploadFile from './components/UploadFile.vue'
import filePreview from './components/FilePreview.vue'
import chat from './components/Chat.vue'
import mindmap from './components/Mindmap.vue'
import mindmapSidebar from './components/MindmapSidebar.vue'

import DataService from "./utils/data-service"

export default {
  name: 'forethought',
  components: {
    uploadFile,
    filePreview,
    chat,
    mindmap,
    mindmapSidebar
  },
  data() {
    return {
      getFileStatus: false,
      wordCloudData: null,

    }
  },
  mounted() {

  },
  methods: {
    // 后端获取文件
    onGetFileContent(file) {
      var formData = new FormData()
      formData.append('file', file)
      DataService.constructor()
      DataService.getFileContent(formData, (backendData) => {
        console.log('backendData:', backendData);
        this.getFileStatus = true;
      })
    },

    // 处理提交的笔记，生成词云
    onGenerateWordCloud(node, noteContext) {
      DataService.getWordCloudData(node, noteContext, (wordCloudData) => {
        //this.wordCloudData.nodeId=node.id()
        //this.wordCloudData.node = node
        //this.wordCloudData.data = wordCloudData
        this.wordCloudData={
          'nodeId':node.id(),
          'node':node,
          'data' : wordCloudData
        }
        console.log('wordCloudData:', this.wordCloudData);
      })
    },

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
  justify-content: center;
  align-items: center;
  border-radius: 5px;
  margin-bottom: 5px;
  background-color: #eee1c7;
  color: #7e7d7f;
  text-align: left;
  font-weight: bold;
  font-size: 1em;
  padding: 5px;
  flex-grow: 1;
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
  color: #aaa;
  font-size: 0.8em;
  margin-top: 5px;
  /*margin-bottom: 20px;*/
  width: 100%;
  font-weight: bold;
  display: flex;
  justify-content: flex-start;
  /* 使所有元素居左 */
  border-bottom: 1.5px solid #eee;
  /* 添加分界线 */
}

.module-block {
  display: flex;
  /* justify-content: center; */
  /* align-items: center; */
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
}

#column-2 {
  flex: 2.5;
  height: 100%;
}

#column-3 {
  flex: 4;
  height: 100%;
}


#file-preview-view {
  flex: 3;
}


#knowledge-mindmap-view {
  flex: 3;
}

#learning-path-view {
  flex: 2;
}

#question-recommendation-view {
  flex: 2;
}

#chat-view {
  flex: 1;
}
</style>
