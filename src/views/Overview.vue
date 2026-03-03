<template>
    <el-row :gutter="20">
      <!-- 左侧控制 -->
      <el-col :span="6">
        <el-card>
          <h3>选择朝代</h3>
          <el-select
            v-model="currentDynasty"
            placeholder="请选择朝代"
            style="width: 100%"
            @change="updateChart"
          >
            <el-option
              v-for="d in dynasties"
              :key="d"
              :label="d"
              :value="d"
            />
          </el-select>
  
          <el-divider />
  
          <p style="color:#666">
            AI 解读：
          </p>
          <p>{{ aiInsight }}</p>
        </el-card>
      </el-col>
  
      <!-- 右侧图表 -->
      <el-col :span="18">
        <el-card>
          <h3>建筑评分分析</h3>
          <div ref="chartRef" style="height:360px" />
        </el-card>
      </el-col>
    </el-row>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import * as echarts from 'echarts'
  
  /* ===== 假数据（之后直接换成 JSON / API） ===== */
  const dataset = {
    唐: { tech: 85, art: 88, integrity: 80, insight: '唐代建筑强调中轴对称与宏大尺度。' },
    宋: { tech: 90, art: 86, integrity: 85, insight: '宋代建筑工艺成熟，注重细部与实用性。' },
    元: { tech: 78, art: 75, integrity: 70, insight: '元代建筑融合多民族空间形制。' },
    明: { tech: 88, art: 90, integrity: 82, insight: '明代官式建筑制度化程度极高。' },
    清: { tech: 92, art: 94, integrity: 88, insight: '清代建筑在装饰与礼制上达到高峰。' }
  }
  
  const dynasties = Object.keys(dataset)
  const currentDynasty = ref('唐')
  const aiInsight = ref(dataset['唐'].insight)
  
  const chartRef = ref(null)
  let chartInstance = null
  
  /* ===== 初始化图表 ===== */
  onMounted(() => {
    chartInstance = echarts.init(chartRef.value)
    renderChart()
  })
  
  /* ===== 渲染 / 更新 ===== */
  function renderChart () {
    const d = dataset[currentDynasty.value]
  
    chartInstance.setOption({
      tooltip: {},
      xAxis: {
        type: 'category',
        data: ['技术', '艺术', '完好度']
      },
      yAxis: {
        type: 'value',
        max: 100
      },
      series: [
        {
          type: 'bar',
          data: [d.tech, d.art, d.integrity],
          itemStyle: {
            color: '#5b4cdb',
            borderRadius: [6, 6, 0, 0]
          }
        }
      ],
      animationDuration: 600
    })
  }
  
  function updateChart () {
    aiInsight.value = dataset[currentDynasty.value].insight
    renderChart()
  }
  </script>