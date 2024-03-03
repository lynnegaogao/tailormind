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
            <chat @getFileData="onGetFileData" :nodeToQuestionRmd="nodeToQuestionRmd" />
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
            <filePreview :fileStructureData="fileStructureData" :fileData="fileData" :cardData="cardData"/>
          </div>
        </div>

        <!-- 问题推荐 -->
        <div id="question-recommendation-view" class="module-block">
          <div class="module-header">
            <img src="./assets/Recommendation.png" alt="Icon" class="icon" />
            QUESTION RECOMMENDATION
          </div>
          <div class="module-component">
            <questionRmd />
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
            <mindmap style="flex: 4;" :mindMapData='mindMapData' @generateWordCloud='onGenerateWordCloud' :wordCloudData='wordCloudData'
              :submitNode='submitNode' @getQuestionRmd='onGetQuestionRmd' />
            <noteEditor style="flex: 2;" />
          </div>
        </div>

        <!-- 学习路径 -->
        <div id="learning-path-view" class="module-block">
          <div class="module-header">
            <img src="./assets/Learningpath.png" alt="Icon" class="icon" />
            LEARNING PATH
          </div>
          <div class="module-component">
            <learningPath />
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
import filePreview from './components/FilePreview.vue'
import chat from './components/Chat.vue'
import mindmap from './components/Mindmap.vue'
import noteEditor from './components/NoteEditor.vue'
import learningPath from './components/LearningPath.vue'
import questionRmd from './components/QuestionRmd.vue'

import DataService from "./utils/data-service"

export default {
  name: 'forethought',
  components: {
    filePreview,
    chat,
    mindmap,
    noteEditor,
    learningPath,
    questionRmd
  },
  data() {
    return {
      getFileStatus: false,
      wordCloudData: null,
      fileStructureData: null,
      fileData: null,
      fileSummary: '',
      cardData: [],
      mindMapData:[],
      nodeToQuestionRmd: '',

    }
  },
  mounted() {

  },
  methods: {
    // 后端获取文件
    onGetFileData(filedata) {
      this.fileData = filedata[0]
      this.fileStructureData = filedata[1]
      this.fileSummary = filedata[2]
      this.mindMapData=filedata[3]

      // 获取wordcard数据
      var childrenContents = []
      filedata[1].forEach(item => {
        childrenContents.push({
              "key": item.key,
              "title": item.title,
              "content": item.content
            });
        if (item.children && item.children.length > 0) {
          item.children.forEach(child => {
            childrenContents.push({
              "key": child.key,
              "title": child.title,
              "content": child.content
            });
          });
        }
      })
      this.cardData=childrenContents
      console.log(this.cardData)
    },


    onGetFileContent(file) {
      var formData = new FormData()
      formData.append('file', file)
      DataService.constructor()
      DataService.getFileContent(formData, (backendData) => {
        console.log('backendData:', backendData);
        this.getFileStatus = true;
      })
    },

    // 对选中节点进行问题推荐
    onGetQuestionRmd(nodeId) {
      this.nodeToQuestionRmd = nodeId
    },

    // 处理提交的笔记，生成词云
    onGenerateWordCloud(node, noteContext) {
      DataService.getWordCloudData(node, noteContext, (wordCloudData) => {
        //this.wordCloudData.nodeId=node.id()
        //this.wordCloudData.node = node
        //this.wordCloudData.data = wordCloudData
        this.wordCloudData = {
          'nodeId': node.id(),
          'node': node,
          'data': wordCloudData
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
}

#column-2 {
  flex: 2.5;
  height: 100%;
  width:100%;
}

#column-3 {
  flex: 4;
  height: 100%;
  width:100%;
}


#file-preview-view {
  flex: 7;
  /* max-height: 700px; */
}


#knowledge-mindmap-view {
  flex: 7;
  /* max-height: 700px; */
}

#learning-path-view {
  flex: 4;
}

#question-recommendation-view {
  flex: 4;
}

#chat-view {
  flex: 1;
}
</style>
