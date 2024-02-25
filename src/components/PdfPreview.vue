https://juejin.cn/post/6844904137155411975
<template>
	<div>
	<!-- <pdf  v-for="i in numPages" :key="i"  :src="url" :page="i"></pdf>
     -->
    <!-- <pdf src="http://storage.xuetangx.com/public_assets/xuetangx/PDF/PlayerAPI_v1.0.6.pdf" :page="1"></pdf> -->
	</div>
</template>

<script>
	// import pdf from 'vue-pdf'
	// export default {
	// 	components: {
	// 		pdf
	// 	},
	// 	data(){
	// 		 return{
	// 			    url: '',
	// 			    numPages:1,
	// 		 }
	// 	 },
	// 	mounted: function() {
	// 	//   this.getNumPages("http://storage.xuetangx.com/public_assets/xuetangx/PDF/PlayerAPI_v1.0.6.pdf")

	// 	},
	// 	methods: {
	// 		getNumPages(url) {
	// 			var loadingTask = pdf.createLoadingTask(url)
	// 			loadingTask.then(pdf => {
	// 				this.url = loadingTask
	// 				this.numPages = pdf.numPages
	// 			}).catch((err) => {
	// 				console.error('pdf加载失败')
	// 			})
	// 		},
	// 	}
	// }
</script>
