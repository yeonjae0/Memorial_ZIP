import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),  // local stoarage 저장
  ],
  state: {
    token: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token
      console.log('여기까지는 오냐?')
      router.push({ name: 'home' })  
      // store/index.js $router 접근 불가 -> import 필요
    }
  },
  actions: {
    signUp(context, payload) {
      const username = payload.username
      const email = payload.email
      const password1 = payload.password1
      const password2 = payload.password2
      axios({
        method: 'POST',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, email, password1, password2
        }
      })
      .then((res) => {
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch((err) => {
        console.log('회원가입에러')
        console.log(err)
      })
    },
    login(context, payload) {
      const username = payload.username
      const password = payload.password
      axios({
        method: "POST",
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
      .then((res) => {
        console.log('login 함수')
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch((err) => {
        console.log('login 함수 에러')
        console.log(err)
      })
    }
  },
  modules: {
  }
})
