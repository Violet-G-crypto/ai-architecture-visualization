<template>
    <div class="search-root">
      <h2>Search</h2>
  
      <input
        v-model="keyword"
        class="search-input"
        placeholder="输入建筑名称进行搜索"
      />
  
      <button class="btn" @click="search">
        搜索
      </button>
  
      <section v-if="result" class="result">
        <h3>AI 搜索结果</h3>
        <p>{{ result }}</p>
      </section>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const keyword = ref('')
  const result = ref('')
  
  function search() {
    if (!keyword.value) return
  
    // ⚠️ 这里后期直接换成 AI 接口
    result.value =
      `关于「${keyword.value}」的分析结果：该建筑在结构、功能与审美层面具有重要历史价值。`
  }
  </script>
  
  <style scoped>
  .search-root {
    height: 100%;
    padding: 24px;
    box-sizing: border-box;
  }
  
  .search-input {
    width: 100%;
    padding: 10px;
    margin: 16px 0;
  }
  
  .btn {
    padding: 8px 16px;
    margin-bottom: 16px;
  }
  
  .result {
    background: #f8fafc;
    padding: 16px;
    border-left: 4px solid #6366f1;
  }
  </style>