<template>
  <div class="select-category">
    <label for="category-select">Select Category:</label>
    <select id="category-select" v-model="selectedCategory" @change="emitSelected">
      <option value="" disabled>Please select an category</option>
      <option v-for="category in categoryList" :key="category" :value="category">
        {{ category }}
      </option>
    </select>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'SelectCategory',
  data() {
    return {
      categoryList: [],
      selectedCategory: ''
    }
  },
  async created() {
    await this.fetchcategoryList()
  },
  methods: {
    async fetchcategoryList() {
      try {
        const response = await axios.get('/api/settings')
        this.categoryList = response.data.category_settings
      } catch (error) {
        console.error('Error fetching category list:', error)
      }
    },
    emitSelected() {
      this.$emit('category-selected', this.selectedCategory)
    }
  }
}
</script>

<style scoped>
.select-category {
  margin-bottom: 20px;
  font-family: Arial, sans-serif;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

select {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
}
</style>