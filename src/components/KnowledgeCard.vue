<template>
    <div ref="cardsContainer" class="scrollable-container">
        <a-tree ref="cardList" :tree-data="cardData" :show-icon="false" :height="400" style="font-size: medium;"
            @rightClick="alert('rightClick')">
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
    <!-- <div class="scrollable-container">
        <a-card size="small" v-for="(card, index) in cardData" :key="index" :title="card.title" style="" class="card">
            <div class="card-content">
                <p>{{ card.content }}</p>
            </div>
        </a-card>
    </div> -->
</template>

<script>
import { Card, Tree, Dropdown, Menu, message } from 'ant-design-vue';
import { ref, computed } from 'vue';

export default {
    name: 'KnowledgeCard',
    components: {
        ACard: Card,
        ATree: Tree,
        ADropdown: Dropdown,
        AMenu: Menu,
        AMenuItem: Menu.Item
    },
    data() {
        return {
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
            selectedKey: ''
        }
    },
    methods: {
        // 计算树的高度
        // calculateTreeHeight() {
        //     const treeContainerHeight = this.$refs.cardsContainer.offsetHeight;
        //     this.treeHeight = `${treeContainerHeight}px`;
        // },

        // 调用 antd-vue 的 scrollTo 方法来滚动到指定 key 的节点位置
        scrollTo(key) {
            this.selectedKey = key;
            this.$refs.cardList.scrollTo({ key: key, align: 'top' });
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
    mounted() {
        console.log('treeData', this.treeData);
        // 计算高度
        // this.calculateTreeHeight();
        // window.addEventListener('resize', this.calculateTreeHeight);
    },
    beforeUnmount() {
        // window.removeEventListener('resize', this.calculateTreeHeight);
    },
    computed: {
        // treeHeight: {
        //     get() {
        //         return this._treeHeight;
        //     },
        //     set(value) {
        //         this._treeHeight = value;
        //     }
        // }
    }
};
</script>

<style>
.scrollable-container {
    margin-left: -25px;
    height: 100%;
    /* overflow-y: auto; */
    padding: 10px;
}

.card {
    margin: 10px;
    padding: 0;
}
</style>