<template>
  <div>
    <h1>제목: {{ page.title }} | 작성자: {{ page.user.username }} </h1>
    <router-link :to="{ name: 'ProfileView', params: {id: page.user.pk}}">{{ page.user.username }}의 프로필</router-link> | 
    

    <i @click="toggleLikes" 
    :class="[isLiked ? 'bi bi-heart-fill': 'bi-heart']" 
    style="font-size:3rem; color: red; cursor: pointer;"></i>
    좋아요 : {{ likesCount }}개

    <br>
    <div v-if="page.user.pk === loginedUser">
      <button @click="pageDelete">삭제하기</button>
    </div>
    <div class="container text-center">
      <div class="row">
        <div class="col-7">
          <div style="margin-left: 100px">
            <div style="width: 300px;" v-html="page.content"></div>
          </div>
        </div>
        <div class="col-5"></div>
      </div>
      <div class="row"></div>
    </div>
  </div>
</template>



<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailPageView',
  data() {
    return {
      pageID: this.$route.params.id,
      page: null,
      loginedUser: this.$store.state.userInfo.id,
      isLiked: null,  // 좋아요 유무 확인을 위한 boolean
      likesCount: 0,  // 좋아요 개수
      
    }
  },

  created() {
    console.log('디테일 마운티드')
    this.pageDetail()
    console.log('111111111111111')
    console.log(this.pageID)
    console.log(this.page)
    this.toggleLikes()
    console.log('222222222222222')
  },
  methods: {
    pageDetail() {
      axios({
        method: 'GET',
        url: `${API_URL}/api/v1/pages/${this.pageID}/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
      })
      .then((response) => {
        this.page = response.data
        console.log(this.page, 'page')
      })
      .catch(() => {
        this.$router.push('IndexPageView')
      })
    },
    toggleLikes() {
      axios({
        method: 'POST',
        url: `${API_URL}/api/v1/pages/${this.pageID}/likes/`,
         headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
      })
      .then((response) => {
        this.isLiked = response.data.is_liked
        this.likesCount = response.data.likes_count
      })
    },
    pageDelete() {
      axios({
        method: 'DELETE',
        url: `${API_URL}/api/v1/pages/${this.pageID}/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
      })
      .then(() => {
        alert('페이지가 삭제되었습니다!')     
        this.$router.push({ name: 'IndexPageView' })
      })
    }
  }
}
</script>

<style>
.bi-heart{
    font-size: 30px;
    line-height: 30px;
    color:crimson;
}

.bi-heart-fill{
    font-size: 30px;
    line-height: 30px;
    color:crimson;
}
</style>