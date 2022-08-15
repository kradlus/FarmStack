<template>
    <div class="container d-flex justify-content-center">
        {{ userObj.username }} {{ userObj.password}}
    </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
    name:"UserComponent",
    props: {
        userObj:{
            type:Object,
            required:true
        },
    },
})
</script>
<style lang="scss" scoped>
</style>