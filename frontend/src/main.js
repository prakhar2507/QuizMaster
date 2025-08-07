import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'

import { createRouter, createWebHistory } from 'vue-router'
import Login from './components/Login.vue'
import Register from './components/Register.vue'
import Landing from './components/Landing.vue'
import AuthLayout from './layouts/AuthLayout.vue'

const routes = [
  {
    path: '/',
    component: Landing,
  },
  {
    path: '/login',
    component: AuthLayout,
    children: [
      { path: '', component: Login }
    ],
  },
  {
    path: '/register',
    component: AuthLayout,
    children: [
      { path: '', component: Register }
    ],
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

createApp(App).use(router).mount('#app')