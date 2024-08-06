// src/router.js
console.log('Router.js: Router configuration loading');

import { createRouter, createWebHistory } from 'vue-router'
import store from './store'
import AppAbout from './views/About.vue'
import UploadDoc from './views/UploadDoc.vue'
import ChatBot from './views/ChatBot.vue'
import UpdateDB from './views/UpdateDB.vue'
import AboutUser from './views/AboutUser.vue'
import UserSettings from './views/UserSettings.vue'
import LoginPage from './views/LoginPage.vue'  // Import the LoginPage component

const routes = [
    { 
        path: '/', 
        component: AppAbout,
        meta: { requiresAuth: true }  // This route requires authentication
    },
    { 
        path: '/upload-doc', 
        component: UploadDoc,
        meta: { requiresAuth: true }
    },
    { 
        path: '/chatbot', 
        component: ChatBot,
        meta: { requiresAuth: true }
    },
    { 
        path: '/update-db', 
        component: UpdateDB,
        meta: { requiresAuth: true }
    },
    { 
        path: '/about-user', 
        component: AboutUser,
        meta: { requiresAuth: true }
    },
    { 
        path: '/settings', 
        component: UserSettings,
        meta: { requiresAuth: true }
    },
    
    { 
        path: '/login', 
        component: LoginPage 
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

// Navigation guard
// router.beforeEach((to, from, next) => {
//     const isAuthenticated = localStorage.getItem('isAuthenticated') === 'true'
    
//     if (to.meta.requiresAuth && !isAuthenticated) {
//         next('/login')
//     } else if (to.path === '/login' && isAuthenticated) {
//         next('/')
//     } else {
//         next()
//     }
// })
// Navigation guard
router.beforeEach((to, from, next) => {
    console.log('Navigation guard triggered');
    console.log('Navigating from:', from.path);
    console.log('Navigating to:', to.path);
    console.log('Route requires auth:', to.meta.requiresAuth);
    
    const isAuthenticated = store.getters['user/isLoggedIn'];
    console.log('Is authenticated (from store):', isAuthenticated);
    
    if (to.meta.requiresAuth && !isAuthenticated) {
        console.log('Auth required but not authenticated, redirecting to login');
        next('/login');
    } else if (to.path === '/login' && isAuthenticated) {
        console.log('Already authenticated, redirecting to home');
        next('/');
    } else {
        console.log('Proceeding to requested route');
        next();
    }
});
  


export default router