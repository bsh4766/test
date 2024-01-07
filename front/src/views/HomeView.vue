!<template>
  <div>
    <h1>TEST</h1>
    <h5>count : {{ count }}</h5>
    <button class="btn btn-primary" @click="add">+1</button>
    <br>
    <br>
    <button class="btn btn-danger" @click="reset">reset</button>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useCounterStore } from '@/stores/counter';
import axios from 'axios'


const count = ref(0)
const store = useCounterStore()

const add = function() {
  axios({
        method: 'POST',
        url: `${store.API_URL}/account/test/`,
    })
    .then((response) => {
      count.value = response.data.data
    })
    .catch((error) => {
        console.log(error)
    })
}

const reset = function() {
  axios({
        method: 'POST',
        url: `${store.API_URL}/account/reset/`,
    })
    .then((response) => {
      count.value = response.data.data
    })
    .catch((error) => {
        console.log(error)
    })
}



onMounted(() => {
    axios({
        method: 'GET',
        url: `${store.API_URL}/account/test/`,
    })
    .then((response) => {
      console.log(response.data)
      count.value = response.data.data
    })
    .catch((error) => {
        console.log(error)
    })
})

</script>

<style scoped>

</style>