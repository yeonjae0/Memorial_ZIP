<template>
  <div class="movie">
    <h1>다른 사람들은 뭘 볼까?</h1>
<!-- <img alt="Vue logo" src="../assets/logo.png"> -->

    <!-- {{ movieFn }} -->
    <carousel :autoplay="true" :loop="true">
      <slide v-for="(movie, index) in PopularmovieFn" :key="index">
    <!-- <div class="container-fluid" > -->
    <PopularMovieCard :movie="movie"/>
    </slide>
      </carousel>
    </div>
</template>

<script>
import PopularMovieCard from '@/components/PopularMovieCard.vue'
import { Carousel, Slide } from 'vue-carousel'

export default {
  name: 'PopularMovieView',
  components: {
    Carousel,
    Slide,
    PopularMovieCard
  },
//   data(){
//     return{
//       // tmdbKey: null,
//       // movieData: null,
//     }
//   },
  created() {
    this.getPopularMovies()
  },
  methods: {
    getPopularMovies(){
      this.$store.dispatch('getPopularMovies')
    }
  },
  computed: {
    PopularmovieFn(){
      return this.$store.state.Pmovies?.results
    }
  }

}
</script>
<style>

.movie {
  display: flex;
  flex-direction: column;
}

.movie-cards {
  display: flex;
  flex-direction: row;
}

</style>
