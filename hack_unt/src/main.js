import Vue from 'vue'
import App from './App.vue'
import vuetify from '@/plugins/vuetify'
import 'vuetify/dist/vuetify.min.css'

Vue.config.productionTip = false
// Vue.use(Vuetify)
// export default new Vuetify({ })

new Vue({
  vuetify,
  components: {App},
  template: "<App/>",
  render: h => h(App)
}).$mount('#app')
