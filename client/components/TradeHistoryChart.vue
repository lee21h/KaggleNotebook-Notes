
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