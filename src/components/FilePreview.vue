<template>
    <div class="container">
        <div class="left-column">
            <!-- 文件预览 -->
            <div class="pdf-preview">
                <pdfPreview />
                <div>文件预览</div>
            </div>
        </div>
        <div class="right-column">
            <!-- 文件目录 -->
            <div class="file-struct">
                <fileStruct />
            </div>
            <!-- 词云 -->
            <!-- <div class="word-cloud">
                <wordCloud />
            </div> -->
            <!-- 知识卡片 -->
            <div class="knowledge-card">
                <knowledgeCard />
            </div>
        </div>
    </div>
</template>

<script>
import pdfPreview from './PdfPreview.vue'
import fileStruct from './FileStruct.vue'
import knowledgeCard from './KnowledgeCard.vue'
import wordCloud from './WordCloud.vue'


export default {
    name: 'filePreview',
    components: {
        pdfPreview,
        fileStruct,
        wordCloud,
        knowledgeCard
    },
    data() {
        return {
            getFileStatus: false,
        }
    },
    mounted() {

    },
    methods: {
        // 后端获取文件

        // 处理提交的笔记，生成词云

    },

}
</script>

<style scoped>
/* file-preview */
.container {
  display: flex;
  width: 100%;
  height: 100%;
}
.right-column, .left-column {
  flex: 1;
  /* height: 100%; */
  overflow-y: auto;
}
.file-struct {
  max-height: 60%;
}
.word-cloud {
  height: 200px;
}

.pdf-preview {
  height: 100%; /* Set height for the PDF preview container */
  overflow-y: auto; /* Enable vertical scrolling if content exceeds container height */
}
</style>
