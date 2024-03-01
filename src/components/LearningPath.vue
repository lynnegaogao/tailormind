<template>
    <div ref="LearningPath" id="learningpath-area">
    </div>
</template>
  
<script>
import * as d3 from "d3";
import milestones from './LearningPathData.json'

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
            const height = 450;
            const offsetX = 35;
            const offsetY = 10;
            const lineOffsetY = height / 3 * 2
            const timelineWidth = 30;
            const firstFlagOffsetX = 10;
            const distanceFromLine = 35;
            const extendedPoleHeight=timelineWidth +40

            // 创建SVG元素
            const svg = d3.select('#learningpath-area').append('svg')
                .attr('width', width)
                .attr('height', height)
                .attr('transform', `translate(${offsetX},${offsetY})`);

            // 定义比例尺
            const scale = d3.scaleLinear()
                .domain([0, 1])
                .range([0, width]);

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
                var dashOffsetY = lineOffsetY - ((index + 1) * distanceFromLine); // 计算每条虚线的Y位置
                svg.append('line')
                    .attr('x1', scale(0)) // 根据需要调整X1
                    .attr('y1', dashOffsetY)
                    .attr('x2', scale(1)) // 根据需要调整X2，这里假设虚线覆盖整个图表宽度
                    .attr('y2', dashOffsetY)
                    .attr('stroke', color)
                    .style('opacity', 0.2)
                    .attr('stroke-width', 2)
                    .attr('stroke-dasharray', '5,5'); // 这里定义虚线的样式，'5,5'表示线段和间隔都是5像素
            }

            )
            console.log(milestones)

            // 绘制milestone
            milestones.forEach((milestone) => {

                var milestoneSvg = allMilestoneSvg.append('g')
                    .attr('id', `${milestone["milestone"]}`)
                    .attr('x', scale(milestone['start']))
                    .style('opacity', 0.5)

                var flagHeight = 30
                var flagWidth = 20
                var poleHeight = milestone["level"] * distanceFromLine - flagWidth / 4
                var poleWidth = 3
                var flagOffsetX = scale(milestone['start'])
                var flagOffsetY = lineOffsetY - timelineWidth / 2 - poleHeight
                var flagColor = this.levelcolor[milestone["level"] - 1]

                this.drawFlag(milestoneSvg, { 'x': flagOffsetX, 'y': flagOffsetY }, flagColor, poleHeight, poleWidth, flagHeight, flagWidth,extendedPoleHeight)
                // milestoneSvg.append('line')
                //     .attr('x1', 0)
                //     .attr('y1', 0)
                //     .attr('x2', 0)
                //     .attr('y2', milestone["level"])
                //     .attr('stroke', this.levelcolor[milestone["level"] - 1])
                //     .attr('stroke-width', 5);
                // 可以根据需要添加文本
                // svg.append('text')
                //     .attr('x', scale(milestone["start"]))
                //     .attr('y', height / 2 - timelineWidth / 2)
                //     .attr('text-anchor', 'left')
                //     .text(`${milestone["milestone"]}`);
            });




        },

        // 绘制flag + knowledge points
        drawFlag(svg, position, color, poleHeight, poleWidth, flagWidth, flagHeight,extendedPoleHeight) {
            // 绘制旗杆
            svg.append('rect')
                .attr('x', position.x)
                .attr('y', position.y)
                .attr('width', poleWidth)
                .attr('height', poleHeight)
                .attr('fill', color);

            svg.append('rect')
                .attr('x', position.x)
                .attr('y', position.y+poleHeight)
                .attr('width', poleWidth)
                .attr('height', extendedPoleHeight)
                .attr('fill', color);
            const offeseX = 2
            // 绘制旗帜的三角形
            svg.append('polygon')
                .attr('points', `${offeseX + position.x + poleWidth},${position.y} 
                         ${offeseX + position.x + poleWidth},${position.y + flagHeight} 
                         ${offeseX + position.x + poleWidth + flagWidth},${position.y + flagHeight / 2}`)
                .attr('fill', color);
        }
    }
}
</script>
  
<style>
#learningpath-area {
    width: 100%;
    height: 90%;
}
</style>
 