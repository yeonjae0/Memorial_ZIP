<template>
  <div>
    <br>
    <br>
      <img src="@/assets/logov3.png" alt="" style='width: 450px'>
      <br>
      <img src="@/assets/Sign Up.png" alt="" style='width: 150px'>
      <br>
      <br>
      <hr>
      <br>
    <form @submit.prevent="signUp">
      <div class="form-element">
      <input type="text" placeholder="username" v-model="username">
      </div><br>
      <!-- <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br> -->
      <div class="form-element">
      <input type="text" placeholder="email" v-model="email">
      </div><br>
      
      <div class="form-element">
      <input type="password" placeholder="password1" v-model="password1">
      </div><br>

      <div class="form-element">
      <input type="password" placeholder="password2" v-model="password2">
      </div><br>

      <div class="form-element">
      <input type="submit" value="SignUp">
      </div>

    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      email: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const email = this.email
      const password1 = this.password1
      const password2 = this.password2
      const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/
      
      if (!emailRegex.test(this.email)) {
        // 이메일 형식 유효성 검사
        alert('유효하지 않은 이메일입니다')
      } else if (this.password1 != this.password2) {
        alert('비밀번호가 서로 다릅니다')
      } else {
        const payload = {
          username, email, password1, password2
        }
        this.$store.dispatch('signUp', payload)
      }
    }
  }
}
</script>
