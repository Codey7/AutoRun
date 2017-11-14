import Vue from 'vue'
import Login from './login.vue'

Vue.config.productionTip = false
/* eslint-disable no-new */
new Vue({
  el: '#app',
  template: '<Login/>',
  components: { Login }
})
