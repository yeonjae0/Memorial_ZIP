import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(), // local storage에 저장 
  ],
  state: {
    movies: null,
    token: null, // 회원가입, 로그인 등 토큰 저장해 두는 변수
    userInfo: null,  // 현재 로그인한 사람 정보
    genreList : [],
    Pmovies: null,

  },
  getters: {
    isLogin(state) {  // 로그인 여부 확인해 주는 함수
      return state.token ? true : false
    }
  },
  mutations: {
  GET_LATEST_MOVIES(state, movies){
    state.movies = movies
  }, 
  GET_Popular_MOVIES(state, Pmovies){
    state.Pmovies = Pmovies
  },
  SAVE_TOKEN(state, token) {
    state.token = token
    console.log(token, 'SAVE_TOKEN!!!!!!!!!')
    router.go()
    // store/index.js $router 접근 불가 -> import 필요
  },
  SAVE_INFO(state, data) {
    state.userInfo = data
  },
  GET_GENRE_LIST(state, genreList) {
    state.genreList = genreList
    console.log(state.genreList, 'mutations')
  },

},
actions: {
  getLatestMovies(context){  // API 호출해서 데이터 state에 넘겨주는 함수
    console.log('getLatestMovies (vuex)')
    const key_API = process.env.VUE_APP_KEY
  axios({
    method:'get',
    url:`https://api.themoviedb.org/3/movie/now_playing?api_key=${key_API}&language=ko-KR&page=1`
  })
  .then((res) => {
    context.commit('GET_LATEST_MOVIES', res.data)
  })
  },
  getPopularMovies(context){  // API 호출해서 데이터 state에 넘겨주는 함수
    console.log('getPopularMovies (vuex)')
    const key_API = process.env.VUE_APP_KEY
  axios({
    method:'get',
    url:`https://api.themoviedb.org/3/movie/popular?api_key=${key_API}&language=ko-KR&page=1&include_adult=false'`
  })
  .then((res) => {
    context.commit('GET_Popular_MOVIES', res.data)
  })
  },
  // async GENRE_LIST()
  signUp(context, payload) {
    axios({
      method: 'POST',
      url: `${API_URL}/accounts/signup/`,
      data: payload
    })
    .then(() => {
      window.localStorage.clear()
      router.push({name: 'home'})
    })
    .catch((err) => {
      console.log('회원가입에러')
      console.log(err)
    })
  },
  login(context, payload) {
    axios({
      method: "POST",
      url: `${API_URL}/accounts/login/`,
      data: payload
    })
    .then((res) => {
      console.log(res, '로그인')
      console.log(this.userInfo)
      context.commit('SAVE_TOKEN', res.data.key)
    })
    .catch((err) => {
      console.log(err)
    })
  },
  logined_user(context, data) {
    console.log('logined_user 시작!!!!!!!!!!!')
    context.commit('SAVE_INFO', data)
  },
  getGenreList(context, genrelist){
    context.commit('GET_GENRE_LIST', genrelist)
    console.log(genrelist, 'actions')
  }
  },

},

)
