<template>
    <div>
        <a-tree v-model:expandedKeys="expandedKeys" :tree-data="treeData" :show-line="true" :height="233">
            <template #title="{ key: treeKey, title }">
                <a-dropdown :trigger="['contextmenu']">
                    <span>{{ title }}</span>
                    <template #overlay>
                        <a-menu @click="({ key: menuKey }) => onContextMenuClick(treeKey, menuKey)">
                            <a-menu-item key="1">1st menu item</a-menu-item>
                            <a-menu-item key="2">2nd menu item</a-menu-item>
                            <a-menu-item key="3">3rd menu item</a-menu-item>
                        </a-menu>
                    </template>
                </a-dropdown>
            </template>
        </a-tree>
    </div>
</template>

<script>
import { Button, Tree } from 'ant-design-vue';
import { ref, watch } from 'vue';

export default {
    components: {
        AButton: Button,
        ATree: Tree
    },
    setup() {
        // 暂时把数据写死
        const treeData = [
            {
                "key": "0",
                "title": "凸集",
                "page": "1-3",
                "children": [
                    { "title": "凸集定义", "page": "1" },
                    { "title": "凸集的例子", "page": "2-3" },
                ]
            },
            {
                "title": "凸函数",
                "page": "3-7",
                "children": [
                    { "title": "凸性的一阶条件", "page": "4" },
                    { "title": "凸性的二阶条件", "page": "5" },
                    { "title": "Jensen不等式", "page": "5" },
                    { "title": "子级集", "page": "6" },
                    { "title": "凸函数的应用", "page": "6-7" },
                ]
            },
            {
                "title": "凸优化问题",
                "page": "7-12",
                "children": [
                    { "title": "凸优化定义", "page": "7-8" },
                    { "title": "凸问题的全局优化", "page": "9-10" },
                    { "title": "凸优化问题的例子", "page": "11-12" },
                ]
            }]

        // 自定义展开第一级
        const expandedKeys = ref(['0'])

        watch(expandedKeys, () => {
            console.log('expandedKeys', expandedKeys.value);
        });

        return {
            treeData,
            expandedKeys
        };
    }
};
</script>
