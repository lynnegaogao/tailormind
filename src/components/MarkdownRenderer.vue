<template>
    <div v-html="renderedMarkdown" class="markdown-container"></div>
</template>

<script>
import { marked } from 'marked';
import DataService from "../utils/data-service"

export default {
    name: 'MarkdownRenderer',
    data() {
        return { source_text: "" };
    },
    computed: {
        renderedMarkdown() {
            DataService.getCustomizedNote((note) => this.source_text = note);
            return marked(this.source_text);
        },
    },
};
</script>

<style>
.markdown-container{
    width: 100%;
    height: 100%;
    max-height: 720px;
}

</style>