<template>
    <div style="position: relative;">
        <div class="markdown-container" ref="markdownContainer">
            <!-- Markdown content here -->
        </div>
        <div id="download-btn">
            <a-config-provider :theme="{ token: { colorPrimary: '#4C5874' } }">
                <a-button @click="downloadMarkdown" style="height:25px;line-height: normal; vertical-align: middle;">
                    <DownloadOutlined />Download
                </a-button>
            </a-config-provider>
        </div>
    </div>
</template>

<script>
import { marked } from 'marked';
import { Button, ConfigProvider, theme, } from 'ant-design-vue';
import { DownloadOutlined } from "@ant-design/icons-vue";
export default {
    name: 'MarkdownRenderer',
    components: {
        DownloadOutlined,
        'a-button': Button,
        'a-config-provider': ConfigProvider,
    },
    setup() {
        // 修改ant-design默认配色
        const { token } = theme.useToken();
        return {
            token,
        };
    },
    props: {
        markdownData: {
            type: String,
            default: ''
        }
    },
    watch: {
        'markdownData': function (newValue, oldValue) {
            this.renderedMarkdown();
        }
    },
    mounted() {
        this.renderedMarkdown();
    },
    methods: {
        renderedMarkdown() {
            this.$refs.markdownContainer.innerHTML = marked(this.markdownData);
        },
        downloadMarkdown() {
            const blob = new Blob([this.markdownData], { type: 'text/markdown;charset=utf-8' });
            const downloadUrl = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = downloadUrl;
            a.download = 'downloaded-file.md'; // 你可以自定义下载的文件名
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(downloadUrl);
        }
    },
};
</script>

<style>
.markdown-container {
    width: 100%;
    height: 100%;
    max-height: 700px;
    max-width: 620px;
    overflow-y: auto;
}

#download-btn {
    position: absolute;
    top: 10px;
    right: 50px;
    z-index: 10;
    /* 确保按钮总是在最上层 */
}
</style>
