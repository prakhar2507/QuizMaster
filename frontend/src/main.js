import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import Swal from "sweetalert2";
import "sweetalert2/dist/sweetalert2.min.css";

import { createRouter, createWebHistory } from 'vue-router'
import Login from './components/Login.vue'
import Register from './components/Register.vue'
import Landing from './views/Landing.vue'
import AuthLayout from './layouts/AuthLayout.vue'
import NotFoundPage from './views/NotFound.vue';

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
  { 
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: NotFoundPage
  }
]

const swal = Swal.mixin({
  confirmButtonColor: "#000000",
  cancelButtonColor: "#555555",
  background: "#ffffff",
  color: "#000000",
});

const router = createRouter({
  history: createWebHistory(),
  routes,
})

const app = createApp(App);
app.config.globalProperties.$swal = swal;

app.use(router);
app.mount("#app");