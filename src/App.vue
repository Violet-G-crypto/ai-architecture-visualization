<template>
  <div class="app-root">
    <!-- 顶部导航 -->
    <header class="top-nav">
      <div class="title">🏯 AI × 中国古代建筑</div>

      <nav class="menu">
        <router-link to="/dashboard">Dashboard</router-link>
        <router-link to="/overview">Overview</router-link>
        <router-link to="/building">Building</router-link>
        <router-link to="/search">Search</router-link>
      </nav>
    </header>

    <!-- 页面内容（唯一出口） -->
    <main class="page-container">
      <router-view />
    </main>
  </div>
</template>

<style scoped>
.app-root {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
}

.top-nav {
  height: 60px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  background: #111;
  color: #fff;
}

.menu a {
  margin-left: 16px;
  color: #aaa;
  text-decoration: none;
}

.menu a.router-link-active {
  color: #fff;
  font-weight: bold;
}

.page-container {
  flex: 1;
  overflow: auto;
  background: #f5f7fa;
}
</style>