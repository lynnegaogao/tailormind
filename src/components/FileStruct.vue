<template>
    <div ref="treeContainer">
        <a-tree v-model:expandedKeys="expandedKeys" :tree-data="treeData" :show-line="true" :height="500"
            style="font-size: medium; margin: 10px 0px 0 20px" @select=handleSelect class="file-struct-tree">
            <template #title="{ key: key, title }">
                <a-dropdown :trigger="['contextmenu']">
                    <span>{{ title }}</span>
                </a-dropdown>
            </template>
        </a-tree>
    </div>
</template>

<script>
import { Button, Tree } from 'ant-design-vue';
import { ref, watch, computed } from 'vue';

export default {
    name: 'FileStruct',
    components: {
        AButton: Button,
        ATree: Tree
    },
    data() {
        return {
            treeData: [
                {
                    "key": "1",
                    "title": "凸集",
                    "page": "1-3",
                    "children": [
                        { "key": "1-1", "title": "凸集定义", "page": "1" },
                        { "key": "1-2", "title": "凸集的例子", "page": "2-3" },
                    ]
                },
                {
                    "key": "2",
                    "title": "凸函数",
                    "page": "3-7",
                    "children": [
                        { "key": "2-1", "title": "凸性的一阶条件", "page": "4" },
                        { "key": "2-2", "title": "凸性的二阶条件", "page": "5" },
                        { "key": "2-3", "title": "Jensen不等式", "page": "5" },
                        { "key": "2-4", "title": "子级集", "page": "6" },
                        { "key": "2-5", "title": "凸函数的应用", "page": "6-7" },
                    ]
                },
                {
                    "key": "3",
                    "title": "凸优化问题",
                    "page": "7-12",
                    "children": [
                        { "key": "3-1", "title": "凸优化定义", "page": "7-8" },
                        { "key": "3-2", "title": "凸问题的全局优化", "page": "9-10" },
                        { "key": "3-3", "title": "凸优化问题的例子", "page": "11-12" }
                    ]
                }
            ],
            expandedKeys: ['1']
        }
    },
    methods: {
        // 计算树的高度
        calculateTreeHeight() {
            const treeContainerHeight = this.$refs.treeContainer.offsetHeight;
            this.treeHeight = `${treeContainerHeight}px`;
        },
        handleSelect(selectedKeys, e) {
            console.log('selectedKeys', selectedKeys);
            if (selectedKeys.length > 0) {
                const selectedKey = selectedKeys[0];
                this.$emit('selectNode', selectedKey);
            }
        }
    },
    mounted() {
        console.log('treeData', this.treeData);
        // 计算高度
        this.calculateTreeHeight();
        window.addEventListener('resize', this.calculateTreeHeight);
    },
    beforeUnmount() {
        window.removeEventListener('resize', this.calculateTreeHeight);
    },
    computed: {
        treeHeight: {
            get() {
                return this._treeHeight;
            },
            set(value) {
                this._treeHeight = value;
            }
        }
    }
};
</script>

<style scoped>
</style>