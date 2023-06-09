<template>
  <div>
    <router-link :to="{ name: 'CreatePageView' }">
      <button>CREATE</button> <br>
    </router-link>
    <br>
      <div class="row row-cols-1 row-cols-md-3 g-4">
        <div v-if="pages">
        <BookPage v-for="(page, index) in pages" 
        :key="index" :page="page"/>
      </div>
      </div>
    <hr>          
  </div>
</template>

<script>
import axios from 'axios'
import BookPage from '@/components/BookPage'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'IndexPageView',
  components: {
    BookPage,
  },
  data() {
    return {
      pages: null,
    }
  },
  created() {
    this.logined_user()
  },
  mounted() {
    this.getPages()
  },
  methods: {
    getPages() {
      axios({
        method: 'GET',
        url: `${API_URL}/api/v1/pages/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
      })
      .then((response) => {
        this.pages = response.data
        // this.$store.dispatch('enrollPage', this.pages)
      })
      .catch(() => {
        alert('작성된 페이지가 없습니다!')
        this.$router.push({name: 'CreatePageView'})
      })
    },
    logined_user() {
    // console.log('일단 들어왔다')
      axios({
        method: 'GET',
        url: `${API_URL}/accounts/relations/userinfo/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
      .then((response) => {
        this.$store.dispatch('logined_user', response.data)
        // console.log()
      })
      .catch(() => {
        this.$router.push({name : 'NotFound404'})
      })
    },
  }
}
</script>

<style>

</style>