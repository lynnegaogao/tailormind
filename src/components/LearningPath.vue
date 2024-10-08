<template>
    <div class="container">
        <div ref="LearningPath" id="learningpath-area">
        </div>
        <div id="toolbar">
            <a-config-provider :theme="{ token: { colorPrimary: '#4C5874' } }">
                <a-button @click="resetAction" style="margin-right: 8px; height:25px;line-height: normal; ">
                    <ReloadOutlined />Reset
                </a-button>
                <a-button @click="editAction" style="margin-right: 8px;height:25px;line-height: normal; ">
                    <EditOutlined />Edit
                </a-button>
                <a-button @click="submitAction" style="height:25px;line-height: normal; ">
                    <CheckOutlined />Submit
                </a-button>
            </a-config-provider>
        </div>
    </div>

</template>

<script>
import * as d3 from "d3";
import { Button, ConfigProvider, theme } from 'ant-design-vue';
import { ReloadOutlined, EditOutlined, CheckOutlined } from '@ant-design/icons-vue';

export default {
    name: 'LearningPath',
    components: {
        'a-button': Button,
        'a-config-provider': ConfigProvider,
        ReloadOutlined,
        EditOutlined,
        CheckOutlined
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
            learningLevelExpl: [
                "Concept",
                "Principle",
                "Application",
                "Implementation",
                "Significance",
                "Related",
                "Contrast",
                "Extended"
            ],

        };
    },
    props: {
        learningPathData: {
            type: Array,
            default: function () { return []; },
        },
        rmdMindmapOrNot: {
            type: Boolean,
            default: true,
        },
        isPathContrast: {
            type: Boolean,
            default: false,
        },

    },
    watch: {
        'learningPathData': {
            // 深度监听参数中具体数值的变化，一般监听只能发现数值的地址变化
            deep: true,
            handler(newValue, oldValue) {
                console.log(newValue, oldValue)
                // if (this.rmdMindmapOrNot) {
                this.$nextTick(() => {
                    this.drawLearningPath(newValue);
                })
                // }

            }
        },
        rmdMindmapOrNot(newValue, oldValue) {
            console.log(newValue, oldValue)
            if (!newValue) {
                this.$nextTick(() => {
                    this.drawLearningPath([]);
                })
            }

        },
        isReflection(newValue, oldValue) {
            console.log(newValue, oldValue)
            if (newValue) {
                this.$nextTick(() => {
                    this.drawLearningPath(this.learningPathData);
                })
            }

        },
        isPathContrast(newValue, oldValue) {
            console.log(newValue, oldValue)
            if (newValue) {
                this.$nextTick(() => {
                    this.drawLearningPath(this.learningPathData);
                })
            }

        },
    },
    mounted() {
        this.drawLearningPath(this.learningPathData);
        if (this.isReflection) {
            this.drawLearningPath(this.learningPathData);
        }
    },
    emits: ['resetLearningPathData'],
    methods: {
        drawLearningPath(learningPathData) {
            d3.selectAll("#learningpath-area svg").remove();
            // console.log("learning path数据：",learningPathData)
            // 预设参数
            const width = this.isPathContrast ? 800 : 1000
            const height = 390;
            const offsetX = 20;
            const offsetY = 10;
            const lineOffsetY = height * 0.8
            const timelineWidth = 25;
            const stackAreaOffsetY = 203
            const firstFlagOffsetX = 10;
            const distanceFromLine = 25;
            const extendedPoleHeight = timelineWidth + 40;
            const dashlineStroke = 2
            const milestonesNum = learningPathData ? learningPathData.length : 0

            // 处理stack area chart数据
            const processSubknowledgeLevels = (data) => {
                let processedData = data.map(item => {
                    // Initialize an object for the levels
                    const levels = { start: item.start };
                    for (let i = 1; i <= 8; i++) { // Assuming levels are from 1 to 8
                        levels[`L${i}`] = 0;
                    }

                    // Count the occurrence of each level
                    item.subknowledge.forEach(sub => {
                        levels[`L${sub.level}`]++;
                    });

                    return levels;
                });

                // 添加最后一个数据点，其中start=1且所有层级值为0
                const finalPoint = { start: 1 };
                for (let i = 1; i <= 8; i++) {
                    finalPoint[`L${i}`] = 0;
                }
                processedData.push(finalPoint);

                return processedData;
            };

            let levelData = []
            if (learningPathData) {
                levelData = processSubknowledgeLevels(learningPathData);
            }
            let stack = d3.stack()
                .keys(["L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8"]);
            let stackareaData = stack(levelData);

            // 创建SVG元素
            const svg = d3.select('#learningpath-area').append('svg')
                .attr('width', width)
                .attr('height', height)
                .attr('transform', `translate(${offsetX},${offsetY})`);

            // 定义比例尺
            const scale = d3.scaleLinear()
                .domain([0, 1])
                .range([0, width - 100]);
            const yScale = d3.scaleLinear()
                .domain([0, d3.max(levelData, d => d3.max(["L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8"], key => d[key]))])
                .range([height / 4, 0]);
            const area = d3.area()
                .x(d => scale(d.data.start)) // `start`值映射到X轴
                .y0(d => yScale(d[0]) + stackAreaOffsetY) // 使用堆叠数据的下界
                .y1(d => yScale(d[1]) + stackAreaOffsetY); // 使用堆叠数据的上界



            // 绘制时间线
            svg.append('line')
                .attr('x1', scale(0))
                .attr('y1', lineOffsetY)
                .attr('x2', scale(1))
                .attr('y2', lineOffsetY)
                .attr('stroke', '#8F939C')
                .attr('stroke-width', timelineWidth);

            var allMilestoneSvg = svg.append('g')
                .attr('transform', `translate(${firstFlagOffsetX},0)`)
                .attr('width', width)
                .attr('height', height)

            allMilestoneSvg.selectAll(".layer")
                .data(stackareaData)
                .enter().append("path")
                .attr("class", "layer")
                .attr("d", area)
                .attr('transform', 'translate(-5,0)')
                .style('opacity', 0.2)
                .style("fill", (d, i) => { return this.levelcolor[i] });


            // 绘制level虚线
            this.levelcolor.forEach((color, index) => {
                var dashOffsetY = lineOffsetY - timelineWidth / 2 - ((index + 1) * distanceFromLine); // 计算每条虚线的Y位置
                svg.append('line')
                    .attr('class', 'level-line')
                    .attr('data-level', color)
                    .attr('x1', scale(0))
                    .attr('y1', dashOffsetY)
                    .attr('x2', scale(1))
                    .attr('y2', dashOffsetY)
                    .attr('stroke', color)
                    .style('opacity', 0.4)
                    .attr('stroke-width', dashlineStroke)
                    .attr('stroke-dasharray', '5,5');

                // 添加标签
                svg.append('text')
                    .attr('x', scale(1) + 2)
                    .attr('y', dashOffsetY)
                    .attr('fill', color)
                    .style('opacity', 0.9)
                    .style('font-size', '12px')
                    .attr('alignment-baseline', 'middle')
                    .text(this.learningLevelExpl[index]);
            })

            // 绘制milestone
            if (learningPathData) {
                learningPathData.forEach((milestone, index) => {

                    var milestoneSvg = allMilestoneSvg.append('g')
                        .attr('id', `${milestone["milestone"]}`)
                        .attr('x', scale(milestone['start']))

                    // 绘制flag
                    var flagHeight = milestone["importance"] * 20
                    var flagWidth = milestone["importance"] * 10
                    var poleHeight = milestone["level"] * distanceFromLine + flagHeight / 4 + dashlineStroke / 2
                    var poleWidth = 3
                    var flagOffsetX = scale(milestone['start'])
                    var flagOffsetY = lineOffsetY - timelineWidth / 2 - poleHeight
                    var flagColor = this.levelcolor[milestone["level"] - 1]

                    this.drawFlag(milestoneSvg, { 'x': flagOffsetX, 'y': flagOffsetY }, index, flagColor, poleHeight, poleWidth, flagHeight, flagWidth, extendedPoleHeight)

                    // 绘制标签
                    var textX = scale(milestone['start']) + 10; // 文本的X位置
                    var textY = flagOffsetY - 20; // 第一行文本的Y位置

                    var textElement = milestoneSvg.append('text')
                        .attr('x', textX)
                        .attr('y', textY)
                        .attr('font-size', '13px') // 设置字体大小
                        .attr('font-weight', 'bold'); // 设置字体加粗

                    textElement.append('tspan')
                        .attr('x', textX)
                        .attr('y', textY)
                        .attr('text-anchor', 'left')
                        .text(`Milestone-${index}`);
                    textElement.append('tspan')
                        .attr('x', textX)
                        .attr('y', textY + 15) // 增加偏移量以创建第二行，假设每行高度约为15px
                        .attr('text-anchor', 'left')
                        .text(milestone["milestone"]);

                    // 绘制knowledge points
                    var knowledgePointsOffsetX = flagOffsetX + poleWidth + 10
                    var knowledgePointsOffsetY = lineOffsetY + timelineWidth / 2 + 15
                    var maxNum = Math.floor((scale(1) - knowledgePointsOffsetX) / 20)
                    if (learningPathData && index + 1 < milestonesNum) {
                        maxNum = Math.floor((scale(learningPathData[index + 1]['start']) - knowledgePointsOffsetX) / 20)
                    }
                    this.drawKnowledgePoints(milestoneSvg, { 'x': knowledgePointsOffsetX, 'y': knowledgePointsOffsetY }, maxNum, milestone['subknowledge'])

                });
            }


            // 添加交互
            // 对于每个flag和level虚线，添加mouseover和mouseout事件监听器
            const milestones = learningPathData
            const levelcolor = this.levelcolor
            if (milestones) {
                svg.selectAll('.flag')
                    .on('mouseover', function (event, d) {
                        // 增加flag和对应level虚线的透明度
                        var currentLevel = d3.select(this).attr('data-level');
                        d3.selectAll('.flag[data-level="' + currentLevel + '"]').style('opacity', 0.9);
                        d3.selectAll('.level-line[data-level="' + currentLevel + '"]').style('opacity', 0.9);

                        // 解析当前hover的milestone ID来获取subKnowledge
                        var milestoneIndex = this.id.split('-')[1];
                        var hoveredMilestones = milestones[milestoneIndex].subknowledge;

                        if (hoveredMilestones.length != 0) {
                            // 创建tooltip组
                            // 确定屏幕的宽度和高度
                            var offsetX = 20;
                            var offsetY = 20;
                            var canvasOffsetX = svg.node().getBoundingClientRect().left;
                            var canvasOffsetY = svg.node().getBoundingClientRect().top;

                            // 计算基于画布的偏移
                            var tooltipOffsetX = event.pageX - canvasOffsetX + offsetX;
                            var tooltipOffsetY = event.pageY - canvasOffsetY + offsetY;
                            // console.log('tooltipOffsetX:', tooltipOffsetX)
                            // console.log('tooltipOffsetY:', tooltipOffsetY)
                            // tooltipOffsetX = Math.max(200, Math.min(tooltipOffsetX, 400));
                            // tooltipOffsetY = Math.max(200, Math.min(tooltipOffsetY, 400));

                        
                            var tooltipGroup = svg.append('g')
                                .attr('class', 'tooltip-group')
                                .attr('transform', `translate(${tooltipOffsetX}, ${tooltipOffsetY})`);

                            // 首先，为了确保背景矩形位于其他元素之下，我们先添加它，但实际的尺寸稍后设置
                            var tooltipBackground = tooltipGroup.append('rect')
                                .style('fill', '#7e7d7f') // 设置灰色背景
                                .attr('rx', 5) // 圆角
                                .attr('ry', 5) // 圆角
                                .attr('width', 200) // 预设宽度，稍后根据内容调整
                                .attr('height', hoveredMilestones.length * 20 + 10) // 预设高度，根据项数动态调整
                                .attr('opacity', 0.1); // 可选：设置透明度以提高视觉效果

                            // 初始化文本宽度的变量，用于动态计算背景宽度
                            var maxTextWidth = 0;

                            // 对于每个subKnowledge，添加一个小圆形和文本
                            hoveredMilestones.forEach((knowledge, index) => {
                                // 添加小圆形
                                let radius = 2 + knowledge.importance;
                                let circleColor = 'steelblue'
                                if (knowledge.level >= 1 && knowledge.level <= 8) {
                                    circleColor = levelcolor[knowledge.level - 1]
                                }
                                tooltipGroup.append('circle')
                                    .attr('cx', 10) // 小圆形的初始x位置
                                    .attr('cy', index * 20 + 10) // 假设每个项的垂直间距是20，加10为顶部留白
                                    .attr('r', radius) // 小圆形半径
                                    .style('fill', circleColor)
                                    .style('opacity', 0.5);

                                // 添加文本解释
                                var textElement = tooltipGroup.append('text')
                                    .attr('x', 20) // 文本相对于小圆形的水平偏移
                                    .attr('y', index * 20 + 10) // 与对应小圆形垂直对齐，加10为顶部留白
                                    .attr('dominant-baseline', 'middle') // 确保文本垂直居中
                                    .attr('font-size', '13px')
                                    .text(knowledge.knowledge);

                                // 获取并更新最大文本宽度
                                var textWidth = textElement.node().getComputedTextLength();
                                maxTextWidth = Math.max(maxTextWidth, textWidth);
                            });

                            // 根据最大文本宽度动态调整背景矩形的宽度
                            tooltipBackground.attr('width', maxTextWidth + 30); // 加30为文本左侧和右侧留白
                        }


                    })
                    .on('mouseout', function (event, d) {
                        // 恢复flag和对应level虚线的透明度
                        var currentLevel = d3.select(this).attr('data-level');
                        d3.selectAll('.flag[data-level="' + currentLevel + '"]').style('opacity', 0.4);
                        d3.selectAll('.level-line[data-level="' + currentLevel + '"]').style('opacity', 0.5);

                        // 移除tooltip组
                        svg.selectAll('.tooltip-group').remove();
                    });
            }



        },

        // 绘制flag
        drawFlag(svg, position, index, color, poleHeight, poleWidth, flagWidth, flagHeight, extendedPoleHeight) {
            // 绘制旗杆
            svg.append('rect')
                .attr('data-level', color)
                .attr('class', 'flag')
                .attr('id', 'flag-' + index)
                .attr('x', position.x)
                .attr('y', position.y)
                .attr('width', poleWidth)
                .attr('height', poleHeight)
                .attr('fill', color)
                .style('opacity', 0.4);

            svg.append('rect')
                .attr('data-level', color)
                .attr('class', 'flag')
                .attr('id', 'flag-' + index)
                .attr('x', position.x)
                .attr('y', position.y + poleHeight)
                .attr('width', poleWidth)
                .attr('height', extendedPoleHeight)
                .attr('fill', color)
                .style('opacity', 0.4);
            const offeseX = 2
            // 绘制旗帜的三角形
            svg.append('polygon')
                .attr('class', 'flag')
                .attr('data-level', color)
                .attr('id', 'flag-' + index)
                .attr('points', `${offeseX + position.x + poleWidth},${position.y} 
                         ${offeseX + position.x + poleWidth},${position.y + flagHeight} 
                         ${offeseX + position.x + poleWidth + flagWidth},${position.y + flagHeight / 2}`)
                .attr('fill', color)
                .style('opacity', 0.4);
        },

        // 绘制knowledge points
        drawKnowledgePoints(svg, position, maxNum, subKnowledge) {
            let { x, y } = position;
            const circleSpacingBase = 10; // 圆圈之间的间距
            const circleRadiusBase = 2; // 基础半径大小



            // 只用展示一行knowledge points
            if (maxNum >= subKnowledge.length) {
                subKnowledge.forEach((knowledge, index) => {
                    let radius = circleRadiusBase + knowledge.importance;
                    let circleColor = 'steelblue'
                    if (knowledge.level >= 1 && knowledge.level <= 8) {
                        circleColor = this.levelcolor[knowledge.level - 1]
                    }
                    svg.append('circle')
                        .attr('cx', x + (index * (2 * circleRadiusBase + circleSpacingBase))) // 计算每个圆圈的x位置
                        .attr('cy', y) // y位置保持不变
                        .attr('r', radius) // 设置圆圈半径
                        .style('fill', circleColor)
                    // .on('click', function () { // 添加点击事件
                    //     // 计算tooltip和线的位置
                    //     let tooltipOffset = 20
                    //     let tooltipHeight = 50
                    //     let tooltipWidth = 100
                    //     let lineStartX = x + (index * (2 * circleRadiusBase + circleSpacingBase));
                    //     let lineStartY = y;
                    //     let lineEndX = lineStartX + tooltipOffset;
                    //     let lineEndY = lineStartY - tooltipOffset;


                    //     // 文本拆分和自适应高度的函数
                    //     function wrapText(text, width) {
                    //         let words = text.split(/\s+/).reverse(),
                    //             word,
                    //             line = [],
                    //             lineNumber = 0,
                    //             lineHeight = 1.1, // ems
                    //             x = lineEndX + 5,
                    //             y = lineEndY - tooltipHeight,
                    //             dy = 0,
                    //             tspan = svg.append('text').attr('x', x).attr('y', y).attr('dy', dy + 'em').style('fill', 'black').attr('alignment-baseline', 'middle');

                    //         while (word = words.pop()) {
                    //             line.push(word);
                    //             tspan.text(line.join(' '));
                    //             if (tspan.node().getComputedTextLength() > width) {
                    //                 line.pop();
                    //                 tspan.text(line.join(' '));
                    //                 line = [word];
                    //                 tspan = svg.append('text').attr('x', x).attr('y', y).attr('dy', ++lineNumber * lineHeight + 'em').text(word).style('fill', 'black').attr('alignment-baseline', 'middle');
                    //             }
                    //         }
                    //         return lineNumber + 1; // 返回总行数
                    //     }

                    //     // 绘制线段
                    //     svg.append('line')
                    //         .attr('x1', lineStartX)
                    //         .attr('y1', lineStartY)
                    //         .attr('x2', lineEndX)
                    //         .attr('y2', lineEndY)
                    //         .attr('stroke', 'black')
                    //         .style('stroke-width', 1);

                    //     // 绘制tooltip方块
                    //     svg.append('rect')
                    //         .attr('x', lineEndX)
                    //         .attr('y', lineEndY - tooltipHeight)
                    //         .attr('width', tooltipWidth)
                    //         .attr('height', tooltipHeight)
                    //         .style('fill', 'white')
                    //         .style('stroke', 'black');

                    //     // 在tooltip方块中添加文本
                    //     svg.append('text')
                    //         .attr('x', lineEndX + 5)
                    //         .attr('y', lineEndY - tooltipHeight / 2)
                    //         .text(knowledge.content)
                    //         .style('fill', 'black')
                    //         .attr('alignment-baseline', 'middle');

                    //     let lineCount = wrapText(knowledge.content, tooltipWidth - 10); // 减去一些padding
                    //     tooltipHeight = lineCount * 20; // 假设每行20像素高，这个值可以根据实际字体大小调整

                    //     // 重新绘制tooltip方块以匹配新的高度
                    //     svg.select('rect').remove(); // 移除旧的方块
                    //     svg.append('rect')
                    //         .attr('x', lineEndX)
                    //         .attr('y', lineEndY - tooltipHeight)
                    //         .attr('width', tooltipWidth)
                    //         .attr('height', tooltipHeight)
                    //         .style('fill', 'white')
                    //         .style('stroke', 'black');
                    // });
                })
            }
            // 展示多行knowledge points
            else {
                // 计算每行的高度，考虑到圆圈的直径和垂直间距
                const rowHeight = 2 * circleRadiusBase + circleSpacingBase;

                subKnowledge.forEach((knowledge, index) => {
                    let radius = circleRadiusBase + knowledge.importance; // 计算圆圈的半径
                    let rowIndex = Math.floor(index / maxNum); // 计算当前圆圈所在的行
                    let columnIndex = index % maxNum; // 计算当前圆圈在当前行的列索引

                    // 计算当前圆圈的x和y位置
                    let currentX = x + (columnIndex * (2 * circleRadiusBase + circleSpacingBase));
                    let currentY = y + (rowIndex * rowHeight);
                    let circleColor = 'steelblue'
                    if (knowledge.level >= 1 && knowledge.level <= 8) {
                        circleColor = this.levelcolor[knowledge.level - 1]
                    }
                    // 绘制圆圈
                    svg.append('circle')
                        .attr('cx', currentX)
                        .attr('cy', currentY)
                        .attr('r', radius)
                        .style('fill', circleColor);
                });
            }
        },

        // 清空所有learning path数据
        resetAction() {
            this.$emit('resetLearningPathData', [])
        },


    }
}
</script>

<style>
.container {
    position: relative;
}

#learningpath-area {
    width: 100%;
    height: 90%;
}

#toolbar {
    position: absolute;
    top: 10px;
    right: 80px;
    z-index: 10;
    /* Ensure this is higher than the z-index (if any) of learningpath-area */
    display: flex;
    gap: 8px;
}

.download-icon {
    cursor: pointer;
    /* Additional styles for the download icon */
}
</style>