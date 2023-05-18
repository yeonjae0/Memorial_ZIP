<template>
  <div class="movie">
    <h1>음... 이건 봐야해</h1>
<!-- <img alt="Vue logo" src="../assets/logo.png"> -->

    <!-- {{ movieFn }} -->
    <div class="row row-cols-1 row-cols-md-8 g-2 " >
    <!-- <MovieCard v-for="(movie, index) in movieFn" :key="index" :movie="movie"/> -->
    <TopMovieCard />
    </div>
  </div>
</template>

<script>
// 여기 수정 필요


import TopMovieCard from '@/components/TopMovieCard.vue'

export default {
  name: 'TopMovieView',
  components: {
    TopMovieCard
  },
//   data(){
//     return{
//       // tmdbKey: null,
//       // movieData: null,
//     }
//   },
//   created() {
//     this.getMovies()
//   },
//   methods: {
//     getMovies(){
//       this.$store.dispatch('getLatestMovies')
//     }
//   },
//   computed: {
//     movieFn(){
//       return this.$store.state.movies?.results
//     }
//   }

}
</script>
<style>
</style>
