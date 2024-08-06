<!-- src/views/AboutUser.vue -->
<template>
    <div class="about-user">
      <h1>About User</h1>
      <div v-if="user">
        <p><strong>Name:</strong> {{ user.name }}</p>
        <p><strong>Email:</strong> {{ user.email }}</p>
        <p><strong>Role:</strong> {{ user.role }}</p>
        <!-- Add more user details as needed -->
      </div>
      <div v-else>
        <p>Loading user information...</p>
      </div>
    </div>
  </template>
  
  <script>
  import { mapState } from 'vuex'
  
  export default {
    name: 'AboutUser',
    computed: {
      ...mapState({
        user: state => state.user.user
      })
    },
    created() {
      this.$store.dispatch('user/fetchUser')
    }
  }
  </script>
  
  <style scoped>
  .about-user {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
  }
  </style>