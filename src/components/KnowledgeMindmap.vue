<template>
    <div ref="cyContainer" class="mindmap-area"></div>
</template>
  
<script>
import { ref } from "vue";
import cytoscape from 'cytoscape';

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
            const cy = cytoscape({
                container: this.$refs.cyContainer, // 容器元素
                elements: {// 节点和边的列表
                    nodes: [
                        { data: { id: 'a', label: 'Node A', size: 20, color: '#ff5722', shape: 'rectangle' } },
                        { data: { id: 'b', label: 'Node B', size: 30, color: '#3f51b5', shape: 'ellipse' } },
                        { data: { id: 'c', label: 'Node C', size: 10, color: '#4caf50', shape: 'ellipse' } }
                    ],
                    edges: [
                        { data: { source: 'a', target: 'b', label: 'Edge A-B' } },
                        { data: { source: 'b', target: 'c', label: 'Edge B-C' } },
                        { data: { source: 'c', target: 'a', label: 'Edge C-A' } }
                    ]
                },
                style: [ // 样式表
                    {
                        selector: 'node',
                        style: {
                            'background-color': 'data(color)',
                            'width': 'data(size)',
                            'height': 'data(size)',
                            'shape': 'data(shape)',
                            'label': 'data(label)'
                        }
                    }, {
                        selector: 'edge',
                        style: {
                            'width': 2,
                            'line-color': '#ccc',
                            'target-arrow-color': '#ccc',
                            'target-arrow-shape': 'triangle',
                            'curve-style': 'bezier',
                            'label': 'data(label)'
                        }
                    }
                ],
                layout: {
                    name: 'grid',
                    rows: 2
                }
            });
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
