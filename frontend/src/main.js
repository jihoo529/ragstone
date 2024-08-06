// src/main.js

import { createApp } from 'vue'
import { createStore } from 'vuex'
import App from './App.vue'
import router from './router'  // Import the router

import uploadModule from './store/modules/upload'
import userModule from './store/modules/user'

const store = createStore({
    modules: {
        upload: uploadModule,
        user: userModule
    }
})

const app = createApp(App)

console.log('Main.js: Setting up Vue app with router:', router);

const token = localStorage.getItem('token')
if (token) {
    store.commit('user/SET_AUTH', true)
    localStorage.setItem('isAuthenticated', 'true')
} else {
    store.commit('user/SET_AUTH', false)
    localStorage.setItem('isAuthenticated', 'false')
}

app.use(router)
app.use(store)

console.log('Main.js: Vue app created and router attached');

app.mount('#app')