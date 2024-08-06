<template>
  <div class="login-container">
    <h1>{{ pageTitle }}</h1>
    <div class="login-interface">
      <form @submit.prevent="handleSubmit">
        <div class="form-group">
          <label for="username">Username:</label>
          <input
            type="text"
            id="username"
            v-model="username"
            required
          >
        </div>
        <div class="form-group">
          <label for="password">{{ isChangingPassword ? 'Old Password:' : 'Password:' }}</label>
          <input
            type="password"
            id="password"
            v-model="password"
            required
          >
        </div>
        <div v-if="isChangingPassword" class="form-group">
          <label for="newPassword">New Password:</label>
          <input
            type="password"
            id="newPassword"
            v-model="newPassword"
            required
          >
        </div>
        <div v-if="isChangingPassword" class="form-group">
          <label for="confirmNewPassword">Confirm New Password:</label>
          <input
            type="password"
            id="confirmNewPassword"
            v-model="confirmNewPassword"
            required
          >
        </div>
        <p v-if="passwordMismatch" class="error-message">New passwords do not match.</p>
        <button type="submit" :disabled="!isFormValid">{{ submitButtonText }}</button>
      </form>
    </div>
    <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
    <p v-if="successMessage" class="success-message">{{ successMessage }}</p>
    <div v-if="isLoading" class="loading">
      <span class="dot"></span>
      <span class="dot"></span>
      <span class="dot"></span>
    </div>
    <p @click="toggleChangePassword" class="change-password-link">
      {{ isChangingPassword ? 'Back to Login' : 'Change Password' }}
    </p>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: "LoginPage",
  data() {
    return {
      username: '',
      password: '',
      newPassword: '',
      confirmNewPassword: '',
      errorMessage: '',
      successMessage: '',
      isLoading: false,
      isChangingPassword: false
    };
  },
  computed: {
    isFormValid() {
      if (this.isChangingPassword) {
        return this.username && this.password && this.newPassword && 
               this.confirmNewPassword && (this.newPassword === this.confirmNewPassword);
      }
      return this.username && this.password;
    },
    pageTitle() {
      return this.isChangingPassword ? 'Change Password' : 'Login';
    },
    submitButtonText() {
      return this.isChangingPassword ? 'Change Password' : 'Login';
    },
    passwordMismatch() {
      return this.isChangingPassword && 
             this.newPassword && 
             this.confirmNewPassword && 
             this.newPassword !== this.confirmNewPassword;
    }
  },
  methods: {
    ...mapActions('user', ['login', 'changePassword']),
    async handleSubmit() {
      if (!this.isFormValid) return;

      this.isLoading = true;
      this.errorMessage = '';
      this.successMessage = '';

      try {
        if (this.isChangingPassword) {
          if (this.newPassword !== this.confirmNewPassword) {
            this.errorMessage = 'New passwords do not match.';
            return;
          }
          await this.changePassword({
            username: this.username,
            oldPassword: this.password,
            newPassword: this.newPassword
          });
          this.successMessage = 'Password changed successfully!';
          setTimeout(() => {
            this.successMessage = '';
            this.toggleChangePassword();
          }, 3000);
        } else {
          const response = await this.login({ username: this.username, password: this.password });
          console.log('Login response:', response);
          this.$router.push('/');
        }
      } catch (error) {
        console.error('Operation failed:', error);
        this.errorMessage = error.response?.data?.detail || 'An unexpected error occurred. Please try again.';
      } finally {
        this.isLoading = false;
      }
    },
    toggleChangePassword() {
      this.isChangingPassword = !this.isChangingPassword;
      this.errorMessage = '';
      this.successMessage = '';
      this.password = '';
      this.newPassword = '';
      this.confirmNewPassword = '';
    }
  }
};
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.login-interface {
  margin-top: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #fff5f5;
  padding: 20px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input {
  width: calc(100% - 24px); /* Subtract left and right padding */
  padding: 8px 12px;
  border: 1px solid #ccc;
  border-radius: 20px;
  font-size: 14px;
  box-sizing: border-box; /* Include padding and border in the element's total width */
}

button {
  width: 100%;
  padding: 8px 16px;
  background-color: #ff5252;
  color: white;
  border: none;
  border-radius: 20px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #d32f2f;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.error-message {
  color: #ff5252;
  margin-top: 10px;
}

.loading {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 10px;
}

.dot {
  width: 8px;
  height: 8px;
  background-color: #333;
  border-radius: 50%;
  display: inline-block;
  margin: 0 3px;
  animation: wave 1.3s linear infinite;
}

.dot:nth-child(2) {
  animation-delay: -1.1s;
}

.dot:nth-child(3) {
  animation-delay: -0.9s;
}

.success-message {
  color: #4CAF50;
  margin-top: 10px;
}

@keyframes wave {
  0%, 60%, 100% {
    transform: initial;
  }
  30% {
    transform: translateY(-10px);
  }
}

.change-password-link {
  color: #007bff;
  cursor: pointer;
  text-decoration: underline;
  margin-top: 10px;
}
</style>