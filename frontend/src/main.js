import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import axios from "axios"
Vue.config.productionTip = false

const app = new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
})

Vue.prototype.$http = axios.create(
  {
    baseURL: "http://" + location.hostname + ":3000/",
    timeout: 20000,
    withCredentials: false,
    headers: {
      "Content-Type": "application/json",
    },
    cache: "default",
  }
)

app.$mount('#app')
