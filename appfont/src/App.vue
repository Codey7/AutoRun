<template>
  <div id="app">
    <img src="./assets/logo.png">
    <hello-world></hello-world>
    <h1>{{ msg }}</h1>
    <div class="nav-box">
            <p class="nav-list">
                <router-link class="nav-item" to="/home">首页</router-link>
                <router-link class="nav-item" to="/about">关于</router-link>
            </p>
        </div>
        <div>
            <router-view/>
        </div>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
export default {
  name: 'app',
  data () {
    return {
      msg: 'hahaha'
    }
  },
  components: {
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
