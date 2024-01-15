<script setup>
import { ref } from 'vue'

defineProps({
  msg: String,
})

const count = ref(0)
const selectedFile = ref(null) // 用于存储选中的文件

// 处理文件选取
const handleFileChange = (event) => {
  selectedFile.value = event.target.files[0]
}

// 处理文件上传（示例，需要根据实际情况调整）
const uploadFile = () => {
  if (!selectedFile.value) {
    alert('请选择一个文件上传')
    return
  }

  // 这里添加实际的文件上传逻辑
  console.log('上传文件:', selectedFile.value.name)
  // 清空文件选择
  selectedFile.value = null
}
</script>

<template>
  <h1>{{ msg }}</h1>

  <div class="uploadfile">
    <!-- 文件上传组件 -->
    <div>
      <input type="file" @change="handleFileChange">
      <button @click="uploadFile">上传文件</button>
    </div>
  </div>

</template>

<style scoped>
.uploadfile {
  margin-top: 20px;
  padding: 10px;
  /* border: 1px solid #ddd;
  border-radius: 5px; */
  text-align: center;
  display: flex;
  justify-content: center; /* 使元素水平居中 */
  gap: 10px; /* 在元素之间创建间隙 */
}

.uploadfile input[type="file"] {
  padding: 10px 15px;
  border: 1px solid #ccc;
  border-radius: 4px;
  cursor: pointer;
  background-color: #f4f4f4;
  transition: background-color 0.3s ease;
  outline: none;
}

.uploadfile button {
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  background-color: #123;
  color: white;
  transition: background-color 0.3s ease;
  margin-left: 20px; /* 在上传按钮前添加空隙 */
}

.uploadfile button:hover {
  background-color: #ccc;
}

.uploadfile input[type="file"]:hover {
  background-color: #e9e9e9;
}
</style>
