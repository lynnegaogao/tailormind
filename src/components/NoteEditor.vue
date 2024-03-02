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
    watch: {

    },
    mounted() {
        this.initializeQuill()
        this.$nextTick(() => {
            this.setQuillEditorBackgroundTransparent();
        });
    },

    methods: {
        initializeQuill() {
            this.quill = new Quill(this.$refs.quillEditor, {
                theme: 'snow' // 选择主题
            })
            document.addEventListener('keydown', this.handleKeydown);

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
