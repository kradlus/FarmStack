<template>
  <form class="d-flex align-items-center justify-content-center flex-column mx-5" @submit.prevent>
    <h2 class="fw-bold">Login</h2>
    <div class="form-group my-3">
        <label for="username">Username</label>
        <input v-model="username" type="text" name="username" id="username" placeholder="Username" class="form-control">
    </div>
    <div class="form-group my-3">
      <label for="password">Password</label>
        <input v-model="password" type="password" name="password" id="password" placeholder="Password" class="form-control">
    </div>
    <input type="submit" value="Login" class="btn btn-success fw-bold" @click="makeLogin">
    <button class="btn btn-warning my-3" @click="() => $router.push('/register')">Register</button>
    <p v-if="error !== ''">{{ error }}</p>
  </form>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import httpService from '../api/http';

export default defineComponent({
    name:"LoginView",
    data: () => ({
        username:"",
        password:"",
        error:""
    }),
    methods:{
      makeLogin() {
        let formData = new FormData();
        formData.append("username", this.username);
        formData.append("password", this.password);
        httpService.userLogin(formData).then(response => {
          this.$cookies.set("session",response.data.token)
          this.$router.push("/")
        })
          .catch(() => (this.error = "Invalid login"))
      }
    }
})
</script>

<style lang="scss" scoped>

</style>