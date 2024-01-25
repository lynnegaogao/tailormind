<script setup>
import uploadFile from './components/UploadFile.vue'
</script>

<template>
  <div id="container">

    <div class="system-header">
      Tailor-Mind
    </div>

    <div class="system-component">
      <!-- 文件上传+文件预览+知识架构+知识点思维导图 -->
      <div id="column-1" class="column">
        <!-- 文件上传 -->
        <div id="upload-file-view" class="module-block">
          <div class="module-header">
            <img src="./assets/Upload.png" alt="Icon" class="icon" />
            UPLOAD FILE
          </div>
          <div class="module-component">
            <uploadFile />
          </div>
        </div>

        <!-- 文件预览 -->
        <div id="file-preview-view" class="module-block">
          <div class="module-header">
            <img src="./assets/Documents.png" alt="Icon" class="icon" />
            FILE PREVIEW
          </div>
          <div class="module-component">

          </div>
        </div>

        <!-- 知识架构 -->
        <div id="file-structure-view" class="module-block">
          <div class="module-header">
            <img src="./assets/Structure.png" alt="Icon" class="icon" />
            FILE STRUCTURE
          </div>
          <div class="module-component">

          </div>
        </div>

        <!-- 知识点思维导图 -->
        <div id="knowledge-mindmap-view" class="module-block">
          <div class="module-header">
            <img src="./assets/Mindmap.png" alt="Icon" class="icon" />
            KNOWLEDGE MINDMAP
          </div>
          <div class="module-component">

          </div>
        </div>

      </div>

      <!-- 对话+问题推荐 -->
      <div id="column-2" class="column">
        <!-- 对话 -->
        <div id="chat-view" class="module-block">
          <div class="module-header">
            <img src="./assets/Chats.png" alt="Icon" class="icon" />
            CHAT
          </div>
          <div class="module-component">

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

      <!-- 编辑笔记+自测+反馈 -->
      <div id="column-3" class="column">
        <!-- 编辑笔记 -->
        <div id="edit-notes-view" class="module-block">
          <div class="module-header">
            <img src="./assets/Note.png" alt="Icon" class="icon" />
            EDIT NOTES
          </div>
          <div class="module-component">

          </div>
        </div>

        <!-- 自测 -->
        <div id="self-examination-view" class="module-block">
          <div class="module-header">
            <img src="./assets/Exam.png" alt="Icon" class="icon" />
            SELF EXAMINATION
          </div>
          <div class="module-component">

          </div>
        </div>

        <!-- 反馈 -->
        <div id="feedback-view" class="module-block">
          <div class="module-header">
            <img src="./assets/Feedback.png" alt="Icon" class="icon" />
            FEEDBACK
          </div>
          <div class="module-component">

          </div>
        </div>

      </div>

    </div>


  </div>
</template>


<style scoped>
#container {
  display: flex;
  flex-direction: column;
  width: 100vw;
  height: 100vh;
}

.system-header{
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 5px;
  margin-bottom: 5px;
  background-color: #eee1c7; 
  color: #7e7d7f; 
  text-align: center; 
  font-weight: bold;
  font-size: 1.2em;
  padding: 5px;
  flex-grow: 1;
}

.system-component{
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
  margin-bottom: 20px;
  font-weight: bold;
  display: flex;
  justify-content: flex-start;
  /* 使所有元素居左 */
  border-bottom: 1.5px solid #eee;
  /* 添加分界线 */
  width: 100%;

}

.module-block {
  display: flex;
  /* justify-content: center; */
  /* align-items: center; */
  min-height: 50px;
  border-radius: 10px;
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.2);
  background-color: #fff;
  margin-bottom: 5px;
  margin-right: 3px;
  background: #fff;
  flex-direction: column;
}

.icon {
  width: 25px;
  height: 25px;
  margin-left: 10px;
  margin-right: 10px;
}

#column-1{
  flex:1;
  height:100%;
}

#column-2{
  flex:2;
  height:100%;
}

#column-3{
  flex:1;
  height:100%;
}

#upload-file-view{
  flex:1;
}
#file-preview-view{
  flex:1; 
}
#file-structure-view{
  flex:1; 
}
#knowledge-mindmap-view{
  flex:1; 
}

#chat-view{
  flex:2; 
}
#question-recommendation-view{
  flex:1;
}

#edit-notes-view{
  flex:3;
}
#self-examination-view{
  flex:2;
}
#feedback-view{
  flex:1;
}

</style>





