<template>
    <div ref="MainMindmap" id="mindmap-area">
    </div>
    <div id="main-legend">
        <div id="legend-header">
            <div id="legend-title">Legend
                <CaretUpOutlined id="collapse-legend-icon" class="collapse-legend-icon" @click="onCollapse" />
                <CaretDownOutlined id="expand-legend-icon" class="expand-legend-icon" @click="onExpand" />
            </div>

        </div>
        <div id="legend-divider"></div>
        <div id="main-legend-content"></div>
    </div>
    <!-- Quill 编辑器的容器，使用 v-if 控制显示和隐藏 -->
    <div v-if="showEditor" ref="editorContainer" class="editor-container"></div>
</template>
  
<script>
import { ref, onMounted } from "vue";
import * as d3 from "d3";
import cytoscape from 'cytoscape';
import cxtmenu from 'cytoscape-cxtmenu';
import cola from 'cytoscape-cola';
import contextMenus from 'cytoscape-context-menus';
import navigator from "cytoscape-navigator";
import dagre from "cytoscape-dagre";
import Quill from 'quill';
import {
    CaretUpOutlined,
    CaretDownOutlined,
} from "@ant-design/icons-vue";

import "cytoscape-navigator/cytoscape.js-navigator.css";
import 'quill/dist/quill.snow.css';

contextMenus(cytoscape);
navigator(cytoscape);
cytoscape.use(cxtmenu);
cytoscape.use(cola);
cytoscape.use(dagre);

import data from './MindmapData.json'
export default {
    components: {
        CaretUpOutlined,
        CaretDownOutlined
    },
    setup() {

    },
    data() {
        return {
            //showEditor
        };
    },
    watch: {

    },
    mounted() {
        this.drawMindmap()
        this.drawLegend()
        this.dragElement(document.getElementById("main-legend"))
    },
    emits: ['click'],
    methods: {
        // 绘制网络图
        drawMindmap() {
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
            ];

            const elements = this.transformData(data);
            // 初始化
            const cy = cytoscape({
                container: this.$refs.MainMindmap,
                elements: elements,
                style: [
                    {
                        selector: 'node',
                        style: {
                            'label': 'data(label)',
                            'text-opacity': 0.6,
                            'font-size': 8,
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
                    'font-size': 8,
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
                        content: "Learning Level",
                        tooltipText: "Select Learning Level",
                        selector: "node",
                        onClickFunction: function (e) {
                            console.log("Select Level" + e)
                        },
                    },
                    {
                        id: "record-note",
                        content: "Record Notes",
                        tooltipText: "Record Notes",
                        selector: "node",
                        onClickFunction: function (e) {
                            console.log("Recode Notes" + e)
                            this.showEditor = true; // 显示编辑器
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

            // 添加navigator
            var defaults = {
                container: false,
                viewLiveFramerate: 0,
                thumbnailEventFramerate: 30,
                thumbnailLiveFramerate: false,
                dblClickDelay: 200,
                removeCustomContainer: false,
                rerenderDelay: 100
            };
            cy.navigator(defaults);

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
        },

        // 图例
        drawLegend() {
            d3.selectAll("#main-legend-content svg").remove();
            let legendSvg = d3
                .select("#main-legend-content")
                .append("svg")
                .attr("width", "180px")
                .attr("height", "220px");

            let learningLevel = ["L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8"];
            let learningLevelColor = {
                L1: "#ff9f6d",
                L2: "#d88c9a",
                L3: "#a17fda",
                L4: "#c3e6a1",
                L5: "#4caead",
                L6: "#82b461",
                L7: "#fffb96",
                L8: "#87ccff",
            };

            let learningLevelExpl = {
                L1: "Concept",
                L2: "Principle / Math formula",
                L3: "Application",
                L4: "Implementation",
                L5: "Significance / Influence",
                L6: "Related Knowledge",
                L7: "Contrast Knowledge",
                L8: "Extended Knowledge",
            };


            let learningLevelWrapper = legendSvg
                .append("g")
                .attr("transform", "translate(5, 0)")

            learningLevelWrapper
                .append("text")
                .text("Learning Level")
                .attr("y", "15px")
                .attr("font-weight", "bold")
                .attr("font-size", "12px");

            let learningLevelG = learningLevelWrapper
                .selectAll("g")
                .data(learningLevel)
                .join("g")
                .attr(
                    "transform",
                    (d, i) => "translate(" + `${i * 6}`.toString() + ",16)"
                );
            learningLevelG
                .append("rect")
                .attr("x", (d, i) => i * 12)
                .attr("y", 10)
                .attr("width", 9)
                .attr("height", 15)
                .attr("fill", (d, i) => learningLevelColor[d])

            learningLevelG
                .append("text")
                .text((d) => d)
                .attr("x", (d, i) => i * 12)
                .attr("y", 35)
                .attr("font-size", "10px")
                .attr("text-align", "center");


            let start = 70;
            for (let i in learningLevelExpl) {
                learningLevelWrapper
                    .append("g")
                    .attr("transform", `translate(3,${start})`)
                    .append("text")
                    .text(i + ": " + learningLevelExpl[i])
                    .attr("font-size", "11px")
                    .attr("font-family", "Arial");
                start += 20;
            }
        },
        onCollapse() {
            d3.select("#main-legend-content").style("display", "none");
        },
        onExpand() {
            d3.select("#main-legend-content").style("display", "contents");
        },
        // 图例可拖拽
        dragElement(elmnt) {
            var pos1 = 0,
                pos2 = 0,
                pos3 = 0,
                pos4 = 0;
            elmnt.onmousedown = dragMouseDown;

            function dragMouseDown(e) {
                e = e || window.event;
                pos3 = e.clientX;
                pos4 = e.clientY;
                document.onmouseup = closeDragElement;
                document.onmousemove = elementDrag;
            }

            function elementDrag(e) {
                e = e || window.event;
                pos1 = pos3 - e.clientX;
                pos2 = pos4 - e.clientY;
                pos3 = e.clientX;
                pos4 = e.clientY;
                elmnt.style.top = elmnt.offsetTop - pos2 + "px";
                elmnt.style.left = elmnt.offsetLeft - pos1 + "px";
            }

            function closeDragElement() {
                document.onmouseup = null;
                document.onmousemove = null;
            }
        },

    }
};
</script>
  
<style>
#mindmap-area {
    width: 80%;
    height: 100%;
}

.editor-container {
    /* 样式调整，确保编辑器可见 */
    position: absolute;
    top: 20px;
    /* 根据需要调整 */
    right: 20px;
    /* 根据需要调整 */
    width: 400px;
    /* 根据需要调整 */
    height: 300px;
    /* 根据需要调整 */
    background: #fff;
    border: 1px solid #ccc;
    z-index: 10;
}

.__________cytoscape_container canvas {
    position: relative;
}

/*Ovveride Navigator border and background:*/
.cytoscape-navigator {
    border: 2px solid #bebebe !important;
    background: white !important;
    height: 150px !important;
    width: 150px !important;
    margin-bottom: 20%;
    margin-right: 37%;
}

/*Add border to View container:*/
.cytoscape-navigator .cytoscape-navigatorView {
    border: 2px solid #917312;
    background: #e7d8a8;
}

/*Ovveride overlay container when mouse is over Navigator*/
.cytoscape-navigator:hover .cytoscape-navigatorOverlay {
    border: 2px solid #917312;
    background: transparent;
}

/*Ovveride view's container when mouse is over view*/
.cytoscape-navigator.mouseover-view .cytoscape-navigatorView {
    background-color: rgba(184, 148, 70, 0.883);
}

.cy-context-menus-cxt-menu button {
    width: 100px !important;
    border: grey;
    background: rgba(0, 0, 0, 0.3);
    color: white;
}

.cy-context-menus-cxt-menu button:hover {
    background: rgba(0, 0, 0, 0.7);
}

#main-legend {
    position: absolute;
    width: 150px;
    top: 90px;
    right: 715px;
    background: rgba(238, 238, 238, 0.439);
    cursor: pointer;
}

#legend-header {
    width: 120px;
    padding-left: 9px;
    background: rgba(238, 238, 238, 0.439);
}

#legend-title {
    color: rgba(184, 148, 70, 0.883);
    font-size: 0.8em;
    /*margin-top: 5px;*/
    width: 100%;
    font-weight: bold;
    display: flex;
    justify-content: flex-start;
}

#legend-divider {
    width: 150px;
    height: 2px;
    background-color: rgba(170, 170, 170, 0.208);
}

#collapse-legend-icon svg {
    background: rgba(238, 238, 238, 0.439);
}

#collapse-legend-icon svg:hover {
    background: #ccc;
}

#expand-legend-icon svg {
    background: rgba(238, 238, 238, 0.439);
}

#expand-legend-icon svg:hover {
    background: #ccc;
}

.collapse-legend-icon {
    padding-top:3px;
    padding-left: 60px;
}

.expand-legend-icon {
    padding-top:3px;
    padding-left: 6px;
}
</style>
