<template>
  <div id="container">
    <div class="system-header">
      Tailor-Mind
      <div class="system-introduction"> Advancing Your Self-Regulated Learning Journey </div>
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
            <chat @getFileData="onGetFileData" :nodeToQuestionRmd="nodeToQuestionRmd" :getFileStatus="getFileStatus"
              @changeMindmapToDefault="onChangeMindmapToDefault" @submitChatHistory="onSubmitChatHistory"
              :isReflection="isReflection" :testingQuestionList="testingQuestionList"
              :learningPathData="learningPathData" @changePathContrast="onChangePathContrast"
              @getAdjustedLearningPathData="onGetAdjustedLearningPathData" :knowledgeCard="knowledgeCard"
              @startDriver="onStartDriver" @addNewRelationToMindmap="onAddNewRelationToMindmap" />
          </div>
        </div>
      </div>


      <div id="column-2" class="column">

        <!-- 文件预览+知识点思维导图 -->
        <div id="row-1" class="row">
          <!-- 文件预览 -->
          <div id="file-preview-view" class="module-block" style="position: relative;">
            <div class="module-header" v-if="!isReflection">
              <img src="./assets/Documents.png" alt="Icon" class="icon" />
              FILE PREVIEW
              <Switch :checked="isReflectionShow" @change="toggleView"
                style="float: right; position: absolute; top:8px;right:10px" size="small" />
            </div>
            <div class="module-header" v-else>
              <img src="./assets/Note.png" alt="Icon" class="icon" />
              NOTES
              <Switch id="file-preview-view" :checked="isReflectionShow" @change="toggleView"
                style="float: right; position: absolute; top:8px;right:10px" size="small" />
            </div>
            <div class="module-component">
              <filePreview v-if="!isReflectionShow" :fileStructureData="fileStructureData" :fileData="fileData"
                :pdfUrl="pdfUrl" :cardData="cardData" @askKnowledgeCard="onAskKnowledgeCard" />
              <markdownRenderer v-else style="padding:10px" :markdownData="markdownData" />
            </div>
          </div>

          <!-- 知识点思维导图 -->
          <div id="knowledge-mindmap-view" class="module-block">
            <div class="module-header">
              <img src="./assets/Mindmap.png" alt="Icon" class="icon" />
              KNOWLEDGE MINDMAP
            </div>
            <div class="module-component">
              <mindmap style="flex: 4;" :mindMapData='mindMapData' @generateWordCloud='onGenerateWordCloud'
                :wordCloudData='wordCloudData' :submitNode='submitNode' @getQuestionRmd='onGetQuestionRmd'
                :rmdMindmapOrNot='rmdMindmapOrNot' @getLearningPathDataByUser='onGetLearningPathDataByUser'
                :newRelationShip="newRelationShip" />
              <noteEditor style="flex: 2;" />
            </div>
          </div>
        </div>

        <!-- 问题推荐+学习路径 -->
        <div id="row-2" class="row">
          <template v-if="!isPathContrast">
            <!-- 问题推荐 -->
            <div id="question-recommendation-view" class="module-block">
              <div class="module-header">
                <img src="./assets/Recommendation.png" alt="Icon" class="icon" />
                QUESTION RECOMMENDATION
              </div>
              <div class="module-component">
                <questionRmd :questionRmdData="questionRmdData" />
              </div>
            </div>

            <!-- 学习路径 -->
            <div id="learning-path-view" class="module-block">
              <div class="module-header">
                <img src="./assets/Learningpath.png" alt="Icon" class="icon" />
                LEARNING PATH
              </div>
              <div class="module-component">
                <learningPath :learningPathData="learningPathData" :rmdMindmapOrNot="rmdMindmapOrNot"
                  @resetLearningPathData="onResetLearningPathData" :isPathContrast="isPathContrast" />
              </div>
            </div>
          </template>

          <template v-else>
            <!-- 第一个学习路径组件，flex为1 -->
            <div id="learning-path-before" class="module-block" style="flex: 1;">
              <div class="module-header">
                <img src="./assets/Learningpath.png" alt="Icon" class="icon" />
                LEARNING PATH -- BEFORE
              </div>
              <div class="module-component">
                <learningPath :learningPathData="learningPathData" :rmdMindmapOrNot="rmdMindmapOrNot"
                  @resetLearningPathData="onResetLearningPathData" :isPathContrast="isPathContrast" />
              </div>
            </div>

            <div id="learning-path-after" class="module-block" style="flex: 1;">
              <div class="module-header">
                <img src="./assets/Learningpath.png" alt="Icon" class="icon" />
                LEARNING PATH -- AFTER
              </div>
              <div class="module-component">
                <learningPathAfter :learningPathData_After="learningPathData_After" :rmdMindmapOrNot="rmdMindmapOrNot"
                  @resetLearningPathData="onResetLearningPathData" :isPathContrast="isPathContrast" />
              </div>
            </div>

          </template>

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
import learningPathAfter from './components/LearningPathAfter.vue'
import DataService from "./utils/data-service"

import { driver } from "driver.js";
import "driver.js/dist/driver.css";
import { Switch } from 'ant-design-vue'
export default {
  name: 'forethought',
  components: {
    filePreview,
    chat,
    mindmap,
    noteEditor,
    learningPath,
    learningPathAfter,
    questionRmd,
    markdownRenderer,
    Switch,
  },
  data() {
    return {
      pdfUrl: '',
      getFileStatus: false,
      wordCloudData: null,
      fileStructureData: [],
      fileData: null,
      fileSummary: '',
      cardData: [],
      mindMapData: [],
      nodeToQuestionRmd: '',
      rmdMindmapOrNot: true,
      questionRmdData: [],
      learningPathData: [],
      learningPathData_After: [],
      submitChatData: [],
      isReflection: false,
      isReflectionShow: false,
      markdownData: "",
      testingQuestionList: [],
      isPathContrast: false,
      knowledgeCard: '',
      newRelationShip: [],
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
      this.mindMapData = filedata[3]
      this.questionRmdData = filedata[4]
      this.learningPathData = filedata[5]
      this.pdfUrl = `../../back/uploads/${filedata[0][0].filename}`
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
      this.cardData = childrenContents
      this.getFileStatus = true
      // console.log(this.getFileStatus)
      // console.log(this.cardData)
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

    // 用户重新定义mindmap数据为default
    onChangeMindmapToDefault() {
      var recommendedMindmapData = this.mindMapData
      recommendedMindmapData.nodes.forEach(node => {
        node.level = 0;
        node.size = 3;
      });
      this.rmdMindmapOrNot = false
      this.mindMapData = recommendedMindmapData
    },

    // 用户重新定义learning path + mindmap数据为default
    onResetLearningPathData(data) {
      this.learningPathData = data
      this.onChangeMindmapToDefault()
    },

    // 获取用户重新定义的learning path数据
    onGetLearningPathDataByUser(data) {
      this.learningPathData = data
      console.log(this.learningPathData)
    },

    // 进入reflection之前对聊天数据进行保存
    onSubmitChatHistory(data) {
      this.submitChatData = data
      this.$store.dispatch('submitChatData', this.submitChatData);
      this.$store.dispatch('learningPathData', this.learningPathData);
      this.$store.dispatch('mindMapData', this.mindMapData);
      this.isReflection = true
      this.isReflectionShow = true

      DataService.getCustomizedNote(data, (markdownData) => {
        this.markdownData = markdownData[0]
        console.log("Markdown数据：", markdownData[0])
      })

      // // 创建一个Blob对象，并保存聊天记录
      // const blob = new Blob([JSON.stringify(this.submitChatData, null, 2)], { type: 'application/json' });
      // // 创建一个指向该Blob的URL
      // const url = URL.createObjectURL(blob);
      // // 创建一个临时的a标签用于下载
      // const link = document.createElement('a');
      // link.href = url;
      // link.download = 'chat-history.json';
      // // 模拟点击该链接实现下载
      // document.body.appendChild(link); // 将链接添加到文档中
      // link.click(); // 触发下载
      // // 清理：移除链接并释放创建的blob URL
      // document.body.removeChild(link);
      // URL.revokeObjectURL(url);
    },

    // 切换file-preview & notes
    toggleView(checked) {
      this.isReflectionShow = checked;
      this.isReflection = checked

    },

    // 切换learning path contrast
    onChangePathContrast() {
      this.isPathContrast = true
    },

    // 获取修改之后的learning path
    onGetAdjustedLearningPathData(data) {
      this.learningPathData_After = data
    },

    // file preview-从card提问
    onAskKnowledgeCard(data) {
      this.knowledgeCard = data
    },

    // 获取从answer中提取的relation，添加到mindmap view中
    onAddNewRelationToMindmap(data) {
      let inputString = data.replace(/\[|\]/g, '').trim();
      let itemList = inputString.split(',').map(item => item.trim());

      let [term1, relation, term2] = itemList;
      let newNode1 = {
        group: 'nodes',
        data: { id: term1 + '-1', label: term1 },
        style: {
          'width': 15,
          'height': 15,
          'content': term1,
          'background-color': "#eee1c7"
        }
      };
      let newNode2 = {
        group: 'nodes',
        data: { id: term2 + '-2', label: term2 },
        style: {
          'width': 15,
          'height': 15,
          'content': term2,
          'background-color': "#eee1c7"
        }
      };
      let newEdge = {
        group: 'edges',
        data: {
          id: 'edge' + Math.random(),
          source: term1 + '-1',
          target: term2 + '-2',
          relation: relation
        }
      };
      this.newRelationShip = [newNode1, newNode2, newEdge]

    },

    // 定义引导的步骤
    onStartDriver() {
      const driverInstance = driver({
        showProgress: true,
        showButtons: [
          'next',
          'previous',
        ],
        steps: [
          {
            element: '#chat-view',
            popover: {
              title: 'Chat View',
              description: "You can ask any questions here with your customed tutor TAILOR-MIND💡. She will guide you through the process of Self-Regulated Learning🎢, so start chatting with her without any reservations!",
              position: 'bottom'
            }
          },
          {
            element: '#file-preview-view',
            popover: {
              title: 'File Preview',
              description: 'Here you will find the presentation and overviews of your uploaded learning material📚, and you can also ask Tailor-Mind about the Knowledge Cards!',
              position: 'bottom'
            }
          },
          {
            element: '#knowledge-mindmap-view',
            popover: {
              title: 'Knowledge Mindmap',
              description: "Here we will show you the knowledge structure and you can interact with the Mindmap. And don't forget to record your learning on the right side✍🏻!",
              position: 'bottom'
            }
          },
          {
            element: '#question-recommendation-view',
            popover: {
              title: 'Question Recommendation',
              description: "If you're not sure how to get started, or aren't inspired to ask questions❔🤔, you can come here for some recommendations!",
              position: 'bottom'
            }
          },
          {
            element: '#learning-path-view',
            popover: {
              title: 'Learning Path',
              description: 'Also, Tailor-Mind tutor will customise your learning path for you. We hope you can work hard to complete each milestone🤩!',
              position: 'bottom'
            }
          }
        ]
      });

      driverInstance.drive();

    },


  },

}
</script>

<style>
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
  /* flex-grow: 1; */
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

}

#column-2 {
  flex: 6.5;
  height: 100%;
  width: 100%;
  display: flex;
  flex-direction: column;
}

#column-3 {
  flex: 4;
  height: 100%;
  width: 100%;
}

#row-1 {
  flex: 7;
  display: flex;
  height: 100%;
  width: 100%;
  flex-direction: row;
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.2);
  background-color: #fff;
  margin-bottom: 5px;
  margin-right: 3px;
  max-height: 760px;

}

#row-2 {
  flex: 4;
  display: flex;
  height: 100%;
  width: 100%;
  flex-direction: row;
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.03);
  background-color: #fff;
  margin-bottom: 5px;
  margin-right: 3px;
}


#file-preview-view {
  flex: 4;
}


#knowledge-mindmap-view {
  flex: 6.5;
}

#learning-path-view {
  flex: 6.5;
}

#question-recommendation-view {
  flex: 4;
}

#chat-view {
  flex: 1;
}

#learning-path-before {
  flex: 1;
}

#learning-path-after {
  flex: 1;
}
</style>
