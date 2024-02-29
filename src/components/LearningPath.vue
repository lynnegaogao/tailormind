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
            const height = 370;
            const offsetX = 35;
            const offsetY = 10;
            const lineOffsetY=height/3*2
            const timelineWidth = 30;
            const firstFlagOffsetX = 10;

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
                .attr('y1', lineOffsetY )
                .attr('x2', scale(1))
                .attr('y2', lineOffsetY)
                .attr('stroke', '#ddd4c16a')
                .attr('stroke-width', timelineWidth);

            var allMilestoneSvg = svg.append('g')
                .attr('transform', `translate(${firstFlagOffsetX},0)`)
                .attr('width', width)
                .attr('height', height)
                

            console.log(milestones)
            // 绘制milestone
            milestones.forEach((milestone) => {

                var milestoneSvg = allMilestoneSvg.append('g')
                    .attr('id', `${milestone["milestone"]}`)
                    .attr('x', scale(milestone['start']))
                    .style('opacity',0.5)

                var poleHeight=milestone["level"]*25
                var poleWidth=3
                var flagHeight=30
                var flagWidth=20
                var flagOffsetX=scale(milestone['start'])
                var flagOffsetY=lineOffsetY-timelineWidth/2-poleHeight
                var flagColor=this.levelcolor[milestone["level"] - 1]

                this.drawFlag(milestoneSvg,{'x':flagOffsetX,'y':flagOffsetY},flagColor,poleHeight,poleWidth,flagHeight,flagWidth)
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
        drawFlag(svg, position, color, poleHeight, poleWidth, flagWidth, flagHeight) {
            // 绘制旗杆
            svg.append('rect')
                .attr('x', position.x)
                .attr('y', position.y)
                .attr('width', poleWidth)
                .attr('height', poleHeight)
                .attr('fill', color);
            const offeseX=2
            // 绘制旗帜的三角形
            svg.append('polygon')
                .attr('points', `${offeseX+position.x + poleWidth},${position.y} 
                         ${offeseX+position.x + poleWidth},${position.y + flagHeight} 
                         ${offeseX+position.x + poleWidth + flagWidth},${position.y + flagHeight / 2}`)
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
 