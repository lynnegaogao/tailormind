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
                <a-tree v-model:expandedKeys="expandedKeys" :tree-data="fileStructData" :show-line="true"
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
                <a-tree ref="cardList" :tree-data="cardData" :show-icon="false" :height="500" style="font-size: medium;">
                    <template #title="{ key: key, title, content }">
                        <a-dropdown :trigger="['contextmenu']">
                            <a-card size="small" :key="key" :title="key + title"
                                :style="{ border: selectedKey == key ? '2px solid rgb(199,151,48)' : '' }" class="card">
                                <div class="card-content">
                                    <p>{{ content }}</p>
                                </div>
                            </a-card>
                            <!-- <div>hh</div> -->
                            <template #overlay>
                                <a-menu>
                                    <a-menu-item key="1" @Click="copyCard(title, content)">Copy</a-menu-item>
                                    <a-menu-item key="2" @Click="askAI(title, content)">Ask AI</a-menu-item>
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
            // pdfUrl: '',
            // fileStructData: [],
            fileStructData: [
                {
                    "key": "1",
                    "title": "凸集",
                    "children": [
                        { "key": "1-1", "title": "凸集定义" },
                        { "key": "1-2", "title": "凸集的例子" },
                    ]
                },
                {
                    "key": "2",
                    "title": "凸函数",
                    "children": [
                        { "key": "2-1", "title": "凸性的一阶条件" },
                        { "key": "2-2", "title": "凸性的二阶条件" },
                        { "key": "2-3", "title": "Jensen不等式" },
                        { "key": "2-4", "title": "子级集" },
                        { "key": "2-5", "title": "凸函数的应用" },
                    ]
                },
                {
                    "key": "3",
                    "title": "凸优化问题",
                    "children": [
                        { "key": "3-1", "title": "凸优化定义" },
                        { "key": "3-2", "title": "凸问题的全局优化" },
                        { "key": "3-3", "title": "凸优化问题的例子" }
                    ]
                }
            ],
            // cardData: [],
            cardData: [
                { "key": "1", "title": "凸集", "content": "凸集是指集合中的任意两点之间的连线上的所有点也属于该集合。" },
                { "key": "1-1", "title": "凸集定义", "content": "凸集定义是指集合中的任意两点之间的连线上的所有点也属于该集合。" },
                { "key": "1-2", "title": "凸集的例子", "content": "凸集的例子是指集合中的任意两点之间的连线上的所有点也属于该集合。" },
                { "key": "2", "title": "凸函数", "content": "凸函数是指函数的图像上的任意两点之间的连线上的所有点也在函数的图像上。" },
                { "key": "2-1", "title": "凸性的一阶条件", "content": "凸性的一阶条件是指函数的一阶导数大于等于零。" },
                { "key": "2-2", "title": "凸性的二阶条件", "content": "凸性的二阶条件是指函数的二阶导数大于等于零。" },
                { "key": "2-3", "title": "Jensen不等式", "content": "Jensen不等式是指对于凸函数和凸组合的函数，函数值的凸组合大于等于函数值的凸组合。" },
                { "key": "2-4", "title": "子级集", "content": "子级集是指集合中的任意子集也是该集合的子集。" },
                { "key": "2-5", "title": "凸函数的应用", "content": "凸函数的应用是指凸函数在各个领域中的应用，如经济学、优化问题等。" },
                { "key": "3", "title": "凸优化问题", "content": "凸优化问题是指目标函数是凸函数，约束条件是凸集的优化问题。" },
                { "key": "3-1", "title": "凸优化定义", "content": "凸优化定义是指目标函数是凸函数，约束条件是凸集的优化问题。" },
                { "key": "3-2", "title": "凸问题的全局优化", "content": "凸问题的全局优化是指找到目标函数的全局最优解的问题。" },
                { "key": "3-3", "title": "凸优化问题的例子", "content": "凸优化问题的例子是指目标函数是凸函数，约束条件是凸集的优化问题的具体实例。" }
            ],
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
        }
    },
    watch: {
        // 用于展示文件结构
        fileStructureData(newValue, oldValue) {
            console.log(newValue, oldValue)
            this.$nextTick(() => {
                this.fileStructData = newValue;
            })
        },
        // 用于展示Pdf
        fileData(newValue, oldValue) {

            console.log('pdfdata:',newValue[0].filename)
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
                .loading('Asking AI, waiting...', 2.5)
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
    width: 100%;
    height: 100%;
}

.left-column {
    flex: 3;
    min-width: 200px;
    min-height: 590px;
    border-right: 2px solid #eee;
}

.right-column {
    flex: 2;
    height: 100%;
}

.pdf-preview {
    height: 100%;
    min-height: 590px;
}

.pdf {
    width: 100%;
    height: 100%;
}

.file-struct {
    height: 40%;
    max-height: 300px;
    overflow-y: auto;
    border-bottom: 3px solid #eee;
}

.knowledge-card {
    height: 60%;
    /* margin-left: -25px; */
    overflow: hidden;
    overflow-y: auto;
}

.card {
    margin: 10px;
    padding: 10px;
}
</style>
