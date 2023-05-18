<template>

    <!-- <div class="row row-cols-3 row-cols-md-3 g-4"> -->
  <div class="col-3 ">
    <div class="card card h-100">
      <img :src='`https://image.tmdb.org/t/p/original/${movie.poster_path}`' class="card-img-top" alt="...">
      <div class="card-body ">
        <h5 class="card-title crop-text-2">{{movie.title}}</h5>
        <p class="card-text">{{ movie.overview }}</p>
      </div>
    </div>
  <!-- </div> -->
  
  </div>
</template>

<script>

export default {
  name: 'TopMovieCard',
  // computed: {
  //   movieFn(){
  //     console.log(333)
  //     return console.log(this.$store.state.movies.results, 777777777)
  //   }
  // }
  props: {
    movie: Object,
  }
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
    color: rgb(19, 167, 32);
  }
</style>