import axios from 'axios'

const API_URL = '/api'

const axiosInstance = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json'
  }
})

axiosInstance.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token')
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`
    }
    console.log('Request config:', config);
    return config
  },
  (error) => {
    console.error('Request interceptor error:', error);
    return Promise.reject(error)
  }
)

axiosInstance.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('Response interceptor error:', error.response || error);
    if (error.response && error.response.status === 401) {
      // Handle 401 error (e.g., redirect to login page)
      console.log('Unauthorized access, redirecting to login');
      // Implement redirection to login page here
    }
    return Promise.reject(error);
  }
);

export default {
  fetchUser() {
    return axiosInstance.get('/profile')
  },
  login(username, password) {
    console.log('Attempting login with username:', username);
    return axiosInstance.post('/login', { username, password })
      .then(response => {
        console.log('Login successful:', response.data);
        return response;
      })
      .catch(error => {
        console.error('Login error:', error.response || error);
        throw error;
      });
  },
  logout() {
    return axiosInstance.get('/logout')
      .then(response => {
        console.log('Logout successful:', response.data);
        return response;
      })
      .catch(error => {
        console.error('Logout error:', error.response || error);
        // Even if the server request fails, we should still clear local storage
        localStorage.removeItem('token');
        localStorage.removeItem('isAuthenticated');
        throw error;
      });
  },
  changePassword(username, oldPassword, newPassword) {
    console.log('Attempting to change password for username:', username);
    console.log('Old password:', oldPassword);
    console.log('new password:', newPassword);
    return axiosInstance.post('/change-password', {
      username,
      old_password: oldPassword,
      new_password: newPassword
    })
      .then(response => {
        console.log('Password change successful:', response.data);
        return response;
      })
      .catch(error => {
        console.error('Password change error:', error.response || error);
        throw error;
      });
  }
}