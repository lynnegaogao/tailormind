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
            const width = 1000;
            const height = 460;
            const offsetX = 60;
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
                .range([0, width - 200]);

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
                if (index + 1 < milestonesNum) {
                    maxNum = Math.floor((scale(this.milestones[index + 1]['start']) - knowledgePointsOffsetX) / 20)
                }
                this.drawKnowledgePoints(milestoneSvg, { 'x': knowledgePointsOffsetX, 'y': knowledgePointsOffsetY }, maxNum, milestone['subknowledge'])

            });

            // 添加交互
            // 对于每个flag和level虚线，添加mouseover和mouseout事件监听器
            const milestones = this.milestones
            const levelcolor = this.levelcolor
            svg.selectAll('.flag')
                .on('mouseover', function (event, d) {
                    // 增加flag和对应level虚线的透明度
                    var currentLevel = d3.select(this).attr('data-level');
                    d3.selectAll('.flag[data-level="' + currentLevel + '"]').style('opacity', 0.9);
                    d3.selectAll('.level-line[data-level="' + currentLevel + '"]').style('opacity', 0.9);

                    // 解析当前hover的milestone ID来获取subKnowledge
                    var milestoneIndex = this.id.split('-')[1];
                    var hoveredMilestones = milestones[milestoneIndex].subknowledge;

                    // 创建tooltip组
                    var tooltipOffsetX = event.pageX - 970
                    var tooltipOffsetY = event.pageY - 680
                    if (tooltipOffsetX  > 590) {
                        tooltipOffsetX = tooltipOffsetX - 300
                    }
                    if (tooltipOffsetY > 280) {
                        tooltipOffsetY = tooltipOffsetY - 200
                    }
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

                })
                .on('mouseout', function (event, d) {
                    // 恢复flag和对应level虚线的透明度
                    var currentLevel = d3.select(this).attr('data-level');
                    d3.selectAll('.flag[data-level="' + currentLevel + '"]').style('opacity', 0.4);
                    d3.selectAll('.level-line[data-level="' + currentLevel + '"]').style('opacity', 0.3);

                    // 移除tooltip组
                    svg.selectAll('.tooltip-group').remove();
                });
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
 