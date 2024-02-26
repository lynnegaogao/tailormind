<template>
    <!--<div class="main-container" ref="maincontainer">-->
    <div class="sidebar" ref="sidebar"></div>
    <!--</div>-->
</template>
  
<script>
import { ref } from "vue";
import cytoscape from 'cytoscape';
import dagre from 'cytoscape-dagre';
import cxtmenu from 'cytoscape-cxtmenu';
import cola from 'cytoscape-cola';
import contextMenus from 'cytoscape-context-menus';

cytoscape.use(cola);
cytoscape.use(dagre);

import data from './MindmapData.json'
export default {
    components: {
    },
    setup() {

    },
    data() {
        return {
        };
    },
    watch: {

    },
    mounted() {
        this.initDraw(13)
    },

    methods: {
        // 初始化
        initDraw(count) {

            // 动态创建并初始化子 mindmap
            for (let i = 1; i <= count; i++) {
                const subDiv = document.createElement('div');
                subDiv.style.height = '100px'; // 设置高度为 100px
                subDiv.style.width = '100%';
                subDiv.style.transform = 'scale(2)'; // 内容放大 150%
                subDiv.style.transformOrigin = 'center'; // 设置放大的基点为中心
                subDiv.style.position = 'relative'; // 相对定位

                this.$refs.sidebar.appendChild(subDiv);

                // 为新创建的 div 调用 drawMindmap
                this.drawMindmap(subDiv, data);
            }
        },

        // 绘制网络图
        drawMindmap(refDiv, refData) {
            const levelcolor = [
                 //'#F07569',
                //'#F17E45',
                //'#ECE066',
                //'#5AA46A',
                //'#399789',
                //'#6AA2CA',
                //'#925096',
                //'#882BF2',
                "#ff9f6d",
                "#d88c9a",
                "#a17fda",
                "#c3e6a1",
                "#4caead",
                "#82b461",
                "#fffb96",
                "#87ccff",
            ]
            const elements = this.transformData(refData);
            //console.log(elements)
            // 初始化
            const cy = cytoscape({
                container: refDiv,
                elements: elements,
                style: [
                    {
                        selector: 'node',
                        style: {
                            'label': 'data(label)',
                            'text-opacity': 0.6,
                            'font-size': 10,
                            'width': 'data(size)',
                            'height': 'data(size)',
                            //'shape': function (ele) {
                            //    return ele.data('isSpecified') ? 'rectangle' : 'ellipse';
                            //},
                            'background-color': function (ele) {
                                if (ele.data('level') < 0) return "#eee1c7"
                                else return levelcolor[ele.data('level')]
                            },

                        }
                    }, {
                        selector: 'edge',
                        style: {
                            'width': 2,
                            'line-color': '#ccc',
                            'target-arrow-color': '#ccc',
                            'target-arrow-shape': 'triangle',
                            'curve-style': 'bezier',
                            //'label': 'data(relation)'
                        }
                    }
                ],
                layout: {
                    name: 'cose',
                    animate: true, // 启用动画
                    animationDuration: 1500, // 动画持续时间，单位为毫秒
                    animationEasing: 'ease-out', // 动画缓动函数
                },
                userZoomingEnabled: false, // 禁止用户缩放
                userPanningEnabled: false, // 禁止用户拖拽
            });



        },

        // 数据处理
        transformData(data) {
            //console.log(data.nodes)
            const nodes = data.nodes.map(node => ({
                data: {
                    id: node.id,
                    label: node.label,
                    size: node.size * 5, // 调整大小
                    isSpecified: node.isSpecified,
                    level: node.level
                }
            }));

            const edges = data.links.map(link => ({
                data: {
                    source: link.source,
                    target: link.target,
                    relation: link.relation
                }
            }));

            return [...nodes, ...edges];
        }

    }
};
</script>
  
<style scoped>
.sidebar {
    flex: 1;
    height: 590px;
    overflow-x: hidden; 
    overflow-y: auto; 
    box-sizing: border-box;
}
</style>
