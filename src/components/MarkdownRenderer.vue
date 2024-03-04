<template>
    <div v-html="renderedMarkdown"></div>
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
/* Add styles for your markdown content if necessary */
</style>