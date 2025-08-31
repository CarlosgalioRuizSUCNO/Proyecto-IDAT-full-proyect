import { createRouter, createWebHistory } from 'vue-router'
import Inicio from '../views/Inicio.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  linkActiveClass: "active",
  routes: [
    {
      path: '/',
      name: 'inicio',
      component: () => import("../views/Inicio.vue"),
    },
    {
      path: "/productos",
      name: "productos",
      component: () => import("../views/Productos.vue"),
    },
    {
      path: "/creador",
      name: "creador",
      component: () => import("../views/Creador.vue"),
    },
    {
      path: "/contacto",
      name: "contacto",
      component: () => import("../views/Contacto.vue"),
    },
  ],
})

export default router
