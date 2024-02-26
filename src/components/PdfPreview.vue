<template>
  <!-- <div class="pdf-viewer" ref="pdfViewer"> -->
    <!-- PDF 预览容器 -->
    <!-- <canvas ref="pdfCanvas"></canvas> -->
  <!-- </div> -->
  <!-- <div class="container">
    <button @click="openpdf">打开pdf</button>
    <vueshowpdf @closepdf="closepdf"
                v-model="isshowpdf"
                :pdfurl="src"
                @pdferr="pdferr"
                :maxscale='4'
                :minscale='0.6'
                :scale='1.0'></vueshowpdf>
  </div> -->

  <div class="pdf-viewer">
    <!-- 隐藏状态栏 -->
    <iframe :src="pdfPath+'#toolbar=0'" frameborder="0" class="pdf"></iframe>
  </div>
</template>

<script>
// import pdfjsLib from 'pdfjs-dist'

// export default {
//   name: 'PdfPreview',
//   props: {
//     pdfUrl: "http://storage.xuetangx.com/public_assets/xuetangx/PDF/PlayerAPI_v1.0.6.pdf" // PDF 文件的 URL
//   },
//   mounted() {
//     // 获取 PDF 预览容器和 Canvas 元素
//     const pdfViewer = this.$refs.pdfViewer
//     const pdfCanvas = this.$refs.pdfCanvas

//     // 使用 pdf.js 加载 PDF 文件
//     pdfjsLib.getDocument(this.pdfUrl).promise.then(pdf => {
//       // 获取第一页
//       pdf.getPage(1).then(page => {
//         const viewport = page.getViewport({ scale: 1 })

//         // 设置 Canvas 尺寸
//         pdfCanvas.height = viewport.height
//         pdfCanvas.width = viewport.width

//         const context = pdfCanvas.getContext('2d')

//         // 渲染 PDF 页面到 Canvas 上
//         page.render({
//           canvasContext: context,
//           viewport: viewport
//         })
//       })
//     })
//   }
// }

// import vueshowpdf from 'vueshowpdf'
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

<style scoped>
.pdf-viewer {
  height: 100%; /* 设置 PDF 预览容器的固定高度 */
  overflow-y: auto; /* 启用垂直滚动 */
}

.pdf{
  width: 100%;
  height: 99%;
}
</style>
