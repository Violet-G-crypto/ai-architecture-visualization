<template>
    <div class="dashboard-root">
      <!-- 顶部指标 -->
      <section class="stats">
        <div class="card">
          <div class="value">{{ stats.buildings }}</div>
          <div class="label">代表性建筑</div>
        </div>
        <div class="card">
          <div class="value">{{ stats.dynasties }}</div>
          <div class="label">主要朝代</div>
        </div>
        <div class="card">
          <div class="value">{{ stats.score }}</div>
          <div class="label">综合评分</div>
        </div>
      </section>
  
      <!-- 图表区 -->
      <section class="chart-section">
        <div ref="chartRef" class="chart"></div>
      </section>
  
      <!-- AI 总结 -->
      <section class="ai-section">
        <h3>AI 综合解读</h3>
        <p>{{ aiSummary }}</p>
      </section>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, onBeforeUnmount } from 'vue'
  import * as echarts from 'echarts'
  
  /* ===== 数据（后期可直接换接口） ===== */
  const stats = ref({
    buildings: 128,
    dynasties: 5,
    score: 87
  })
  
  const aiSummary = ref(
    '中国古代建筑在不同朝代中逐步完成制度化、技术化与审美化演进，整体呈现稳定上升趋势。'
  )
  
  /* ===== 图表 ===== */
  const chartRef = ref(null)
  let chartInstance = null
  
  const option = {
    tooltip: { trigger: 'axis' },
    grid: { left: 40, right: 20, top: 30, bottom: 30 },
    xAxis: {
      type: 'category',
      data: ['唐', '宋', '元', '明', '清']
    },
    yAxis: {
      type: 'value',
      max: 100
    },
    series: [
      {
        name: '建筑成熟度',
        type: 'line',
        smooth: true,
        data: [78, 85, 80, 90, 88],
        areaStyle: {}
      }
    ]
  }
  
  function resizeChart() {
    chartInstance && chartInstance.resize()
  }
  
  onMounted(() => {
    chartInstance = echarts.init(chartRef.value)
    chartInstance.setOption(option)
    window.addEventListener('resize', resizeChart)
  })
  
  onBeforeUnmount(() => {
    window.removeEventListener('resize', resizeChart)
    chartInstance && chartInstance.dispose()
  })
  </script>
  
  <style scoped>
  .dashboard-root {
    height: 100%;
    padding: 24px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    gap: 24px;
  }
  
  .stats {
    display: flex;
    gap: 16px;
  }
  
  .card {
    flex: 1;
    background: #f1f5f9;
    padding: 16px;
    text-align: center;
    border-radius: 8px;
  }
  
  .value {
    font-size: 28px;
    font-weight: bold;
  }
  
  .chart-section {
    background: #ffffff;
    border-radius: 8px;
    padding: 16px;
  }
  
  .chart {
    width: 100%;
    height: 320px;
  }
  
  .ai-section {
    background: #f8fafc;
    border-left: 4px solid #3b82f6;
    padding: 16px;
  }
  </style>