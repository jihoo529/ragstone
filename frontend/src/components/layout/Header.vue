<!-- src/components/layout/Header.vue -->
<template>
  <header class="header">
    <div class="header-container">
      <div class="header-left">
        <img src="@/assets/ragstone_logo.png" alt="Equinix Logo" class="logo">
        <h1 class="header-title">Ragstone</h1>
      </div>
      <nav class="header-nav">
        <router-link to="/" class="header-link">Instruction</router-link>
        <router-link to="/upload-doc" class="header-link">Upload RFI Document</router-link>
        <router-link to="/chatbot" class="header-link">Chat with Ragstone</router-link>
        <router-link to="/update-db" class="header-link">Document Management</router-link>
      </nav>
      <div class="user-dropdown">
        <div class="user-avatar" @click="toggleDropdown">
          <!-- Placeholder for user avatar -->
          <span class="avatar-icon">U</span>
        </div>
        <transition name="dropdown">
          <div v-if="showDropdown" class="dropdown-menu">
            <ul>
              <li><router-link to="/settings">Settings</router-link></li>
              <li><a @click="logout" href="#">Logout</a></li>
            </ul>
          </div>
        </transition>
      </div>
    </div>
  </header>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: "AppHeader",
  data() {
    return {
      showDropdown: false
    };
  },
  methods: {
    ...mapActions('user', ['logoutUser']),
    toggleDropdown() {
      this.showDropdown = !this.showDropdown;
    },
    closeDropdown(e) {
      if (!this.$el.querySelector('.user-dropdown').contains(e.target)) {
        this.showDropdown = false;
      }
    },
    async logout() {
      try {
        await this.logoutUser();
        // this.$router.push('/');
      } catch (error) {
        console.error('Logout failed:', error);
      }
    }
  },
  mounted() {
    document.addEventListener('click', this.closeDropdown);
  },
  beforeUnmount() {
    document.removeEventListener('click', this.closeDropdown);
  }
};
</script>

<style scoped>
.header {
  background-color: #ff5252; /* Light blue background */
  color: #fff; /* White text color */
  padding: 10px 0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Subtle shadow */
}

.header-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.header-left {
  display: flex;
  align-items: center;
}

.logo {
  height: 40px; /* Adjust this value to match your desired logo size */
  margin-right: 15px;
}

.header-title, .header-link {
  font-family: Arial, sans-serif; /* Arial font */
  margin: 0;
}

.header-title {
  font-size: 1.5rem;
  margin: 0;
}


.header-nav {
  display: flex;
}

.header-link {
  text-decoration: none;
  color: #fff;
  padding: 10px 15px;
  margin-right: 10px;
  transition: background-color 0.3s ease;
}

.header-link:hover {
  background-color: #d32f2f; /* Darker blue on hover */
  border-radius: 5px;
}

.user-dropdown {
  position: relative;
}

.user-avatar {
  cursor: pointer;
  width: 40px;
  height: 40px;
  background-color: #d32f2f;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.avatar-icon {
  font-weight: bold;
}

.dropdown-menu {
  position: absolute;
  top: calc(100% + 10px); /* Position it 10px below the avatar */
  right: 0;
  background-color: white;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  z-index: 1000;
  min-width: 150px; /* Ensure a minimum width for the dropdown */
}

.dropdown-menu ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.dropdown-menu li {
  padding: 10px 20px;
}

.dropdown-menu a {
  color: #333;
  text-decoration: none;
  display: block; /* Make the entire area clickable */
}

.dropdown-menu a:hover {
  background-color: #f5f5f5; /* Light gray background on hover */
}

/* Animation for dropdown */
.dropdown-enter-active, .dropdown-leave-active {
  transition: opacity 0.3s, transform 0.3s;
}

.dropdown-enter, .dropdown-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

@media (max-width: 768px) {
  .header-title {
    font-size: 1.2rem;
  }
}
</style>
