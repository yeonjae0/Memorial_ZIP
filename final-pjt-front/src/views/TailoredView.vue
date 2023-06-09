<template>
<div>
    <h1>오늘의 영화를 추천해드립니다.</h1>
    <div v-if="eventFinished" id = 'today'>
      <!-- <div class="col-md-6"> -->
        <h4>장르를 선택해주세요</h4>
        <!-- <br>
        <br> -->
      <div class="container">
      <div class="row">
      <div class="col-md-3">
        <div class="funkyradio">
          <div class="funkyradio-default">
            <input type="checkbox" name="checkbox" id="checkbox1" v-model="arr" value="12" checked/>
            <label for="checkbox1">모험</label>
          </div>
          </div>
          </div>
          <div class="col-md-3">
          <div class="funkyradio">
          <div class="funkyradio-primary">
            <input type="checkbox" name="checkbox" id="checkbox2" v-model="arr" value="14" checked/>
            <label for="checkbox2">판타지</label>
          </div>
          </div>
          </div>
          <div class="col-md-3">
          <div class="funkyradio">
          <div class="funkyradio-success">
            <input type="checkbox" name="checkbox" id="checkbox3" v-model="arr" value="16" checked/>
            <label for="checkbox3">애니메이션</label>
          </div>    
          </div>    
          </div>    
          <div class="col-md-3">
          <div class="funkyradio">
          <div class="funkyradio-warning">
            <input type="checkbox" name="checkbox" id="checkbox4" v-model="arr" value="18" checked/>
            <label for="checkbox4">드라마</label>
          </div>
          </div>
          </div>
          </div>
          <div class="row">
          <div class="col-md-3">
          <div class="funkyradio">
          <div class="funkyradio-danger">
            <input type="checkbox" name="checkbox" id="checkbox5" v-model="arr" value="27" checked/>
            <label for="checkbox5">공포</label>
          </div>
          </div>
          </div>
          <div class="col-md-3">
          <div class="funkyradio">
          <div class="funkyradio-info">
            <input type="checkbox" name="checkbox" id="checkbox6" v-model="arr" value="28" checked/>
            <label for="checkbox6">액션</label>
          </div>
          </div>
          </div>
        <div class="col-md-3">
          <div class="funkyradio">
          <div class="funkyradio-default">
            <input type="checkbox" name="checkbox" id="checkbox7" v-model="arr" value="35" checked/>
            <label for="checkbox7">코미디</label>
          </div>
          </div>
          </div>
          <div class="col-md-3">
            <div class="funkyradio">
          <div class="funkyradio-primary">
            <input type="checkbox" name="checkbox" id="checkbox8" v-model="arr" value="36" checked/>
            <label for="checkbox8">역사</label>
          </div>
          </div>
          </div>
          </div>
          <div class="row">
          <div class="col-md-3">
            <div class="funkyradio">
          <div class="funkyradio-success">
            <input type="checkbox" name="checkbox" id="checkbox9" v-model="arr" value="37" checked/>
            <label for="checkbox9">서부</label>
          </div>
          </div>
          </div>
          <div class="col-md-3">
            <div class="funkyradio">
          <div class="funkyradio-warning">
            <input type="checkbox" name="checkbox" id="checkbox10" v-model="arr" value="53" checked/>
            <label for="checkbox10">스릴러</label>
          </div>
          </div>
          </div>
          <div class="col-md-3">
            <div class="funkyradio">
          <div class="funkyradio-danger">
            <input type="checkbox" name="checkbox" id="checkbox11" v-model="arr" value="80" checked/>
            <label for="checkbox11">범죄</label>
          </div>
          </div>
          </div>
          <div class="col-md-3">
            <div class="funkyradio">
          <div class="funkyradio-info">
            <input type="checkbox" name="checkbox" id="checkbox12" v-model="arr" value="99" checked/>
            <label for="checkbox12">다큐멘터리</label>
          </div>
          </div> 
        </div>
        </div>
        <div class="row">
        <div class="col-md-3">
          <div class="funkyradio">
          <div class="funkyradio-default">
            <input type="checkbox" name="checkbox" id="checkbox13" v-model="arr" value="878" checked/>
            <label for="checkbox13">SF</label>
          </div>
          </div>
          </div>
          <div class="col-md-3">
            <div class="funkyradio">
          <div class="funkyradio-primary">
            <input type="checkbox" name="checkbox" id="checkbox14" v-model="arr" value="9648" checked/>
            <label for="checkbox14">미스터리</label>
          </div>
          </div> 
          </div> 
          <div class="col-md-3">
            <div class="funkyradio">
          <div class="funkyradio-success">
            <input type="checkbox" name="checkbox" id="checkbox15" v-model="arr" value="10402" checked/>
            <label for="checkbox15">음악</label>
          </div>
          </div>
          </div>
          <div class="col-md-3">
            <div class="funkyradio">
          <div class="funkyradio-warning">
            <input type="checkbox" name="checkbox" id="checkbox16" v-model="arr" value="10749" checked/>
            <label for="checkbox16">로맨스</label>
          </div>
          </div>
          </div>
          </div>
          <div class="row">
          <div class="col-md-3">
            <div class="funkyradio">
          <div class="funkyradio-info">
            <input type="checkbox" name="checkbox" id="checkbox17" v-model="arr" value="10751" checked/>
            <label for="checkbox17">가족</label>
          </div>
          </div>
          </div>
          <div class="col-md-3">
            <div class="funkyradio">
          <div class="funkyradio-danger">
            <input type="checkbox" name="checkbox" id="checkbox18" v-model="arr" value="10752" checked/>
            <label for="checkbox18">전쟁</label>
          </div>
          </div>
          </div>
          <div class="col-md-3">
          <div class="funkyradio">
          <div class="funkyradio-default">
            <input type="checkbox" name="checkbox" id="checkbox19" v-model="arr" value="10770" checked/>
            <label for="checkbox19">TV영화</label>
            </div>
            </div>
            </div>
          </div>
          </div>
      <!-- <input type="checkbox" v-model="arr" value="12">모험

      <input type="checkbox" v-model="arr" value="878">SF
      <input type="checkbox" v-model="arr" value="9648">미스터리
      <input type="checkbox" v-model="arr" value="10402">음악
      <input type="checkbox" v-model="arr" value="10749">로맨스
      <input type="checkbox" v-model="arr" value="10751">가족
      <input type="checkbox" v-model="arr" value="10752">전쟁
      <input type="checkbox" v-model="arr" value="10770">TV영화  -->
      <br>

      <button @click='showAlert' style="width: 18rem; background-color: #EAF0EE;">확인</button>
    <!-- </div> -->
    </div>

    <div v-else>
      <!-- <h1>{{this.cardData}}</h1> -->
      <!-- <h1>{{typyof(this.cardData)}}</h1> -->
    <TailoredCard :cardData="this.cardData" />
    <button type='button' @click='showAlert' class="btn btn-success" style="width: 18rem;" >다시 추천받기</button>
    </div>
  <!-- </div> -->
</div>
</template>

<script>
import TailoredCard from '@/components/TailoredCard.vue'
  import axios from 'axios'

// import axios from 'axios'
//  장르 3개를 선택하고 DB에서 해당 value 값에 해당하는 genre id값을 얻는다.
// 장르 별로 평점이 높은 영화를 15개씩 총 45개를 리스트에 넣는다. 
// 리스트의 중복을 제거하고 랜덤으로 3개 or 5개의 영화를 반환

export default {
  // el: '#today',
  name: 'TailoredView',
  components: {
    TailoredCard,
  },
  data(){ 
    return{  
    arr : [],
    eventFinished: true,
    cardData:{
    recTitles : null,
    recOverviews : null,
    recPaths : null,
    }
  }
  },
  methods: {
    showAlert() {
      // console.log('클릭')
      // console.log(this.arr)
      // console.log(this.arr.length)
      if (this.arr.length < 2 | this.arr.length > 2) {
        alert('2개의 체크박스를 선택해주세요')
      } else {
        // this.$store.dispatch('getGenreList', this.arr)
        axios({
          method: 'POST',
          url: `http://127.0.0.1:8000/movies/recommend/`,
          data: this.arr,
        })
        .then(response => {
          this.cardData.recTitles = [response.data.rec_lst[0][0], response.data.rec_lst[1][0]]
          this.cardData.recOverviews = [response.data.rec_lst[0][1], response.data.rec_lst[1][1]]
          this.cardData.recPaths = [response.data.rec_lst[0][2], response.data.rec_lst[1][2]]
          this.eventFinished =false
          // console.log(this.recTitles)
          // console.log('oooooooooooooooooo')
          // console.log(response)
          // console.log(response.data.rec_lst[0][0]) // 제목
          // console.log(response.data.rec_lst[0][1]) // 줄거리
          // console.log(response.data.rec_lst[0][2]) // 포스터 링크
        })
        .catch(() => {
          console.log('errrrrrrrrrrrrrrrrrr')
          console.log(this.arr)
          // console.log(response.data.rec_set)
        })

        }
      },
    },
    }






</script>

<style>

.funkyradio div {
  clear: both;
  overflow: hidden;
}

.funkyradio label {
  width: 100%;
  border-radius: 3px;
  border: 1px solid #D1D3D4;
  font-weight: normal;
}

.funkyradio input[type="radio"]:empty,
.funkyradio input[type="checkbox"]:empty {
  display: none;
}

.funkyradio input[type="radio"]:empty ~ label,
.funkyradio input[type="checkbox"]:empty ~ label {
  position: relative;
  line-height: 2.5em;
  text-indent: 3.25em;
  margin-top: 2em;
  cursor: pointer;
  -webkit-user-select: none;
    -moz-user-select: none;
      -ms-user-select: none;
          user-select: none;
}

.funkyradio input[type="radio"]:empty ~ label:before,
.funkyradio input[type="checkbox"]:empty ~ label:before {
  position: absolute;
  display: block;
  top: 0;
  bottom: 0;
  left: 0;
  content: '';
  width: 2.5em;
  background: #D1D3D4;
  border-radius: 3px 0 0 3px;
}

.funkyradio input[type="radio"]:hover:not(:checked) ~ label,
.funkyradio input[type="checkbox"]:hover:not(:checked) ~ label {
  color: #888;
}

.funkyradio input[type="radio"]:hover:not(:checked) ~ label:before,
.funkyradio input[type="checkbox"]:hover:not(:checked) ~ label:before {
  content: '\2714';
  text-indent: .9em;
  color: #C2C2C2;
}

.funkyradio input[type="radio"]:checked ~ label,
.funkyradio input[type="checkbox"]:checked ~ label {
  color: #777;
}

.funkyradio input[type="radio"]:checked ~ label:before,
.funkyradio input[type="checkbox"]:checked ~ label:before {
  content: '\2714';
  text-indent: .9em;
  color: #333;
  background-color: #ccc;
}

.funkyradio input[type="radio"]:focus ~ label:before,
.funkyradio input[type="checkbox"]:focus ~ label:before {
  box-shadow: 0 0 0 3px #999;
}

.funkyradio-default input[type="radio"]:checked ~ label:before,
.funkyradio-default input[type="checkbox"]:checked ~ label:before {
  color: #333;
  background-color: #ccc;
}

.funkyradio-primary input[type="radio"]:checked ~ label:before,
.funkyradio-primary input[type="checkbox"]:checked ~ label:before {
  color: #fff;
  background-color: #337ab7;
}

.funkyradio-success input[type="radio"]:checked ~ label:before,
.funkyradio-success input[type="checkbox"]:checked ~ label:before {
  color: #fff;
  background-color: #5cb85c;
}

.funkyradio-danger input[type="radio"]:checked ~ label:before,
.funkyradio-danger input[type="checkbox"]:checked ~ label:before {
  color: #fff;
  background-color: #d9534f;
}

.funkyradio-warning input[type="radio"]:checked ~ label:before,
.funkyradio-warning input[type="checkbox"]:checked ~ label:before {
  color: #fff;
  background-color: #f0ad4e;
}

.funkyradio-info input[type="radio"]:checked ~ label:before,
.funkyradio-info input[type="checkbox"]:checked ~ label:before {
  color: #fff;
  background-color: #5bc0de;
}

</style>