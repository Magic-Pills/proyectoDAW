import Vue from 'vue'
import Router from 'vue-router'
import Inicio from './views/Inicio.vue'
import Nosotros from './views/Nosotros.vue'
import Noticias from './components/paginaNoticias/NoticiasGeneral.vue'
import Productos from './views/Productos.vue'
//import Admin from './././backend/src/pages/Dashboard.vue'

Vue.use(Router)



export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'inicio',
            component: Inicio
        },
        {
            path: '/nosotros',
            name: 'nosotros',
            component: Nosotros
        },
        {
            path: '/noticias',
            name: 'noticias',
            component: Noticias
        },
        {
            path: '/productos',
            name: 'productos',
            component: Productos
        }/*,
        {
            path: '/admin',
            name: 'admin',
            component: Admin
        }*/
    ]
})