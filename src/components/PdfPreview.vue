<template>
  <div class="pdf-viewer">
    <!-- 隐藏状态栏 -->
    <iframe :src="pdfPath+'#toolbar=0'" frameborder="0" class="pdf"></iframe>
  </div>
</template>

<script>
import pdfPath from '/src/assets/cs229-notes12.pdf';
export default {
  name: 'PdfPreview',
  components: {
  },
  data () {
    return {
      pdfPath
    };
  },
  methods: {
    closepdf () {
      this.isshowpdf = false
    },
    pdferr (errurl) {
      console.log(errurl)
    },
    openpdf () {
      this.isshowpdf = true
    }
  }
}
</script>

<style>
.pdf-viewer {
  height: 100%; /* 设置 PDF 预览容器的固定高度 */
  /* overflow-y: auto; 启用垂直滚动 */
}

.pdf{
  width: 100%;
  height: 100%;
}
</style>
