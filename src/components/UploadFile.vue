<template>
  <div class="upload-file">
    <a-upload v-model:file-list="fileList" :custom-request="handleUpload">
      <a-button>
        <upload-outlined />
        Upload Your Learning Material~
      </a-button>
    </a-upload>
  </div>
</template>

<script>
import axios from 'axios';
import { UploadOutlined } from '@ant-design/icons-vue';
import { Upload, Button } from 'ant-design-vue';

export default {
  components: {
    UploadOutlined,
    'a-upload': Upload,
    'a-button': Button
  },
  props: {
    //formData: {
    //  type: FormData,
    //  required: true
    //}
  },
  data() {
    return {
      fileList: [],
    };
  },
  emits: ["getFileContent"],
  methods: {
    handleUpload(options) {
      const { onSuccess, onError, file } = options;
      console.log("front gets file!",file)
      this.$emit('getFileContent', file)
      onSuccess(file);
    },

  },
}
</script>

<style scoped>
.upload-file {
  margin-top: 15px;
}
</style>