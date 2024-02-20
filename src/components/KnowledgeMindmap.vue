<template>
    <div ref="cyContainer" class="mindmap-area"></div>
</template>
  
<script>
import { ref } from "vue";
import cytoscape from 'cytoscape';
//import dagre from 'cytoscape-dagre';
//cytoscape.use( dagre );
import cxtmenu from 'cytoscape-cxtmenu';
import cola from 'cytoscape-cola';
import contextMenus from 'cytoscape-context-menus';

cytoscape.use(cxtmenu);
cytoscape.use(cola);
contextMenus(cytoscape);

import data from './MindmapData_eng.json'
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
        this.drawGraph();
    },

    methods: {
        drawGraph() {
            const levelcolor = [
                '#F07569',
                '#F17E45',
                '#ECE066',
                '#5AA46A',
                '#399789',
                '#6AA2CA',
                '#925096',
                '#882BF2',
            ]
            const elements = this.transformData(data);

            // 初始化
            const cy = cytoscape({
                container: this.$refs.cyContainer,
                elements: elements,
                style: [
                    {
                        selector: 'node',
                        style: {
                            'label': 'data(label)',
                            'text-opacity': 0.6,
                            'font-size': 12,
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
                }
            });

            // 鼠标悬停在边上时显示标签
            cy.on('mouseover', 'edge', function (event) {
                const edge = event.target;
                edge.style({
                    'label': edge.data('relation'),
                    'text-opacity': 0.6,
                    'font-size': 12,
                    //'color': '#fff', 
                    //'font-family': 'Arial, sans-serif', 
                });
            });

            // 鼠标移开边时隐藏标签
            cy.on('mouseout', 'edge', function (event) {
                const edge = event.target;
                edge.style({
                    'label': '',
                    'text-opacity': 0
                });
            });

            // 右键进行问题推荐+选择学习目标+记笔记
            var menuOptions = {
                evtType: "cxttap",
                menuItems: [
                    {
                        id: "recommend-ques",
                        content: "Recommend",
                        tooltipText: "Recommend questions",
                        selector: "node",
                        onClickFunction: function (e) {
                            console.log("Recommend questions" + e)
                        },
                    },
                    {
                        id: "select-level",
                        content: "Level",
                        tooltipText: "Select Learning Level",
                        selector: "node",
                        onClickFunction: function (e) {
                            console.log("Select Level" + e)
                        },
                    },
                    {
                        id: "record-note",
                        content: "Record",
                        tooltipText: "Record Notes",
                        selector: "node",
                        onClickFunction: function (e) {
                            console.log("Recode Notes" + e)
                        },
                    },

                ],
            };
            cy.contextMenus(menuOptions);

            // 添加事件监听器以监听Del键实现删除节点
            document.addEventListener('keydown', function (event) {
                if (event.key === 'Delete' || event.keyCode === 46) {
                    // 获取当前选中的所有节点
                    const selectedNodes = cy.$('node:selected');
                    // 如果有选中的节点，则删除这些节点
                    if (selectedNodes.length > 0) {
                        selectedNodes.remove();
                    }
                }
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
.chat {
    display: flex;
    flex-direction: column;
    height: 100%;
    width: 100%;
}

.chat-window {
    flex-grow: 1;
    overflow-y: auto;
}

.mindmap-area {
    width: 100%;
    height: 100%;
}

.input-area {
    box-sizing: border-box;
    margin-top: 5px;
    margin-bottom: 5px;
    margin-left: 5px;
    margin-right: 5px;
    width: 98%;
}

.message {
    padding: 10px 15px;
    border-radius: 15px;
    margin: 5px;
    max-width: 70%;
    word-break: break-word;
}

.system-message {
    background-color: white;
    color: #7e7d7f;
    align-self: flex-start;
}

.user-message {
    background-color: #E8D4AD91;
    color: #7e7d7f;
    align-self: flex-end;
}

.my-message {
    text-align: right;
}
</style>
