!<template>
  <div>
<RouterLink :to="{name : 'home'}">home</RouterLink>
<RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style lang="scss" scoped>

</style>