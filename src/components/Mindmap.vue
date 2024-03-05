<template>
    <div ref="MainMindmap" id="mindmap-area">
    </div>
    <div id="main-legend">
        <div id="legend-header">
            <div id="legend-title" class="title">Legend
                <CaretUpOutlined id="collapse-legend-icon" class="collapse-legend-icon" @click="onCollapse" />
                <CaretDownOutlined id="expand-legend-icon" class="expand-legend-icon" @click="onExpand" />
            </div>
        </div>
        <div id="legend-divider"></div>
        <div id="main-legend-content"></div>
    </div>
    <div class="toolbar-container">
        <a-config-provider :theme="{ token: { colorPrimary: '#4C5874' } }">
            <div id="layout-title" class="title"
                style="line-height: 25px; vertical-align: middle; display: inline-block;">Layout
                <a-select v-model:value="chartLayout" class="custom-select" clearIcon=""
                    style="width: 90px;height:25px;margin-left:5px;" @change="onChangeLayout">
                    <a-select-option value="cose">cose</a-select-option>
                    <a-select-option value="dagre">dagre</a-select-option>
                    <a-select-option value="euler">euler</a-select-option>
                    <a-select-option value="concentric">concentric</a-select-option>
                    <a-select-option value="fcose">fcose</a-select-option>
                </a-select>
            </div>
            <a-button @click="undoAction" style="height:25px;line-height: normal; vertical-align: middle;">
                <UndoOutlined />Undo
            </a-button>
            <a-button @click="redoAction" style="height:25px;line-height: normal; vertical-align: middle;">
                <RedoOutlined />Redo
            </a-button>
            <a-button @click="rollbackAction" style="height:25px;line-height: normal; vertical-align: middle;">
                <RollbackOutlined />Rollback
            </a-button>
            <a-button @click="submitAction" style="height:25px;line-height: normal; vertical-align: middle;">
                <CheckOutlined />Submit
            </a-button>
            <DownloadOutlined id="download-icon" class="download-icon" @click="handleDownload" />
        </a-config-provider>
    </div>
    <div id="quill-editor" style="position: absolute; display: none;">
        <div id="editor">
        </div> <!-- Quill编辑器将被初始化在这个div中 -->
    </div>
    <div id="wordCloud"></div>
    <a-config-provider :theme="{ token: { colorPrimary: '#4C5874' } }">
        <a-modal v-model:open="addNodeModalVisible" title="Add knowledge points to your mindmap!" @ok="handleNodeSubmit"
            @cancel="handleNodeCancel">
            <a-form ref="nodeForm" :model="formData" @submit.prevent="handleNodeSubmit">
                <a-form-item label="Knowledge Point">
                    <a-input v-model:value="formData.label" placeholder="Please enter the knowledge point..." />
                </a-form-item>
                <a-form-item label="Important Degree" name="size">
                    <a-select v-model:value="formData.size" placeholder="Please select...">
                        <a-select-option value="very important">very important</a-select-option>
                        <a-select-option value="important">important</a-select-option>
                        <a-select-option value="moderate">moderate</a-select-option>
                        <a-select-option value="ordinary">ordinary</a-select-option>
                        <a-select-option value="very ordinary">very ordinary</a-select-option>
                    </a-select>
                </a-form-item>
                <a-form-item label="Learning Level" name="level">
                    <a-select v-model:value="formData.level" placeholder="Please select...">
                        <a-select-option value="L1"> L1-Concept</a-select-option>
                        <a-select-option value="L2">L2-Principle / Math formula</a-select-option>
                        <a-select-option value="L3">L3-Application</a-select-option>
                        <a-select-option value="L4">L4-Implementation</a-select-option>
                        <a-select-option value="L5">L5-Significance / Influence</a-select-option>
                        <a-select-option value="L6">L6-Related Knowledge</a-select-option>
                        <a-select-option value="L7">L7-Contrast Knowledge</a-select-option>
                        <a-select-option value="L8">L8-Extended Knowledge</a-select-option>
                    </a-select>
                </a-form-item>
            </a-form>
        </a-modal>
        <a-modal v-model:open="addEdgeModalVisible" title="Add knowledge relations to your mindmap!"
            @ok="handleEdgeSubmit" @cancel="handleEdgeCancel">
            <a-form ref="nodeForm" :model="formData" @submit.prevent="handleEdgeSubmit">
                <a-form-item label="Relation Between Selected Nodes">
                    <a-input v-model:value="formData.relation" placeholder="Please enter the relation..." />
                </a-form-item>
            </a-form>
        </a-modal>
        <a-modal v-model:open="selectLevelVisible" title="Select Your Learning Goal!" @ok="handleLevelSubmit"
            @cancel="handleLevelCancel">
            <a-form ref="nodeForm" :model="formData" @submit.prevent="handleLevelSubmit">
                <a-form-item label="Learning Level" name="level">
                    <a-select v-model:value="formData.level" placeholder="Please select...">
                        <a-select-option value="L1">L1-Concept</a-select-option>
                        <a-select-option value="L2">L2-Principle / Math formula</a-select-option>
                        <a-select-option value="L3">L3-Application</a-select-option>
                        <a-select-option value="L4">L4-Implementation</a-select-option>
                        <a-select-option value="L5">L5-Significance / Influence</a-select-option>
                        <a-select-option value="L6">L6-Related Knowledge</a-select-option>
                        <a-select-option value="L7">L7-Contrast Knowledge</a-select-option>
                        <a-select-option value="L8">L8-Extended Knowledge</a-select-option>
                    </a-select>
                </a-form-item>
                <a-form-item label="Important Degree" name="size">
                    <a-select v-model:value="formData.size" placeholder="Please select...">
                        <a-select-option value="very important">very important</a-select-option>
                        <a-select-option value="important">important</a-select-option>
                        <a-select-option value="moderate">moderate</a-select-option>
                        <a-select-option value="ordinary">ordinary</a-select-option>
                        <a-select-option value="very ordinary">very ordinary</a-select-option>
                    </a-select>
                </a-form-item>
                <a-form-item label="Learning Path Starting" name="progress">
                    <!-- <a-slider v-model="formData.start" min="0" max="1" step="0.01" /> -->
                    <a-input-number v-model:value="formData.start" min="0" max="1" step="0.1" />
                </a-form-item>
            </a-form>
        </a-modal>
    </a-config-provider>
</template>

<script>
import { ref, onMounted } from "vue";
import * as d3 from "d3";
import cloud from 'd3-cloud';
import cytoscape from 'cytoscape';
import cxtmenu from 'cytoscape-cxtmenu';
import cola from 'cytoscape-cola';
import contextMenus from 'cytoscape-context-menus';
import navigator from "cytoscape-navigator";
import dagre from "cytoscape-dagre";
import euler from 'cytoscape-euler';
import coseBilkent from 'cytoscape-cose-bilkent';
import fcose from 'cytoscape-fcose';
import undoRedo from 'cytoscape-undo-redo';
import Quill from 'quill';
import {
    CaretUpOutlined,
    CaretDownOutlined,
    DownloadOutlined,
    UndoOutlined,
    RedoOutlined,
    RollbackOutlined,
    CheckOutlined
} from "@ant-design/icons-vue";
import {
    Form,
    Input,
    Modal,
    Select,
    Button,
    ConfigProvider,
    theme,
    Slider,
} from 'ant-design-vue';
import AInputNumber from 'ant-design-vue/lib/input-number';
import "cytoscape-navigator/cytoscape.js-navigator.css";
import 'quill/dist/quill.snow.css';

contextMenus(cytoscape);
navigator(cytoscape);
undoRedo(cytoscape);
cytoscape.use(cxtmenu);
cytoscape.use(cola);
cytoscape.use(dagre);
cytoscape.use(euler);
cytoscape.use(coseBilkent);
cytoscape.use(fcose);
// cytoscape.use(undoRedo);

export default {
    components: {
        CaretUpOutlined,
        CaretDownOutlined,
        DownloadOutlined,
        UndoOutlined,
        RedoOutlined,
        RollbackOutlined,
        CheckOutlined,
        AInputNumber,
        'a-form': Form,
        'a-form-item': Form.Item,
        'a-select': Select,
        'a-select-option': Select.Option,
        'a-input': Input,
        'a-modal': Modal,
        'a-button': Button,
        'a-config-provider': ConfigProvider,
        'a-slider': Slider,
    },
    setup() {
        // 修改ant-design默认配色
        const { token } = theme.useToken();
        return {
            token,
        };
    },
    data() {
        return {
            modalPos: null,
            cyInstance: null,
            ur: null,
            quillInstance: null,
            addNodeModalVisible: false,
            addEdgeModalVisible: false,
            selectLevelVisible: false,
            showEditor: false,
            formData: {
                label: '',
                size: '',
                level: '',
                relation: '',
                start: 0
            },
            selectedNodes: null,
            milestonesByUser: [],
            chartLayout: '',
            layoutOptionDict: {
                euler: {
                    name: "euler",
                    fit: true, // whether to fit to viewport
                    animate: true, // whether to transition the node positions
                    avoidOverlap: true,
                    springLength: 10,
                    mass: 7,
                },
                concentric: {
                    name: "concentric",
                    fit: false, // whether to fit to viewport
                    animate: true, // whether to transition the node positions
                    avoidOverlap: true,
                    minNodeSpace: 1,
                    concentric: function (node) {
                        return node.degree();
                    },
                    levelWidth: function (nodes) {
                        // the variation of concentric values in each level
                        return nodes.maxDegree() / 15;
                    },
                    spacingFactor: 1,
                    animationDuration: 1000, // duration of animation in ms if enabled
                },
                dagre: {
                    name: "dagre",
                    fit: false, // whether to fit to viewport
                    animate: true, // whether to transition the node positions
                    addNodeMoanimationDuration: 1000,
                },
                cose: {
                    name: 'cose',
                    animate: true,
                    addNodeMoanimationDuration: 1000,
                    animationEasing: 'ease-out',
                },
                fcose: {
                    name: "fcose",
                    fit: false,
                    quality: "default",
                    animate: true,
                    randomize: true,
                    avoidOverlap: true,
                    nodeRepulsion: 5000,
                    idealEdgeLength: 50,
                    edgeElasticity: 0.55,
                    gravity: 0.55,
                },
            },
            learningLevelColor: {
                "L1": "#9B6072",
                "L2": "#CE8D68",
                "L3": "#CFAD6D",
                "L4": "#9CA767",
                "L5": "#527840",
                "L6": "#406868",
                "L7": "#4C5874",
                "L8": "#776B9F",
            },
            levelcolor: [
                "#9B6072",
                "#CE8D68",
                "#CFAD6D",
                "#9CA767",
                "#527840",
                "#406868",
                "#4C5874",
                "#776B9F"
            ],
            formDataSize: {
                'very important': 5,
                'important': 4,
                'moderate': 3,
                'ordinary': 2,
                'very ordinary': 1
            },
            historyStack: [],
        };
    },
    props: {
        wordCloudData: {
            type: Array,
            default: function () { return []; },
        },
        mindMapData: {
            type: Object,
            default: function () { return {}; },
        },
    },
    watch: {
        wordCloudData(newValue, oldValue) {
            console.log(newValue, oldValue)
            this.$nextTick(() => {
                this.updateNodeBackgroundWithWordCloud()
            })
        },
        'mindMapData': {
            // 深度监听参数中具体数值的变化，一般监听只能发现数值的地址变化
            deep: true,
            handler(newValue, oldValue) {
                console.log(newValue, oldValue)
                this.$nextTick(() => {
                    this.drawMindmap()
                    this.drawLegend()
                    this.dragElement(document.getElementById("main-legend"))
                })
            }
        },

    },
    mounted() {
        // this.drawMindmap()
        this.drawLegend()
        this.dragElement(document.getElementById("main-legend"))

    },
    emits: ['click', 'generateWordCloud', 'getQuestionRmd', 'getLearningPathDataByUser'],
    methods: {
        // 绘制网络图
        drawMindmap() {
            d3.selectAll("#mindmap-area svg").remove();

            console.log("mindmap数据：", this.mindMapData)
            const elements = this.transformData(this.mindMapData); 
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
                            'background-color': (ele) => {
                                if (ele.data('level') < 1) return "#eee1c7"
                                else return this.levelcolor[ele.data('level') - 1]
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
                    },
                    {
                        selector: '.selected',
                        style: {
                            'border-width': 2,
                            'border-style': 'dashed',
                            'border-color': 'grey'
                        }
                    },
                    {
                        selector: '.hover',
                        style: {
                            'label': 'data(relation)',
                            'text-opacity': 0.6,
                            'font-size': 8,
                        }
                    },
                ],
                layout: {
                    name: 'cose',
                    animate: true,
                    addNodeMoanimationDuration: 1000,
                    animationEasing: 'ease-out',

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
                        onClickFunction: (e) => {
                            var node = e.target;
                            console.log("Recommend questions for node: ", node.id());
                            this.$emit('getQuestionRmd', node.id())
                        },
                    },
                    {
                        id: "select-level",
                        content: "Learning Level",
                        tooltipText: "Select Learning Level",
                        selector: "node",
                        onClickFunction: (e) => {
                            var node = e.target;
                            this.selectedNodes = node
                            this.selectLevelVisible = true
                        },
                    },
                    {
                        id: "record-note",
                        content: "Record Notes",
                        tooltipText: "Record Notes",
                        selector: "node",
                        onClickFunction: (e) => {
                            var pos = e.renderedPosition || e.position;
                            var node = e.target;
                            // 显示并定位Quill编辑器容器
                            var quillContainer = document.getElementById('quill-editor');
                            quillContainer.style.left = pos.x + 1100 + 'px';
                            quillContainer.style.top = pos.y + 100 + 'px';
                            quillContainer.style.display = 'block';
                            this.dragElement(document.getElementById('quill-editor'))

                            // 初始化Quill编辑器（如果尚未初始化）
                            if (!this.quillInstance) {
                                this.quillInstance = new Quill('#editor', {
                                    theme: 'snow'
                                });
                            }
                            // 构造与节点相关的预设文本
                            var presetText = `Record Something about: ${node.id()} ...Bagging算法，全称为Bootstrap Aggregating，是一种集成学习算法，旨在提高单个预测模型，如决策树，的稳定性和准确性。这种方法通过以下步骤实现：</p><p><br></p><p>1. **自助采样（Bootstrap Sampling）**：从原始数据集中随机选择N个样本，采用放回抽样的方式，这意味着同一个样本可以被多次选择。这样的一个样本集称为一个bootstrap样本。</p><p><br></p><p>2. **构建基学习器**：使用每个bootstrap样本独立训练一个基学习器。在bagging算法中，基学习器通常是决策树，但也可以是任何其他算法。</p><p><br></p><p>3. **聚合**：将所有基学习器的预测结果进行聚合。对于分类问题，通常采用多数投票法；对于回归问题，则通常采用平均法。</p><p><br></p><p>Bagging的关键优势在于它可以减少模型的方差，从而提高模型的稳定性。通过结合多个模型的预测，它可以降低过拟合的风险，并在面对不同的数据子集时表现出更好的泛化能力。Bagging是随机森林算法的基础，随机森林通过在构建决策树时引入更多的随机性来进一步提高模型的性能。.</p>`; // 假设node对象有id()方法获取节点标识
                            // 首先清空编辑器内容
                            this.quillInstance.setText('');
                            // 设置预设文本
                            this.quillInstance.setText(presetText);

                            // 首先获取到工具栏和编辑器容器的元素
                            var toolbar = document.querySelector('.ql-toolbar')
                            var editorContainer = document.querySelector('.ql-container')
                            var editor = document.querySelector('.ql-editor')

                            editorContainer.style.display = ''
                            toolbar.style.display = ''
                            editor.style.display = ''

                            // 双击toolbar隐藏container
                            toolbar.addEventListener('dblclick', function () {
                                // 检查编辑器容器当前的显示状态，并切换它
                                if (editorContainer.style.display === 'none') {
                                    editorContainer.style.display = '';
                                } else {
                                    editorContainer.style.display = 'none';
                                }
                            });

                            // 按下Esc键隐藏编辑器容器
                            document.addEventListener('keydown', (event) => {
                                if (event.key === "Escape") {
                                    // 获取编辑器内容
                                    var editorContent = this.quillInstance.root.innerHTML;
                                    if (editorContent != '') {
                                        this.$emit('generateWordCloud', node, editorContent)
                                    }
                                    // 隐藏编辑器容器
                                    editorContainer.style.display = 'none'
                                    toolbar.style.display = 'none'
                                    editor.style.display = 'none';
                                }
                            }, { once: true });


                        },
                    },

                ],
            };
            cy.contextMenus(menuOptions);

            // 监听Del键删除节点或边
            document.addEventListener('keydown', (event) => {
                if (event.key === 'Delete' || event.keyCode === 46) {
                    // 获取当前选中的所有元素（节点和边）
                    const selectedElements = cy.$(':selected');

                    // 如果没有选中的元素，则直接返回
                    if (selectedElements.length === 0) {
                        return;
                    }

                    // 获取与选中节点相关联的边（即选中节点的所有相邻边）
                    const relatedEdges = selectedElements.connectedEdges();

                    // 合并选中的元素和相关的边
                    const elementsToRemove = selectedElements.union(relatedEdges);

                    // 定义执行删除选中元素及其相关边的函数
                    const doFunc = () => {
                        elementsToRemove.remove();
                    };

                    // 定义撤销删除的函数，恢复元素及其相关边
                    const undoFunc = () => {
                        cy.add(elementsToRemove.jsons());
                    };

                    // 使用 this.ur.action() 创建一个自定义操作
                    this.ur.action("remove-selected-elements-and-edges", doFunc, undoFunc);

                    // 执行自定义操作
                    this.ur.do("remove-selected-elements-and-edges");
                }
            });


            // 点击空白处添加node
            cy.on('cxttap', (event) => {
                const evtTarget = event.target;
                if (evtTarget === cy) { // 确保是在空白处点击
                    event.preventDefault(); // 阻止默认的右键菜单

                    const pos = event.position || event.cyPosition; // 获取鼠标位置
                    this.addNode(pos, cy); // 打开模态对话框并且传递位置和cy对象

                }
            });

            // 动态添加edge
            let selectedNodes = [];
            cy.on('tap', 'node', (evt) => {
                const node = evt.target;
                // 检查节点是否已经被选中
                if (selectedNodes.includes(node)) {
                    // 移除已选中的节点
                    selectedNodes = selectedNodes.filter(n => n !== node);
                    node.removeClass('selected');
                } else {
                    // 如果选中的节点少于2个，添加新的选中节点
                    if (selectedNodes.length < 2) {
                        selectedNodes.push(node);
                        node.addClass('selected');
                    } else {
                        // 如果已有两个节点被选中，清除旧的选中状态
                        selectedNodes.forEach(n => n.removeClass('selected'));
                        selectedNodes = [node]; // 将当前节点作为新的选中节点
                        node.addClass('selected');
                    }
                }

                if (selectedNodes.length === 2) {
                    this.addEdge(selectedNodes, cy)
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
            this.cyInstance = cy

            // 记录用户数据undo-redo
            var options = {
                isDebug: false,
                actions: {},
                undoableDrag: true,
                stackSizeLimit: undefined,
            }
            this.ur = this.cyInstance.undoRedo(options);
        },

        // 添加节点表单
        addNode(pos, cy) {
            this.modalPos = pos
            this.cyInstance = cy
            this.addNodeModalVisible = true;
        },
        handleNodeCancel() {
            this.addNodeModalVisible = false;
        },
        handleNodeSubmit() {
            const pos = this.modalPos;
            const cy = this.cyInstance;
            const nodeSize = this.formDataSize[this.formData.size]
            const nodeColor = this.learningLevelColor[this.formData.level]
            const nodeLabel = this.formData.label
            const doFunc = () => {
                var newNode = {
                    group: 'nodes',
                    data: { id: nodeLabel, label: nodeLabel },
                    position: pos,
                    style: {
                        'width': 5 * nodeSize,
                        'height': 5 * nodeSize,
                        'content': this.formData.label,
                        'background-color': nodeColor
                    }
                };
                cy.add(newNode);

                // 触发重新布局
                let layout = cy.layout({
                    name: 'cose',
                    animate: true,
                    addNodeMoanimationDuration: 1000,
                    animationEasing: 'ease-out',
                });
                layout.run(); // 运行布局
            };

            // 定义撤销添加节点的函数
            const undoFunc = () => {
                cy.$id(nodeLabel).remove(); // 删除刚刚添加的节点
            };

            // 使用 this.ur.action() 创建一个自定义操作
            const customAction = this.ur.action("add-node", doFunc, undoFunc);

            // 执行自定义操作
            this.ur.do("add-node", customAction);

            this.addNodeModalVisible = false;
            this.formData = {
                label: '',
                size: '',
                level: '',
                relation: ''
            }
        },

        // 添加边表单
        addEdge(selectedNodes, cy) {
            this.selectedNodes = selectedNodes
            this.cyInstance = cy
            this.addEdgeModalVisible = true;
        },
        handleEdgeCancel() {
            this.addEdgeModalVisible = false;
        },
        handleEdgeSubmit() {
            const selectedNodes = this.selectedNodes
            const cy = this.cyInstance;
            const relation = this.formData.relation
            const edgeId = 'edge' + Math.random();

            const doFunc = () => {
                const newEdge = {
                    group: 'edges',
                    data: {
                        id: edgeId, // 使用前面生成的唯一ID
                        source: selectedNodes[0].id(),
                        target: selectedNodes[1].id(),
                        relation: relation
                    }
                };
                cy.add(newEdge);
            };

            const undoFunc = () => {
                cy.$id(edgeId).remove(); // 删除刚刚添加的边
            };

            cy.on('mouseover', 'edge', function (event) {
                const edge = event.target;
                edge.addClass('hover'); // 添加悬停样式类以显示标签
            });
            cy.on('mouseout', 'edge', function (event) {
                const edge = event.target;
                edge.removeClass('hover'); // 移除悬停样式类以隐藏标签
            });
            // 触发重新布局
            let layout = cy.layout({
                name: 'cose',
                animate: true,
                addNodeMoanimationDuration: 1000,
                animationEasing: 'ease-out',
            });

            layout.run(); // 运行布局

            // 使用 this.ur.action() 创建一个自定义操作
            const customAction = this.ur.action("add-edge", doFunc, undoFunc);
            this.ur.do("add-edge", customAction);

            this.selectedNodes.forEach(node => node.removeClass('selected'));
            this.selectedNodes = null;
            this.addEdgeModalVisible = false;
        },

        // 选择learning level
        handleLevelCancel() {
            this.selectLevelVisible = false;
        },
        handleLevelSubmit() {
            const selectNode = this.selectedNodes
            const oldNodeColor = selectNode.style('background-color')
            const oldNodeSize = [selectNode.style('height'), selectNode.style('width')]
            console.log(oldNodeSize)
            const nodeColor = this.learningLevelColor[this.formData.level]
            const nodeLevel = parseInt(this.formData.level.match(/\d+/)[0])
            const nodeStart = this.formData.start
            const nodeImportance = this.formDataSize[this.formData.size]
            const newMilestone = {
                "start": nodeStart,
                "level": nodeLevel,
                "milestone": selectNode.id(),
                "importance": nodeImportance,
                "subknowledge": []
            }
            // 查找具有相同milestone值的对象在数组中的索引
            const index = this.milestonesByUser.findIndex(m => m.milestone === newMilestone.milestone);

            if (index !== -1) {
                // 如果找到了具有相同milestone的对象，就替换这个对象
                this.milestonesByUser[index] = newMilestone;
            } else {
                // 如果没有找到，就添加新的对象到数组
                this.milestonesByUser.push(newMilestone);
            }

            // 定义一个redo undo更改颜色的函数
            const doFunc = () => {
                selectNode.style('background-color', nodeColor);
                selectNode.style('height', nodeImportance*5);
                selectNode.style('width', nodeImportance*5);

            };
            const undoFunc = () => {
                selectNode.style('background-color', oldNodeColor);
                selectNode.style('height', oldNodeSize[0]);
                selectNode.style('width', oldNodeSize[1]);
            };
            const customAction = this.ur.action("change-node-color", doFunc, undoFunc);
            // 存储action到堆栈中
            this.ur.do("change-node-color", customAction);

            this.formData.level = '';
            this.formData.start = 0;
            this.formData.start='',
            this.selectedNodes = null;
            this.selectLevelVisible = false;
        },

        // 更新布局
        onChangeLayout() {
            var newLayout = this.layoutOptionDict[this.chartLayout]
            var cy = this.cyInstance
            console.log(newLayout)

            // 应用新布局
            let layout = cy.layout(newLayout);
            layout.run();
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
                L1: "#9B6072",
                L2: "#CE8D68",
                L3: "#CFAD6D",
                L4: "#9CA767",
                L5: "#527840",
                L6: "#406868",
                L7: "#4C5874",
                L8: "#776B9F",
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

        // 下载当前mindmap为png图片
        handleDownload() {
            const cy = this.cyInstance
            // 获取 Cytoscape 图的数据 URL
            const cyDataURL = cy.png({ output: 'blob', full: true });

            const link = document.createElement('a');
            link.href = URL.createObjectURL(cyDataURL);
            link.download = 'knowledge-mindmap.png';

            // 模拟点击链接，触发下载
            link.click();

            // 释放 URL 对象
            URL.revokeObjectURL(link.href);
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

        // 绘制笔记相关词云并更新节点背景
        updateNodeBackgroundWithWordCloud() {
            var cy = this.cyInstance;
            var updateNode = this.wordCloudData.node;
            var wordCloudData = this.wordCloudData.data;
            var oldStyle = updateNode.style(); // 保存原始样式以便撤销

            const width = parseInt(updateNode.style().width) * 2.7;  // SVG 宽度
            const height = parseInt(updateNode.style().height) * 2.7; // SVG 高度


            // 创建 SVG 元素
            const svgElement = d3.select("#wordCloud").append("svg")
                .attr("width", 500)
                .attr("height", 500)
                .append("g")
                .attr("transform", "translate(" + 50 + "," + 200 + ")");

            // 绘制词云
            svgElement.selectAll("text")
                .data(wordCloudData)
                .enter().append("text")
                .style("font-size", d => d.size * 15 + "px")
                .style("font-family", "Arial")
                .style("fill", 'black')
                .attr("x", (d, i) => (i % 2) * 180) // 根据需要调整以避免重叠
                .attr("y", (d, i) => Math.floor(i / 2) * 100) // 根据需要调整以避免重叠
                .text(d => d.text);

            // 获取 SVG 元素并序列化
            var svgElementNode = document.querySelector('#wordCloud svg');
            d3.selectAll("#wordCloud svg").remove();
            var svgData = new XMLSerializer().serializeToString(svgElementNode);
            var imgSrc = 'data:image/svg+xml;base64,' + btoa(unescape(encodeURIComponent(svgData)));
            console.log(imgSrc)
            // 更新 Cytoscape 节点的样式
            var updateNode = cy.$id(updateNode.id())

            // undo-redo settings
            const doFunc = () => {
                updateNode.style({
                    'background-image': imgSrc,
                    'background-fit': 'cover',
                    'width': width + 'px',
                    'height': height + 'px',
                });
            };
            const undoFunc = () => {
                updateNode.style(oldStyle);
            };
            const customAction = this.ur.action("update-node-style", doFunc, undoFunc);
            this.ur.do("update-node-style", customAction);
        },

        undoAction() {
            console.log(this.ur.actions)
            this.ur.undo();
        },
        redoAction() {
            console.log(this.ur.actions)
            this.ur.redo();
        },
        rollbackAction() {
            console.log(this.ur.actions)
            this.ur.undoAll();
        },
        submitAction() {
            if (this.milestonesByUser) {
                this.$emit('getLearningPathDataByUser', this.milestonesByUser)
            }

        },



    }
};
</script>

<style>
#mindmap-area {
    width: 70%;
    height: 100%;
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
    margin-bottom: 21%;
    /* 数字越小 越往上 */
    margin-right: 38.5%;
    /* 数字越小 越往右 */
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
    background: rgba(0, 0, 0, 0.197);
    color: white;
}

.cy-context-menus-cxt-menu button:hover {
    background: rgba(0, 0, 0, 0.257);
}

#main-legend {
    position: absolute;
    width: 150px;
    top: 110px;
    right: 850px;
    /* 数字越大 越靠左*/
    background: rgba(238, 238, 238, 0.439);
    cursor: pointer;
}

#legend-header {
    width: 120px;
    padding-left: 9px;
    background: rgba(238, 238, 238, 0.439);
}

.title {
    color: #4C5874;
    font-size: 13px;
    width: 100%;
    font-weight: bold;
    display: flex;
    justify-content: flex-start;
    align-items: center;
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
    padding-top: 3px;
    padding-left: 60px;
}

.expand-legend-icon {
    padding-top: 3px;
    padding-left: 5px;
}

.download-icon {
    margin-left: 5px;
    cursor: pointer;
}

.custom-select .ant-select-selector {
    height: 25px !important;
    line-height: 20px !important;
}

.custom-select .ant-select-selection-item,
.custom-select .ant-select-selection-placeholder {
    line-height: 20px !important;
}

.toolbar-container {
    position: absolute;
    top: 80px;
    right: 330px;
    display: flex;
    gap: 8px;

}

#editor {
    width: 400px;
    height: 200px;
    overflow-y: auto;
}

.ql-container {
    background-color: rgba(211, 211, 210, 0.289);

}

.ql-toolbar {
    background-color: rgba(211, 211, 210, 0.289);
}
</style>
