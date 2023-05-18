<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>
      
      <label for="email">email : </label>
      <input type="text" id="email" v-model="email"><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2">
      
      <input type="submit" value="SignUp">
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
