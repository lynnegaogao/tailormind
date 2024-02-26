<template>
    <div class="container">
        <div class="left-column">
            <!-- 文件预览 -->
            <div class="pdf-preview sub-module-block">
                <pdfPreview />
            </div>
        </div>
        <div class="right-column">
            <!-- 文件目录 -->
            <div class="file-struct sub-module-block">
                <fileStruct @selectNode="scrollToCard" />
            </div>
            <!-- 词云 -->
            <!-- <div class="word-cloud">
                <wordCloud />
            </div> -->
            <!-- 知识卡片 -->
            <div class="knowledge-card sub-module-block">
                <knowledgeCard ref="cardListComponent" />
            </div>
        </div>
    </div>
</template>

<script>
import pdfPreview from './PdfPreview.vue'
import fileStruct from './FileStruct.vue'
import knowledgeCard from './KnowledgeCard.vue'
// import wordCloud from './WordCloud.vue'


export default {
    name: 'filePreview',
    components: {
        pdfPreview,
        fileStruct,
        // wordCloud,
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
        // 滑动到对应的卡片
        scrollToCard(selectedKey) {
            // 在这里根据选中的节点 key 值，调用解释卡片组件的方法来滚动到相应的位置
            this.$refs.cardListComponent.scrollTo(selectedKey);
        }

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

.left-column {
    flex: 3;
    min-width: 200px;
    overflow-y: auto;
    border-right: 2px solid #eee;
}

.right-column {
    flex: 2;
    height: 100%;
}

.pdf-preview {
    height: 100%;
    /* Set height for the PDF preview container */
    overflow-y: auto;
    /* Enable vertical scrolling if content exceeds container height */
}

.file-struct {
    height: 40%;
    max-height: 300px;
    overflow-y: auto;
    border-bottom: 3px solid #eee;
}

.knowledge-card {
    height: 60%;
    max-height: 500px;
    overflow: hidden;
}

.sub-module-block {}
</style>
