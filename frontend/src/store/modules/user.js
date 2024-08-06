// src/store/modules/user.js
import userService from '@/services/userService'

export default {
  namespaced: true,
  state: {
    user: null,
    isAuthenticated: false
  },
  mutations: {
    SET_USER(state, user) {
      state.user = user
    },
    CLEAR_USER(state) {
      state.user = null
      state.isAuthenticated = false
    },
    SET_AUTH(state, isAuthenticated) {
      state.isAuthenticated = isAuthenticated
    }
  },
  actions: {
    async fetchUser({ commit }) {
      try {
        const response = await userService.fetchUser()
        commit('SET_USER', response.data)
        commit('SET_AUTH', true)
      } catch (error) {
        console.error('Error fetching user:', error)
        commit('SET_AUTH', false)
      }
    },
    async login({ commit }, { username, password }) {
      console.log('Login action called with username:', username);
      try {
        const response = await userService.login(username, password);
        console.log('Login API response:', response.data);
        
        console.log('Updating Vuex store...');
        commit('SET_USER', response.data.user);
        console.log('User set in store');
        commit('SET_AUTH', true);
        console.log('Authentication state set to true');
        
        console.log('Updating localStorage...');
        localStorage.setItem('token', response.data.access_token);
        localStorage.setItem('isAuthenticated', 'true');
        console.log('Token and isAuthenticated set in localStorage');
        
        return response;
      } catch (error) {
        console.error('Error in login action:', error);
        throw error;
      }
    },
    async logoutUser({ commit }) {
      try {
        await userService.logout();
      } catch (error) {
        console.error('Error during logout:', error);
        // Log out the user locally even if the server request fails
      } finally {
        // Always clear local state and storage
        commit('CLEAR_USER');
        localStorage.removeItem('token');
        localStorage.removeItem('isAuthenticated');

        window.location.reload();
      }
    },
    async changePassword(_, { username, oldPassword, newPassword }) {
      try {
        const response = await userService.changePassword(username, oldPassword, newPassword);
        return response.data;
      } catch (error) {
        console.error('Error changing password:', error);
        throw error;
      }
    }
  },
  getters: {
    isLoggedIn: state => state.isAuthenticated
  }
}