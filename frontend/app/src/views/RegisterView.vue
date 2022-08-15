<template>
  <form class="d-flex align-items-center justify-content-center flex-column mx-5" @submit.prevent>
    <h2 class="fw-bold">Registration</h2>
    <div class="form-group my-3">
        <label for="username">Username</label>
        <input v-model="username" type="text" name="username" id="username" placeholder="Username" class="form-control">
    </div>
    <div class="form-group my-3">
      <label for="password">Password</label>
        <input v-model="password" type="password" name="password" id="password" placeholder="Password" class="form-control">
    </div>
    <input type="submit" value="Login" class="btn btn-success fw-bold" @click="makeRegistration">
    <button class="btn btn-warning my-3" @click="() => $router.push('/login')">Login</button>
    <p v-if="isError" class="my-5">There was an error while registering the user</p>
  </form>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import httpService from '../api/http';

export default defineComponent({
    name:"RegisterView",
    data: () => ({
        username:"",
        password:"",
        isError:false,
    }),
    methods:{
      makeRegistration() {
        let formData = new FormData();
        formData.append("username", this.username);
        formData.append("password", this.password);
        httpService.userRegistration(formData).then(response => {
            this.$router.push("/login");
        }).catch(() => (this.isError = true))
      }
    }
})
</script>

<style lang="scss" scoped>

</style>