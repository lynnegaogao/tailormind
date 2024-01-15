<script setup>
import uploadFile from './components/UploadFile.vue'
</script>

<template>
  <div class="upload-file">
  <uploadFile msg="Welcome to Tailor-Mind!"/>
  </div>
</template>


<style scoped>
::deep .upload-file {
  position: absolute;
  top: 0;
  left: 0;
  margin: 0;
}
</style>





