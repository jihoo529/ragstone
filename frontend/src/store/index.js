// src/store/index.js

import { createStore } from 'vuex'
import upload from './modules/upload'
import user from './modules/user'


export default createStore({
  modules: {
    upload,
    user
  }
})