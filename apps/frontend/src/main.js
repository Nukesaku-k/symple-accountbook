// エントリポイントとなるjsファイル

import Vue from 'vue'
import App from './App.vue'
import './plugins/element'
import './plugins/goodtable'
import './plugins/fontawesome'

import router from './router'
import VHeader from './components/VHeader'
import VFooter from './components/VFooter'
import VContainer from './components/VContainer'

// Entery Global components.
Vue.component('v-header', VHeader)
Vue.component('v-footer', VFooter)
Vue.component('v-container', VContainer)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');