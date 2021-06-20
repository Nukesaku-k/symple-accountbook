// https://github.com/FortAwesome/vue-fontawesome
import Vue from 'vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import {
    faCircle,
    faTshirt,
    faQuestion,
    faShoppingBasket,
    faHamburger,
    faCoffee,
    faFilm,
    faCreditCard,
    faShoppingCart,
    faTint,
    faBurn,
    faPlug,
    faGlobe,
    faMobileAlt,
    faCashRegister,
    faGraduationCap,
    faToiletPaper,
    faSubway,
    faBusAlt,
    faTaxi,
    faGift,
    faDumbbell,
    faPlayCircle,
    faCut,
    faBookOpen,
    faIcons
} from '@fortawesome/free-solid-svg-icons'
import { faApple } from '@fortawesome/free-brands-svg-icons'

// Import entire styles.
library.add(
    faCircle,
    faTshirt,
    faQuestion,
    faShoppingBasket,
    faHamburger,
    faCoffee,
    faFilm,
    faCreditCard,
    faShoppingCart,
    faTint,
    faBurn,
    faPlug,
    faGlobe,
    faApple,
    faMobileAlt,
    faCashRegister,
    faGraduationCap,
    faToiletPaper,
    faSubway,
    faBusAlt,
    faTaxi,
    faGift,
    faDumbbell,
    faPlayCircle,
    faCut,
    faBookOpen,
    faIcons
)

Vue.component('font-awesome-icon', FontAwesomeIcon)