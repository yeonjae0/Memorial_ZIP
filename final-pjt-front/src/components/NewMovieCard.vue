<template>

  <!-- <div class="col-3 ">
    <div class="card card h-100">
      <img :src='`https://image.tmdb.org/t/p/original/${movie.poster_path}`' class="card-img-top" alt="...">
      <div class="card-body ">
        <h5 class="card-title crop-text-2">{{movie.title}}</h5>
        <p class="card-text">{{ movie.overview }}</p>
      </div>
    </div>
  </div> -->

  <!-- <div class='row'>
<div class="container-fluid"> -->
    <!-- <h1>{{movie}}</h1> -->
    <!-- {{ this.movie[0].poster_path }} -->
            <!-- <img :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" class="card-img-top " style="max-width: 18rem" alt="..."> -->
    <!-- <vue-carousel :autoplay="true" :loop="true"> -->
      
      <!-- <slide v-for="(movie, index) in movieFn" :key="index"> -->
        <div class="row no-gutters">
          <div class="card h-100 w-100 p-2" >
            <img :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title crop-text-2">{{ movie.title }}</h5>
              <p class="card-text">{{ movie.overview }}</p>
            </div>
          </div>
          </div>
      
    <!-- </vue-carousel> -->
  <!-- </div>
  </div> -->
  
</template>

<script>
// import { Carousel, Slide } from 'vue-carousel'

export default {
  name: 'NewMovieCard',
  // computed: {
  //   movieFn(){
  //     console.log(333)
  //     return console.log(this.$store.state.movies.results, 777777777)
  //   }
  // }
  props: {
    movie: Object,
    // movie: {
    //   type: Array,
    // }
  },
  components: {
    // Carousel,
    // Slide
  },
  created() {
    console.log('card로 왔다')
    console.log(this.movie)
  },
}
</script>

<style>
.card {
    background-color: #58c7a5
  }
  .crop-text-2 {
    -webkit-line-clamp: 2;
    overflow : hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    color: rgb(55, 81, 77);
  }

.row {
  display:flex;
  /* width: 100px;
  height: 100px; */

}
</style>