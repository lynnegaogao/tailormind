<template>
    <div ref="LearningPath" id="learningpath-area">
    </div>
</template>
  
<script>
import * as d3 from "d3";

export default {
    name: 'LearningPath',
    components: {
    },
    setup() {

    },
    data() {
        return {
            levelcolor: [
                "#ff9f6d",
                "#d88c9a",
                "#a17fda",
                "#c3e6a1",
                "#4caead",
                "#82b461",
                "#fffb96",
                "#87ccff",
            ],
            milestones: [
                {
                    "start": 0.00,
                    "level": 6,
                    "milestone": "Ensemble Learning",
                    "importance": 4,
                    "subknowledge": [
                        {
                            "level": 2,
                            "knowledge": "Concept of Ensemble Learning",
                            "importance": 5
                        },
                        {
                            "level": 2,
                            "knowledge": "Benefits of Ensemble Learning",
                            "importance": 2
                        },
                        {
                            "level": 2,
                            "knowledge": "Basic Ensemble Methods",
                            "importance": 5
                        }
                    ]
                },
                {
                    "start": 0.30,
                    "level": 3,
                    "milestone": "Bagging",
                    "importance": 2,
                    "subknowledge": [
                        {
                            "level": 4,
                            "knowledge": "Principles of Bagging",
                            "importance": 3
                        },
                        {
                            "level": 4,
                            "knowledge": "Implementing Bagging Models",
                            "importance": 3
                        },
                        {
                            "level": 4,
                            "knowledge": "Advantages and Limitations of Bagging",
                            "importance": 3
                        }
                    ]
                },
                {
                    "start": 0.5,
                    "level": 3,
                    "milestone": "Boosting",
                    "importance": 2,
                    "subknowledge": [
                        {
                            "level": 4,
                            "knowledge": "Basics of Boosting",
                            "importance": 3
                        },
                        {
                            "level": 4,
                            "knowledge": "Types of Boosting Algorithms",
                            "importance": 3
                        },
                        {
                            "level": 4,
                            "knowledge": "Boosting vs Bagging",
                            "importance": 3
                        }
                    ]
                },
                {
                    "start": 0.63,
                    "level": 8,
                    "milestone": "Random Forests",
                    "importance": 5,
                    "subknowledge": [
                        {
                            "level": 6,
                            "knowledge": "Introduction to Random Forests",
                            "importance": 3
                        },
                        {
                            "level": 6,
                            "knowledge": "How Random Forests Work",
                            "importance": 3
                        },
                        {
                            "level": 6,
                            "knowledge": "Applying Random Forests in Real-World Scenarios",
                            "importance": 3
                        },
                        {
                            "level": 6,
                            "knowledge": "Introduction to Random Forests",
                            "importance": 3
                        },
                        {
                            "level": 6,
                            "knowledge": "How Random Forests Work",
                            "importance": 3
                        },
                        {
                            "level": 6,
                            "knowledge": "Applying Random Forests in Real-World Scenarios",
                            "importance": 3
                        },
                        {
                            "level": 6,
                            "knowledge": "Introduction to Random Forests",
                            "importance": 3
                        },
                        {
                            "level": 6,
                            "knowledge": "How Random Forests Work",
                            "importance": 3
                        },
                        {
                            "level": 6,
                            "knowledge": "Applying Random Forests in Real-World Scenarios",
                            "importance": 3
                        }
                    ]
                },
                {
                    "start": 0.9,
                    "level": 5,
                    "milestone": "Stacking",
                    "importance": 2,
                    "subknowledge": [
                        {
                            "level": 6,
                            "knowledge": "Introduction to Stacking",
                            "importance": 3
                        },
                        {
                            "level": 6,
                            "knowledge": "How Stacking Works",
                            "importance": 3
                        },
                        {
                            "level": 6,
                            "knowledge": "Implementing Stacking Models",
                            "importance": 3
                        },
                        {
                            "level": 6,
                            "knowledge": "Use Cases and Examples of Stacking",
                            "importance": 3
                        }
                    ]
                }
            ],
        };
    },
    props: {


    },
    watch: {

    },
    mounted() {
        this.drawLearningPath();
    },
    emits: [],
    methods: {
        drawLearningPath() {
            d3.selectAll("#learningpath-area svg").remove();

            // 预设参数
            const width = 800;
            const height = 460;
            const offsetX = 35;
            const offsetY = 0;
            const lineOffsetY = height / 3 * 2
            const timelineWidth = 25;
            const firstFlagOffsetX = 10;
            const distanceFromLine = 25;
            const extendedPoleHeight = timelineWidth + 40;
            const dashlineStroke = 2
            const milestonesNum = this.milestones.length

            // 创建SVG元素
            const svg = d3.select('#learningpath-area').append('svg')
                .attr('width', width)
                .attr('height', height)
                .attr('transform', `translate(${offsetX},${offsetY})`);

            // 定义比例尺
            const scale = d3.scaleLinear()
                .domain([0, 1])
                .range([0, width - 50]);

            // 绘制时间线
            svg.append('line')
                .attr('x1', scale(0))
                .attr('y1', lineOffsetY)
                .attr('x2', scale(1))
                .attr('y2', lineOffsetY)
                .attr('stroke', '#ddd4c16a')
                .attr('stroke-width', timelineWidth);

            var allMilestoneSvg = svg.append('g')
                .attr('transform', `translate(${firstFlagOffsetX},0)`)
                .attr('width', width)
                .attr('height', height)

            // 绘制level虚线
            this.levelcolor.forEach((color, index) => {
                var dashOffsetY = lineOffsetY - timelineWidth / 2 - ((index + 1) * distanceFromLine); // 计算每条虚线的Y位置
                svg.append('line')
                    .attr('class', 'level-line')
                    .attr('data-level', color)
                    .attr('x1', scale(0)) // 根据需要调整X1
                    .attr('y1', dashOffsetY)
                    .attr('x2', scale(1)) // 根据需要调整X2，这里假设虚线覆盖整个图表宽度
                    .attr('y2', dashOffsetY)
                    .attr('stroke', color)
                    .style('opacity', 0.2)
                    .attr('stroke-width', dashlineStroke)
                    .attr('stroke-dasharray', '5,5'); // 这里定义虚线的样式，'5,5'表示线段和间隔都是5像素
            })

            // 绘制milestone
            this.milestones.forEach((milestone, index) => {

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

                this.drawFlag(milestoneSvg, { 'x': flagOffsetX, 'y': flagOffsetY }, flagColor, poleHeight, poleWidth, flagHeight, flagWidth, extendedPoleHeight)

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
                if (index + 1 < milestonesNum) {
                    maxNum = Math.floor((scale(this.milestones[index + 1]['start']) - knowledgePointsOffsetX) / 20)
                }
                this.drawKnowledgePoints(milestoneSvg, { 'x': knowledgePointsOffsetX, 'y': knowledgePointsOffsetY }, maxNum, milestone['subknowledge'])

            });

            // 添加交互
            // 对于每个flag和level虚线，添加mouseover和mouseout事件监听器
            svg.selectAll('.flag')
                .on('mouseover', function (event, d) {
                    // 增加flag和对应level虚线的透明度
                    var currentLevel = d3.select(this).attr('data-level');
                    d3.selectAll('.flag[data-level="' + currentLevel + '"]').style('opacity', 0.9);
                    d3.selectAll('.level-line[data-level="' + currentLevel + '"]').style('opacity', 0.9);
                })
                .on('mouseout', function (event, d) {
                    // 恢复flag和对应level虚线的透明度
                    var currentLevel = d3.select(this).attr('data-level');
                    d3.selectAll('.flag[data-level="' + currentLevel + '"]').style('opacity', 0.4);
                    d3.selectAll('.level-line[data-level="' + currentLevel + '"]').style('opacity', 0.3);
                });





        },

        // 绘制flag
        drawFlag(svg, position, color, poleHeight, poleWidth, flagWidth, flagHeight, extendedPoleHeight) {
            // 绘制旗杆
            svg.append('rect')
                .attr('data-level', color)
                .attr('class', 'flag')
                .attr('x', position.x)
                .attr('y', position.y)
                .attr('width', poleWidth)
                .attr('height', poleHeight)
                .attr('fill', color)
                .style('opacity', 0.4);

            svg.append('rect')
                .attr('data-level', color)
                .attr('class', 'flag')
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
                        console.log(knowledge)
                        console.log(knowledge.level)
                        console.log(this.levelcolor)
                        circleColor = this.levelcolor[knowledge.level - 1]
                    }
                    svg.append('circle')
                        .attr('cx', x + (index * (2 * circleRadiusBase + circleSpacingBase))) // 计算每个圆圈的x位置
                        .attr('cy', y) // y位置保持不变
                        .attr('r', radius) // 设置圆圈半径
                        .style('fill', circleColor); // 设置填充颜色，你可以根据需要调整
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
    }
}
</script>
  
<style>
#learningpath-area {
    width: 100%;
    height: 90%;
}
</style>
 