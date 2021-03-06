// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import axios from 'axios'
import qs from 'qs'
Vue.config.productionTip = false
Vue.use(ElementUI)

axios.defaults.baseURL= process.env.API_ROOT
axios.interceptors.request.use(config => {
  config.data = qs.stringify(config.data)
  config.headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
