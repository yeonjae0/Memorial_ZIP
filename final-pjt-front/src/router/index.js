import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import NewMovieView from '@/views/NewMovieView'
import PopularMovieView from '@/views/PopularMovieView'
import TailoredView from '@/views/TailoredView'
import SignUpView from '@/views/SignUpView'
// import LoginView from '@/views/LoginView'
import ProfileView from '@/views/ProfileView'
import CreatePageView from '@/views/CreatePageView'
import IndexPageView from '@/views/IndexPageView'
import DetailPageView from '@/views/DetailPageView'
import NotFound404 from '@/views/NotFound404'

Vue.use(VueRouter)

const routes = [
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404,
  },
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/newmovie',
    name: 'newmovie',
    component: NewMovieView
    // path: '/about',
    // name: 'about',
    // // route level code-splitting
    // // this generates a separate chunk (about.[hash].js) for this route
    // // which is lazy-loaded when the route is visited.
    // component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/popularmovie',
    name: 'popularmovie',
    component: PopularMovieView
  },
  {
    path: '/tailoredmovie',
    name: 'tailoredmovie',
    component: TailoredView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  // {
  //   path: '/login',
  //   name: 'LoginView',
  //   component: LoginView
  // },
  {
    path: '/profile/:id',
    name: 'ProfileView',
    component: ProfileView
  },
  {
    path: '/create',
    name: 'CreatePageView',
    component: CreatePageView
  },
  {
    path: '/pages',
    name: 'IndexPageView',
    component: IndexPageView,
  },
  {
    path: '/pages/:id',
    name: 'DetailPageView',
    component: DetailPageView,
  },
  {
    path: '*', // 위에 해당하지 않는 모든 것..
    redirect: '/404',
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
