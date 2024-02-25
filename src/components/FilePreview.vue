<template>
    <div>
        <vue-pdf :src="pdfPath" />
    </div>
</template>

<script>
import { pdf } from 'vue-pdf';

export default {
    components: {
        VuePdf: pdf,
    },
    data() {
        return {
            pdfPath: require('@/assets/cs229-notes12.pdf'), // Provide the path to your local PDF file
        };
    },
};
</script>
