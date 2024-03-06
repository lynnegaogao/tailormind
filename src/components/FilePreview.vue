<template>
    <div class="container">
        <div class="left-column">
            <!-- 1文件预览 -->
            <div class="pdf-preview sub-module-block">
                <!-- 隐藏状态栏 -->
                <iframe v-if="pdfUrl" :src="pdfUrl + '#toolbar=0'" frameborder="0" class="pdf"></iframe>
            </div>
        </div>
        <div class="right-column">
            <!-- 2-1文件目录 -->
            <div class="file-struct sub-module-block">
                <a-tree v-model:expandedKeys="expandedKeys" :tree-data="fileStructureData" :show-line="true"
                    style="font-size: medium; margin: 10px 0px 0 20px" @select=scrollToCard class="file-struct-tree">
                    <template #title="{ key: key, title }">
                        <a-dropdown :trigger="['contextmenu']">
                            <span>{{ title }}</span>
                        </a-dropdown>
                    </template>
                </a-tree>
                <!-- <fileStruct @selectNode="scrollToCard" :fileStructureData='fileStructureData' /> -->
            </div>
            <!-- 2-2知识卡片 -->
            <div class="knowledge-card sub-module-block">
                <a-tree ref="cardList" :tree-data="cardData" :show-icon="false" :height="500"
                    style="font-size: medium;">

                    <template #title="{ key: key, title, content }">
                        <a-dropdown :trigger="['contextmenu']">
                            <a-card size="small" :key="key" :title="key + ' ' + title"
                                :style="{ border: selectedKey == key ? '2px solid rgb(199,151,48)' : '' }" class="card">
                                <div class="card-content">
                                    <p>{{ content }}</p>
                                </div>
                            </a-card>
                            <!-- <div>hh</div> -->
                            <template #overlay>
                                <a-menu>
                                    <a-menu-item key="1" @Click="copyCard(title, content)">Copy</a-menu-item>
                                    <a-menu-item key="2" @Click="askAI(title, content)">Ask Tailor-Mind
                                        Tutor</a-menu-item>
                                </a-menu>
                            </template>
                        </a-dropdown>
                    </template>
                </a-tree>
            </div>
        </div>
    </div>
</template>

<script>
import pdfUrl from '/src/assets/cs229-notes12.pdf';
import { Button, Card, Tree, Dropdown, Menu, message } from 'ant-design-vue';

export default {
    name: 'filePreview',
    components: {
        // from ant-design-vue
        AButton: Button,
        ACard: Card,
        ADropdown: Dropdown,
        ATree: Tree,
        AMenu: Menu,
        AMenuItem: Menu.Item
    },
    data() {
        return {
            pdfUrl: null,
            fileStructureData: [],
            cardData: [],
            expandedKeys: ['1'],
            selectedKey: '',
        }
    },
    mounted() {
    },
    props: {
        fileStructureData: {
            type: Array,
            default: function () { return []; },
        },
        fileData: {
            type: Array,
            default: function () { return []; },
        },
        cardData: {
            type: Array,
            default: function () { return []; },
        },
        pdfUrl: {
            type: String,
            default: function () { return ''; },
        },
    },
    watch: {
        // 用于展示文件结构
        fileStructureData(newValue, oldValue) {
            console.log(newValue, oldValue)
            this.$nextTick(() => {
                this.fileStructureData = newValue;
            })
        },
        // 用于展示单词卡
        cardData(newValue, oldValue) {
            console.log(newValue, oldValue)
            this.$nextTick(() => {
                this.cardData = newValue;
            })
        },
        // 用于展示Pdf
        fileData(newValue, oldValue) {

            console.log('pdfdata:', newValue[0].filename)
            this.$nextTick(() => {
                // if (filename.endsWith('.pdf')) {
                // let pdfData = `data:application/pdf;base64,${newValue[0]}`;
                // console.log(pdfData)
                this.pdfUrl = `../../back/uploads/${newValue[0].filename}`; // pdfUrl是绑定到<iframe> src属性的数据属性
                // }
            })
        }
    },
    methods: {
        // 点击文件目录树节点，滚动到对应的知识卡片
        scrollToCard(selectedKeys, e) {
            console.log('selectedKeys', selectedKeys);
            if (selectedKeys.length > 0) {
                // 获取选中的 key
                const key = selectedKeys[0];
                this.selectedKey = key;
                // 调用 antd-vue 的 scrollTo 方法来滚动到指定 key 的节点位置
                this.$refs.cardList.scrollTo({ key: key, align: 'top' });
            }
        },
        // 复制卡片的内容
        copyCard(title, content) {
            const textToCopy = `${title}\n${content}`; // 将标题和内容组合成需要复制的文本
            navigator.clipboard.writeText(textToCopy) // 使用浏览器的Clipboard API将文本复制到剪贴板
                .then(() => {
                    message.success('Card copied successfully!');
                })
                .catch(err => {
                    message.error('Error copying card:', err);
                });
        },
        // 调用AI接口
        askAI(title, content) {
            message
                .loading('Asking AI Tutor, waiting...', 2.5)
                .then(
                    () => message.success('Loading finished', 2.5),
                    // eslint-disable-next-line @typescript-eslint/no-empty-function
                    () => { },
                )
                .then(() => message.info('Successfully asked', 2.5));
            //TODO
        }

    },

}
</script>

<style>
/* file-preview */
.container {
    display: flex;
    flex-direction: row;
    width: 100%;
    height: 100%;
}

.left-column {
    flex: 2.5;
    margin: 2px;
    max-height: 720px;
    border-right: 5px solid #eee;
}

.right-column {
    flex: 3;
    max-height: 720px;
}

.pdf-preview {
    height: 100%;
}

.pdf {
    width: 100%;
    height: 100%;
}

.file-struct {
    height: 40%;
    overflow-y: auto;
    border-bottom: 5px solid #eee;
}

.knowledge-card {
    height: 60%;
    /* margin-left: -10px; */
    overflow: hidden;
    /* overflow-y: auto; */
}

.card {
    margin: 10px;
    padding: 10px;

}
</style>
