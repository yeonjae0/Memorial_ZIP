<template>
  <div>
    <div class="col">
      <div class="card">
        <div class="card-body h-100">
          <h5 class="card-title">{{ page.title }}</h5>
          <p class="card-text" v-html="page.content"></p>
          <p class="cart-footer">
            <router-link :to="{name:'DetailPageView', params:{id: page.pk}}">
              {{ page.title }}
            </router-link>
               <i @click="toggleLikes" 
                  :class="[isLiked ? 'bi bi-heart-fill': 'bi-heart']" 
                  style="font-size:1rem; color: red; cursor: pointer;"></i>
                {{likesCount}}
          </p>          
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'BookPage',
  props: {
    page: Object,
  },
  data() {
    return {
      isLiked: null,  // 좋아요 유무 확인을 위한 boolean
      likesCount: 0,  // 좋아요 개수
    }
  },
  created() {
    this.toggleLikes()
  },
  methods: {
    toggleLikes() {
      axios({
        method: 'POST',
        url: `${API_URL}/api/v1/pages/${this.page.pk}/likes/`,
         headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
      })
      .then((response) => {
        this.isLiked = response.data.is_liked
        this.likesCount = response.data.likes_count
      })
    },
  }
}
</script>

<style>
</style>