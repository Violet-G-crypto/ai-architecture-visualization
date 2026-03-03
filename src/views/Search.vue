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
  
   async function search() {
  if (!keyword.value) return

  try {
    const response = await fetch("http://127.0.0.1:8000/api/search", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        keyword: keyword.value
      })
    })

    const data = await response.json()

    if (data.success) {
      result.value = JSON.stringify(data.data, null, 2)
    } else {
      result.value = data.error
    }

  } catch (err) {
    result.value = "请求失败"
  }
}
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
