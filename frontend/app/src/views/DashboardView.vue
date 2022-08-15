<template>
<div class="container">
  <h2 class="fw-bold">Search for users</h2>
  <form @submit.prevent>
    <div class="form-group mx-5 my-3">
      <input v-model="search" type="text" name="user" id="user" class="form-control">
    </div>
    <div class="form-group mx-5 my-3">
      <input type="submit" value="Search" @click="searchUser" class="form-control btn btn-success">
    </div>
  </form>
  <template v-if="searching">
    <div class="container">
      <h2 class="fw-bold">Searching</h2>
    </div>
  </template>
  <template v-if="!searching && Object.keys(userObj).length > 0">
    <div class="container">
      <user-component :userObj="userObj"></user-component>
    </div>
  </template>
</div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import httpService from '../api/http';
import UserComponent from '../components/UserComponent.vue';
import router from '../router';

export default defineComponent({
    name: "DashboardView",
    data: () => ({
        search: "",
        searching: false,
        userObj: {}
    }),
    created() {
      const cookie = this.$cookies.get("session");
      if (!cookie || !router.isAuthenticated(cookie)) this.$router.push("/login")
    },
    components:{
      "user-component":UserComponent,
    },
    methods: {
        searchUser() {
            const search = this.search;
            this.search = "";
            this.searching = true;
            httpService.getUser(search).then(response => {
                let user = response.data.user.user.split(" ");
                this.userObj = { "username": user[0], "password": user[1] };
            }).catch(err => {
                console.log(err);
            });
            this.searching = false;
        }
    },
});
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
