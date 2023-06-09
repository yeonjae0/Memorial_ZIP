<template>
  <div id='loginview'>
    <img src="@/assets/logov3.png" alt="" style='width: 450px'>
    <br>
    <img src="@/assets/Login.png" alt="" style='width: 100px'>
<br>
    <hr>
    <br>
    <form @submit.prevent="login" id='login_form'>
      <div class="form-element">
      <input type="text" placeholder="username" v-model="username">
      </div>
    <br>
    <div class="form-element">
      <input type="password" placeholder="password"  v-model="password">
    </div>
    <br>
    <div class="form-element">
      <input type="submit" value="logIn">
  </div>
    </form>
    <router-link :to="{name:'SignUpView'}">signup</router-link>
  </div>
</template>

<script>
export default {
  name: 'LogIn',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password
      const payload = {
        username, password
      }
      this.$store.dispatch('login', payload)
    }
  }
}
</script>

<style>

  .form-element input[type="text"],
  .form-element input[type="password"],
  .form-element input[type="submit"] {
    box-sizing: border-box;
    width: 30%;
    /* 둥근 정도 */
    border-radius: 9px; 
    padding: 10px;
    border: none;
    outline: none;
    border: 1px solid #ccc;
  }

  .form-element input[type="submit"] {
    background-color: gray;
    color: #fff;
    cursor: pointer;
    transition: background-color 0.3s;
  }

  .form-element input[type="submit"]:hover {
    background-color: rgb(182,89,76);
  }

</style>