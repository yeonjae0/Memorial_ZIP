<template>
  <div class="movie">
    <h1>따끈따끈한 최신 영화가 궁금하다면?</h1>
<!-- <img alt="Vue logo" src="../assets/logo.png"> -->

    <!-- {{ movieFn }} -->
    <div class="row row-cols-1 row-cols-md-8 g-2 " >
    <NewMovieCard v-for="(movie, index) in movieFn" :key="index" :movie="movie"/>
    </div>
  </div>
</template>

<script>


import NewMovieCard from '@/components/NewMovieCard.vue'

export default {
  name: 'NewMovieView',
  components: {
    NewMovieCard
  },
  data(){
    return{
      // tmdbKey: null,
      // movieData: null,
    }
  },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies(){
      this.$store.dispatch('getLatestMovies')
    }
  },
  computed: {
    movieFn(){
      return this.$store.state.movies?.results
    }
  }

}
</script>
<style>
</style>
