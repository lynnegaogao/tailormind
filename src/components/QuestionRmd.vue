<template>
  <div id="question-rmd-container">
    <a-collapse v-model:activeKey="activeKey" class="collapse">
    <a-collapse-panel
      v-for="(item, index) in items"
      :key="item.key"
      :header="item.knowledgepoint"
      class="collapse-item"
    >
      <div v-for="(question, qIndex) in item.questions" :key="qIndex">
        <div class="tag-button-container">
        <Tag :color="levelcolor[question.level - 1]" style="font-size: 14px;">
          {{ `L${question.level} : ${learningLevelExpl[question.level - 1]}` }}
        </Tag>
        
        <a-button-group >
            <a-button class="button" @click="copyToClipboard(question.question); success()"><CopyOutlined />Copy</a-button>
            <a-button class="button"><ReloadOutlined />Reload</a-button> 
        </a-button-group> 
        </div>
        <p>{{ question.question }}</p>
        <a-divider v-if="qIndex !== item.questions.length - 1" class="divider-style"/>
      </div>
    </a-collapse-panel>
  </a-collapse>
  </div>
  
</template>

<script>
import { defineComponent, ref, watch } from 'vue';
import { Collapse } from 'ant-design-vue';
import { Divider } from 'ant-design-vue';
import { Tag } from 'ant-design-vue';
import { Button } from 'ant-design-vue';
import { CopyOutlined, ReloadOutlined } from '@ant-design/icons-vue';
import { message } from 'ant-design-vue';
import questionData from './QuestionData.json';

export default defineComponent({
  components: {
    'a-collapse': Collapse,
    'a-collapse-panel': Collapse.Panel,
    'a-divider': Divider,
    Tag,
    'a-button': Button,
    CopyOutlined,
    ReloadOutlined,
    message

  },
  setup() {
    const activeKey = ref(['1']);
    const levelcolor = [
      '#ff9f6d',
      '#d88c9a',
      '#a17fda',
      '#c3e6a1',
      '#4caead',
      '#82b461',
      '#fffb96',
      '#87ccff',
    ];
    const learningLevelExpl = [
      'Concept',
      'Principle / Math formula',
      'Application',
      'Implementation',
      'Significance / Influence',
      'Related Knowledge',
      'Contrast Knowledge',
      'Extended Knowledge',
    ];

    // 使用引入的 QuestionData.json 作為問題數據
    const questions = questionData.questions;
    const knowledgepoints = questionData.knowledgepoints;

    // 將問題按照 knowledgepoint 進行分組
    const groupedQuestions = questions.reduce((result, question) => {
      const key = question.knowledgepoint;
      if (!result[key]) {
        result[key] = [];
      }
      result[key].push(question);
      return result;
    }, {});
    

    // 為每個 knowledgepoint 創建一個折疊表單
    const items = Object.keys(groupedQuestions).map((knowledgepoint, index) => ({
      key: (index + 1).toString(),
      knowledgepoint,
      header: knowledgepoint,
      questions: groupedQuestions[knowledgepoint],

      
    }));


    const copyToClipboard = async (text) => {
      try {
        await navigator.clipboard.writeText(text);
        console.log('Text copied to clipboard');
      } catch (err) {
        console.error('Failed to copy text: ', err);
      }
    };

    const success = () => {
      message.success('Question copied successfully');
    };


    return {
      activeKey,
      items,
      groupedQuestions,
      levelcolor,
      learningLevelExpl,
      CopyOutlined,
      copyToClipboard,
      success
    };
  },
});


</script>

<style>
#question-rmd-container{
  width: 100%;
  height:100%;
  max-height: 100%;
  overflow-y: auto;
}
.collapse {
  background: #f7f7f7;
  border: 1px solid #d9d9d9;
  border-radius: 4px;
  max-height: 443px;
  overflow-y: auto;
  width: 100%;
}
.tag-button-container{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 0;

}
p{
  font-size: 16px;
  margin: 0;
}
.divider-style{

  margin-top: 5px;
  margin-bottom: 5px;
}
.button{
  margin-left: 5px;
}

/* Remove the empty ruleset */
/* 默认样式，可根据需求设置 */

</style>
