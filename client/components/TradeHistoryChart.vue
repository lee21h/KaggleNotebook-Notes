
<template lang="pug">
section.section
  .column
    .card
      .card-content
        .content.has-text-centered
          v-chart.chart(:option='optionScatter', autoresize)
          //- chart(:options="tradesChart",
          //-       autoresize,
          //-       ref="tradesChart")
</template>
<script>
import { format } from 'date-fns'
import { use, graphic } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { ScatterChart } from 'echarts/charts'
import { TitleComponent, TooltipComponent } from 'echarts/components'
import VChart from 'vue-echarts'
// import { THEME_KEY } from 'vue-echarts'

use([CanvasRenderer, ScatterChart, TitleComponent, TooltipComponent])

export default {
  name: 'TradeHistoryChart',
  components: {
    VChart,
  },
  provide: {
    // [THEME_KEY]: 'dark',
  },
  props: {
    trades: {
      type: Array,
      required: true,
    },
  },
  data() {
    const tradesData = this.trades.map(Object.values)
    const dollarUSLocale = Intl.NumberFormat('en-US')

    return {
      optionPie: {
        title: {
          text: 'Traffic Sources',
          left: 'center',
        },
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b} : {c} ({d}%)',
        },
        legend: {
          orient: 'vertical',
          left: 'left',
          data: [
            'Direct',
            'Email',
            'Ad Networks',
            'Video Ads',
            'Search Engines',
          ],
        },
        series: [
          {
            name: 'Traffic Sources',
            type: 'pie',
            radius: '55%',
            center: ['50%', '60%'],
            data: [
              { value: 335, name: 'Direct' },
              { value: 310, name: 'Email' },
              { value: 234, name: 'Ad Networks' },
              { value: 135, name: 'Video Ads' },
              { value: 1548, name: 'Search Engines' },
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)',
              },
            },
          },
        ],
      },
      optionScatter: {
        backgroundColor: new graphic.RadialGradient(0.3, 0.3, 0.8, [
          {
            offset: 0,
            color: '#f7f8fa',
          },
          {
            offset: 1,
            color: '#cdd0d5',
          },
        ]),
        title: {
          text: 'Trades history',
          // subtext: 'Red bubble = trade size\nPurple bubble = total value',
          subtext: 'Bubble size = Total value',
          left: 'center',
          top: '5%',
          textStyle: {
            fontSize: 25,
          },
          subtextStyle: {
            fontSize: 18,