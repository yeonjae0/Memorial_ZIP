<template>
      <!-- <router-link to="/about">About</router-link> | -->
  <div id="app">
    <NavBar/>
    

    <!-- <nav>
      <router-link :to="{ name: 'home' }">Home</router-link> |
      <router-link :to="{ name: 'newmovie' }">개봉작</router-link> |
      <router-link :to="{ name: 'popularmovie' }">인기영화</router-link> |
      <router-link :to="{ name: 'tailoredmovie' }">맞춤</router-link> |
      <router-link :to="{ name: 'SignUpView' }">회원가입</router-link> |
      <router-link :to="{ name: 'LoginView' }">로그인</router-link>
      <router-link :to="{ name: 'IndexView' }">서재</router-link>
    </nav> -->
    <router-view/>
  </div>
</template>

<script>
import NavBar from '@/components/navigation-bar.vue'


export default {
  components: {
    NavBar,


  }
}

</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* background: red; */
}

nav {
  padding: 30px;
}


nav a {
  
  font-weight: bold;
  color: #50422c;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>


