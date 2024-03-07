<template>
    <div class="sidebar" ref="sidebar">
        <div ref="quillEditor"></div>
    </div>
</template>

<script>
import Quill from 'quill';
import 'quill/dist/quill.snow.css';

export default {
    components: {
    },
    setup() {

    },
    data() {
        return {
            quill: null, // 用于存储Quill实例
        };
    },
    props: {
    },
    watch: {
        
    },
    mounted() {
        this.initializeQuill()
        this.$nextTick(() => {
            this.setQuillEditorBackgroundTransparent();
        });
    },
    emits: ['generateWordCloud'],
    methods: {
        initializeQuill() {
            this.quill = new Quill(this.$refs.quillEditor, {
                theme: 'snow' // 选择主题
            })
            // 构造与节点相关的预设文本

            var presetText = `Record some of what you've learned ~`


            // 首先清空编辑器内容
            this.quill.setText('');
            // 设置预设文本
            this.quill.setText(presetText);
            // 生成词云
            // document.addEventListener('keydown', (event) => {
            //     if (event.key == 'Escape') {
            //         // 获取编辑器内容
            //         var editorContent = this.quill.root.innerHTML;
            //         if (editorContent != '' && this.editNode) {
            //             this.$emit('generateWordCloud', this.editNode, editorContent)
            //         }
            //     }
            // }, { once: true });

        },
        setQuillEditorBackgroundTransparent() {
            const editor = this.$refs.quillEditor.querySelector('.ql-editor');
            if (editor) {
                editor.style.backgroundColor = 'transparent';
            }

        },
    }
};
</script>

<style>
.sidebar {
    overflow-x: hidden;
}

.quillEditor {
    overflow-y: auto;
}


.ql-container {
    background-color: rgba(255, 255, 255, 0.763);

}

.ql-toolbar {
    background-color: rgba(255, 255, 255, 0.763);
}
</style>
