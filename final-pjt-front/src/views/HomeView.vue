<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <br>
    <HelloWorld msg="당신의 경험을 디자인하세요"/>
    <hr>
    <div v-if="this.$store.getters.isLogin===true">
    <h3>안녕하세요 {{this.$store.state.userInfo.username}}님</h3>
    </div>
    <div v-else>
    <LogIn />
    </div>

  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import LogIn from '@/components/LogIn.vue'

import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'HomeView',
  components: {
    HelloWorld,
    LogIn,
  },
  mounted() {
    if (this.$store.getters.isLogin) {
      console.log(this.$store.getters.isLogin)
      this.logined_user()
    }
  },
  methods: {
    logined_user() {
      axios({
        method: 'GET',
        url: `${API_URL}/accounts/relations/userinfo/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
      .then((response) => {
        this.$store.dispatch('logined_user', response.data)
      })
      .catch(() => {
        this.$router.push({name : 'NotFound404'})
      })
    },
  }
}
</script>