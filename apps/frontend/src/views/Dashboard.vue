<template>
  <div class="flex-container chart-container">
    <div class="datavew-inner">
        <el-card shadow="never">
          <line-chart :chart-data="datacollection"></line-chart>
        </el-card>
    </div>
  </div>
</template>

<script>
  import LineChart from '../plugins/chart'
  const axios = require('axios').create()
  export default {
    name: 'home',
    components: {
      LineChart
    },
    data () {
      return {
        datacollection: null
      }
    },
    mounted () {
      this.getChartData()
    },
    methods: {
      getChartData: async function() {
      const response = await axios.get('/api/chart')
      this.datacollection = response.data
      },
    }
  }
</script>

<style>
.chart-container {
  display: flex;
  flex-direction: row;
}

.datavew-inner {
  display: flex;
  flex-flow: column;
  padding: 22px;
  height: 100%;
  max-width: 600px;
  margin:  25px auto;
  background-color: white;
}
</style>
