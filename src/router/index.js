import { createRouter, createWebHashHistory } from 'vue-router'

import Dashboard from '../views/Dashboard.vue'
import Overview from '../views/Overview.vue'
import Building from '../views/Building.vue'
import Search from '../views/Search.vue'

const routes = [
  { path: '/', redirect: '/dashboard' },
  { path: '/dashboard', component: Dashboard },
  { path: '/overview', component: Overview },
  { path: '/building', component: Building },
  { path: '/search', component: Search }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router