<template>
  <div class="upload-file">
    <a-upload action="http://localhost:8000/upload" v-model:file-list="fileList" :custom-request="handleUpload">
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
  data() {
    return {
      fileList: [],
    };
  },
  methods: {
    handleUpload(options) {
      console.log(options)
      const { onSuccess, onError, file } = options;
      const formData = new FormData();
      formData.append('file', file); // 添加这一行
      console.log(file)
      axios.post('http://localhost:8000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
        .then(response => {
          // 调用 onSuccess 来告知上传成功  
          onSuccess(response.data, file);
        })
        .catch(error => {
          // 调用 onError 来告知上传失败
          onError(error);
          console.log(error)
        });
    },

  }
};
</script>

<style scoped>


</style>