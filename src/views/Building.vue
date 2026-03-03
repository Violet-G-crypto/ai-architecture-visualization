<template>
    <div class="building-root">
      <h2>{{ building.name }}</h2>
  
      <section class="info">
        <p>{{ building.description }}</p>
        <ul>
          <li>朝代：{{ building.dynasty }}</li>
          <li>结构：{{ building.structure }}</li>
          <li>高度：{{ building.height }}</li>
        </ul>
      </section>
  
      <section class="ai-section">
        <h3>AI 解读</h3>
        <p>{{ aiConclusion }}</p>
      </section>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const building = ref({
    name: '应县木塔',
    dynasty: '辽',
    structure: '木构架',
    height: '67.31 米',
    description:
      '应县木塔是现存最高、最古老的纯木结构楼阁式建筑，体现了高超的结构工程技术。'
  })
  
  const aiConclusion = ref(
    '该建筑在抗震结构、材料利用和空间组织方面具有极高的工程价值，是古代建筑智慧的集中体现。'
  )
  </script>
  
  <style scoped>
  .building-root {
    height: 100%;
    padding: 24px;
    box-sizing: border-box;
  }
  
  .info {
    margin-bottom: 24px;
  }
  
  .ai-section {
    background: #f1f5f9;
    padding: 16px;
    border-left: 4px solid #10b981;
  }
  </style>