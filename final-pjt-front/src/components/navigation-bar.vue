<template>
<div>
  <nav class="navbar sticky-top navbar-light">
  <!-- <nav class="navbar fixed-top navbar-light" style="background-color: rgba(128, 78, 141, 0.489);"> -->
  <div class="container-fluid">
    <router-link :to="{ name: 'home' }" class="navbar-brand">
  <img src="@/assets/logov3.png" alt="" style="width: 300px">
</router-link>

    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
  <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <router-link :to="{ name: 'newmovie' }">개봉작</router-link>
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'popularmovie' }">인기영화</router-link>
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'tailoredmovie' }">맞춤</router-link>
        </li>
        <!-- <li class="nav-item">
          <router-link :to="{ name: 'SignUpView' }">회원가입</router-link>
        </li> -->
        <!-- <li class="nav-item">
          <router-link :to="{ name: 'LoginView' }">로그인</router-link>
        </li> -->
        <li class="nav-item">
          <router-link :to="{ name: 'IndexPageView' }">인덱스페이지</router-link>
        </li>
        <li class="nav-item">
          <router-link :to="{ name: 'ProfileView' }">프로필</router-link>
        </li>
      </ul>
    </div>
  </div>
</nav>

<!-- <router-link :to="{ name: 'ProfileView', params: {id: this.$store.state.userInfo.id}}">프로필</router-link> -->
</div>
</template>

<script>
export default {
// data() {
//     return {
//       username: null,
//     };
//   },
// mounted() {
//     this.username = this.$store.state.userInfo.username;
//   },
}
</script>

<style>
.navbar {
  background: rgb(221, 142, 117);
}

</style>
