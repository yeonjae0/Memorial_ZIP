<template>
  <!-- <div class="movie"> -->
  <div>
    <h1>최신영화를 보여드림</h1>
    <!-- <div class="container-fluid"> -->
    <!-- <div class="[]">
      <div class="col-12">
        <div class="card-deck"> -->
<!-- <img alt="Vue logo" src="../assets/logo.png"> -->

    <!-- {{ movieFn }} -->
    <!-- <div class="row row-cols-1 row-cols-md-8 g-2 " > -->
    <!-- <div id="carouselExampleDark" class="carousel carousel-dark slide" data-bs-ride="carousel"> -->
    <!-- <carousel :autoplay="true" :loop="true"> -->
      <carousel :autoplay="true" :loop="true">
        <slide v-for="(movie, index) in movieFn" :key="index">
          <!-- <div class="row no-gutters"> -->
          <!-- <div class="movie-cards" > -->
            <NewMovieCard :movie="movie"/>
            <!-- </div> -->
          <!-- </div> -->
        </slide>
      </carousel>
          <!-- </div>
          </div>
          </div>
          </div> -->
    <!-- </carousel> -->
    </div>

  <!-- </div> -->
</template>

<script>
// npm i vue-carousel
import NewMovieCard from '@/components/NewMovieCard.vue'
import { Carousel, Slide } from 'vue-carousel'
// import { mapGetters } from 'vuex'

export default {
  name: 'NewMovieView',
  components: {
    Carousel,
    Slide,
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
  },
  // computed: {
  //   ...mapGetters(['movies']),
  //   movieFn() {
  //     // console.log(1111111111111)
  //     return this.movies?.results || []
  //   }
  // },
  mounted(){
    // console.log(this.movieFn)
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
