import Vue from 'vue'
import App from './App.vue'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import brand icons */
import { faTwitter, faFacebook, faTiktok, faInstagram } from '@fortawesome/free-brands-svg-icons';


/* import specific icons */
import { faCartShopping, faShop, faHeart, faEye} from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(faShop, faCartShopping, faHeart, faEye, faTwitter, faTiktok, faFacebook, faInstagram)

/* add font awesome icon component */
Vue.component('font-awesome-icon', FontAwesomeIcon)


// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

Vue.config.productionTip = false

new Vue({
  render: function (h) { return h(App) },
}).$mount('#app')

screen.orientation.lock('landscape').then(
  success=> console.log(success),
  failure=> console.log(failure)
);

