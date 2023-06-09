<template>
<div id='Profile'>
    <br>
    <h1>{{ userInfo.username }}의 프로필</h1>
    <p>{{ userInfo.id }}</p>
    
    <p>{{ userInfo.email }}</p>

    <button @click="toggleFollow" v-if="userID != this.$store.state.userInfo.id">
      {{ isFollowing ? '언팔로우' : '팔로우' }}
    </button>

    <p>followers: {{ followersCount }} | following: {{ followingsCount }}</p>
    <button @click="logout">로그아웃</button>
    
    <!-- <div v-if="user.username != person">
    </div> -->


  
  <!-- <div v-for="(image, index) in imageList" :key="index">
    <div class="box" :style="{ background: selectedImage === image ? '#FF0000' : '#BDBDBD' }">
      <img :src="image.pfUrl" alt="Profile Image" @click="selectProfileImage">
    </div> -->
  <!-- <button @click="selectProfileImage">사진 선택</button> -->
  <!-- </div>
  <div class="selected-profile" v-if="selectedImage">
      <h3>선택한 프로필 사진</h3>
      <div class='box' style='background: #BDBDBD'>
      <img :src="selectedImage.pfUrl" alt="Selected Profile Image">
      </div>
    </div> -->

  
</div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
name: 'ProfileView',
data() {
    return {
      // imageList: [
      //   {pfUrl: require("@/assets/images/페스티벌커비.jpg")},
      //   {pfUrl: require("@/assets/images/샌드커비.jpg")},
      //   {pfUrl: require("@/assets/images/건담커비.jpg")},
      //   {pfUrl: require("@/assets/images/스톤커비.jpg")},
      //   {pfUrl: require("@/assets/images/기본커비.png")},

      // ], // 서버로부터 받아온 이미지 목록  // 아니면 그냥 넣어주기?
    // selectedImage : null,  
    userID: this.$route.params.id,  // 현재 프로필 화면의 유저
    userInfo: null,                 // 현재 프로필 화면 유저 정보
    followersCount: 0,
    followingsCount: 0,
    isFollowing: null, // 팔로우 유무를 결정할 boolean
    };
  },
created() {
  this.userProfile()
  axios({
        method: "POST",
        url: `${API_URL}/accounts/relations/${this.userID}/follow/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
      })
      .then((response) => {
        this.isFollowing = response.data.is_followed
        this.followersCount = response.data.followers_count
        this.followingsCount = response.data.followings_count
      })
      .catch(() => {
        console.log('error')
        this.$router.push({name : 'ProfileView', params: {id: this.userID}})
      })

  },
// mounted() {
//   this.toggleFollow()
// },
methods: {
  userProfile() {
    axios({
        method: 'GET',
        url: `${API_URL}/accounts/relations/profile/${this.userID}/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
      })
      .then((response) => {
        this.userInfo = response.data
        console.log(this.userInfo)
      })
      .catch(() => {
        this.$router.push({ name: 'IndexPageView'})
      })
    },
    toggleFollow() {
      axios({
        method: "POST",
        url: `${API_URL}/accounts/relations/${this.userID}/follow/`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
      })
      .then((response) => {
        this.isFollowing = response.data.is_followed
        this.followersCount = response.data.followers_count
        this.followingsCount = response.data.followings_count
      })
      .catch(() => {
        console.log('error')
        this.$router.push({name : 'ProfileView', params: {id: this.userID}})
      })
    },
    logout() {
      window.localStorage.clear()
      this.$store.state.userInfo = null
      this.$store.state.token = null
      this.$router.push({ name: 'home' })
      this.$router.go()
    },
  },
}
</script>

<style>
img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.box {
    width: 150px;
    height: 150px; 
    border-radius: 70%;
    overflow: hidden;
}

.selected {
  border: 2px solid red;
}
</style>