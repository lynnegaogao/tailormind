<template>
  <div id="question-rmd-container">
    <a-collapse v-model:activeKey="activeKey" class="collapse">
      <a-collapse-panel v-for="(item, index) in items" :key="item.key" :header="item.knowledgepoint"
        class="collapse-item">
        <div v-for="(question, qIndex) in item.questions" :key="qIndex">
          <div class="tag-button-container">
            <Tag :color="levelcolor[question.level - 1]" style="font-size: 14px;">
              {{ `L${question.level} : ${learningLevelExpl[question.level - 1]}` }}
            </Tag>

            <a-button-group>
              <a-button class="button" @click="copyToClipboard(question.question)">
                <CopyOutlined />Copy
              </a-button>
              <a-button class="button">
                <ReloadOutlined />Reload
              </a-button>
            </a-button-group>
          </div>
          <p>{{ question.question }}</p>
          <a-divider v-if="qIndex !== item.questions.length - 1" class="divider-style" />
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

export default {
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

  },
  data() {
    return {
      activeKey: ['1'],
      items: [],
      levelcolor: [
        "#9B6072",
        "#CE8D68",
        "#CFAD6D",
        "#9CA767",
        "#527840",
        "#406868",
        "#4C5874",
        "#776B9F"],
      learningLevelExpl: [
        'Concept',
        'Principle / Math formula',
        'Application',
        'Implementation',
        'Significance / Influence',
        'Related Knowledge',
        'Contrast Knowledge',
        'Extended Knowledge'],
    }
  },
  props: {
    questionRmdData: {
      type: Object,
      default: function () { return {}; },
    },
  },
  watch: {
    'questionRmdData': {
      deep: true,
      handler(newValue, oldValue) {
        console.log(newValue, oldValue)
        this.$nextTick(() => {
          this.initializeItems();
        })
      }
    }
  },
  mounted() {
    // this.initializeItems();
  },
  methods: {
    initializeItems() {
      const questions = this.questionRmdData;

      const groupedQuestions = questions.reduce((result, question) => {
        const key = question.knowledgepoint;
        if (!result[key]) {
          result[key] = [];
        }
        result[key].push(question);
        return result;
      }, {});

      this.items = Object.keys(groupedQuestions).map((knowledgepoint, index) => ({
        key: (index + 1).toString(),
        knowledgepoint,
        questions: groupedQuestions[knowledgepoint],
      }));
    },

    async copyToClipboard(text) {
      try {
        await navigator.clipboard.writeText(text);
        message.success('Question copied successfully');
      } catch (err) {
        console.error('Failed to copy text: ', err);
      }
    },
  },
};


</script>

<style>
#question-rmd-container {
  width: 100%;
  height: 100%;
  overflow-y: auto;
}

.collapse {
  background: #f7f7f7;
  border: 1px solid #d9d9d9;
  border-radius: 4px;
  max-height: 400px;
  overflow-y: auto;
  width: 100%;
}

.tag-button-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 0;

}

p {
  font-size: 16px;
  margin: 0;
}

.divider-style {

  margin-top: 5px;
  margin-bottom: 5px;
}

.button {
  margin-left: 5px;
}

/* Remove the empty ruleset */
/* 默认样式，可根据需求设置 */
</style>
