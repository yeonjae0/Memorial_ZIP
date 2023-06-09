<template>
  <div>
    <!-- <h1>{{this.cardData}}</h1> -->
    <!-- <div class="text-container"> -->
    <div class='card-group '>
  <div class="card h-100 w-75 p-3 my-2" style="width: 18rem;">
      <img :src='`https://image.tmdb.org/t/p/original/${cardData?.recPaths[0]}`' class="card-img-top" alt="...">
      <div class="card-body ">
        <h5 class="card-title crop-text-2">{{cardData?.recTitles[0]}}</h5>
        <div class="text-content" :class="{ 'collapsed': isCollapsed }">
          <div v-if="isCollapsed">
          {{ truncateText(cardData?.recOverviews[0], 100) }}
        </div>
        <div v-else>
          {{ cardData?.recOverviews[0] }}
          </div>
          </div>
        <button class="more-button" @click="toggleCollapse">
          {{ isCollapsed ? '더보기' : '줄이기' }}

        </button>
      </div>
    </div>
  <div class="card h-100 w-75 p-3 my-2" >
      <img :src='`https://image.tmdb.org/t/p/original/${cardData?.recPaths[1]}`' class="card-img-top" alt="..." >
      <div class="card-body ">
        <h5 class="card-title crop-text-2">{{cardData?.recTitles[1]}}</h5>
        <div class="text-content" :class="{ 'collapsed': isCollapsed2 }">
          <div v-if="isCollapsed2">
          {{ truncateText2(cardData?.recOverviews[1], 100) }}
        </div>
        <div v-else>
          {{ cardData?.recOverviews[1] }}
          </div>
          </div>
        <button class="more-button" @click="toggleCollapse2">
          {{ isCollapsed2 ? '더보기' : '줄이기' }}
          <!-- <span v-if="isCollapsed">더보기</span>
          <span v-else>접기</span> -->
        </button>
      </div>
    </div>
    </div>
  </div>
  <!-- </div> -->
</template>

<script>
export default {
  name: 'TailoredCard',
  data() {
  return {
    isCollapsed: true,
    isCollapsed2: true,
    // text: 
  };
},
  props: {
  cardData: {
    type: Object,
    required: true,
  }
  },
  created(){
    console.log(1111111111)
    console.log(this.cardData)


  },
  methods: {
  toggleCollapse() {
    this.isCollapsed = !this.isCollapsed;
  },
  toggleCollapse2() {
    this.isCollapsed2 = !this.isCollapsed2;
  },
  truncateText(text, maxLength) {
    if (text.length <= maxLength) {
      return text;
    } else {
      return text.substring(0, maxLength) + '...';
    }
  },
  truncateText2(text, maxLength) {
    if (text.length <= maxLength) {
      return text;
    } else {
      return text.substring(0, maxLength) + '...';
    }
  },
}

}
</script>

<style>
.card-img-top {
  /* height: 15rem; */
  object-fit: cover;
}

.text-container {
  position: relative;
  max-height: 5px; /* 표시할 최대 높이 */
  overflow: hidden;
}

.text-content {
  position: relative;
}

.collapsed::after {
  content: "";
  position: absolute;
  bottom: 0;
  right: 0;
  width: 100%;
  height: 10px; /* '더보기' 버튼의 높이 */
  background: linear-gradient(transparent, white); /* 더보기 버튼이 가려지는 부분을 흰색으로 그라데이션 처리 */
}

.more-button {
  position: absolute;
  bottom: 0;
  right: 0;
  padding: 5px 10px;
  background: white;
  border: none;
  color: blue;
  cursor: pointer;
}

/* .card-text {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  display: -webkit-box;
  -webkit-line-clamp: 5;
  -webkit-box-orient: vertical;
}

.selectbtn {
  max-width: calc(100% - 38px);
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
} */
</style>