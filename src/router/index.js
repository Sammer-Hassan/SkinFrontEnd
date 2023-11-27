import { createRouter, createWebHashHistory } from 'vue-router'
import LeaderBoard from '../views/LeaderboardPage.vue'
import RatingPage from '../views/RatingPage.vue'
import About from '../views/About.vue'
const routes = [
  {
    path: '/',
    name: 'RatingPage',
    component: RatingPage
  },
  {
    path: '/LeaderBoard',
    name: 'LeaderBoard',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: LeaderBoard
  },
  {
    path:'/About',
    name: 'About',
    component: About
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
