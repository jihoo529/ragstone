<template>
  <div class="settings">
    <h1>User Settings</h1>
    <div class="category-settings">
      <h2>Category Settings</h2>
      <ul>
        <li v-for="(category, index) in categorySettings" :key="index">
          {{ category }}
          <button @click="removeCategory(index)" class="remove-button">-</button>
        </li>
      </ul>
      <div class="add-category">
        <input v-model="newCategory" placeholder="New category name" />
        <button @click="newCategory" class="add-button">+</button>
      </div>
    </div>
    <div class="model-settings">
      <h2>Model Settings</h2>
      <div class="input-group">
        <label for="modelSelect">Select Model:</label>
        <select id="modelSelect" v-model="selectedModel">
          <option v-for="model in models" :key="model.name" :value="model.name">
            {{ model.name }} - {{ model.description }}
          </option>
        </select>
      </div>
    </div>
    <div class="chunk-settings">
      <h2>Chunk Settings</h2>
      <div class="input-group">
        <label for="chunkSize">Chunk Size:</label>
        <input id="chunkSize" v-model.number="chunkSize" type="number" min="1" />
      </div>
      <div class="input-group">
        <label for="chunkOverlap">Chunk Overlap:</label>
        <input id="chunkOverlap" v-model.number="chunkOverlap" type="number" min="0" />
      </div>
    </div>
    <div class="prompt-settings">
      <h2>Prompt Settings</h2>
      <textarea v-model="promptContent" rows="10"></textarea>
    </div>
    <button @click="saveSettings" class="save-button">Save Settings</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'UserSettings',
  data() {
    return {
      categorySettings: ['HK1', 'HK2', 'HK3', 'HK4', 'HK5', 'HK6'],
      newCategory: '',
      selectedModel: '',
      models: [
        { name: 'llama3.1', description: 'Model from Meta, 8b size' },
        { name: 'qwen2:1.5b', description: 'Model from Alibaba, 1.5b size' },
        { name: 'phi3', description: 'Model from Microsoft, 3b size' },
        { name: 'gemma2:2b', description: 'Model from Google, 2b size' }
      ],
      promptContent: 'Default Prompt',
      chunkSize: 1024,
      chunkOverlap: 300
    }
  },
  created() {
    this.loadSettings()
    this.loadPromptContent()
  },
  methods: {
    async loadSettings() {
      try {
        const response = await axios.get('/api/settings')
        this.categorySettings = response.data.category_settings
        this.selectedModel = response.data.selected_model
      } catch (error) {
        console.error('Error loading settings:', error)
      }
    },
    async loadPromptContent() {
      try {
        const response = await axios.get('/api/prompt')
        console.log(response)
        this.selectedModel = response.data.model
        this.promptContent = response.data.prompt_template
        this.chunkSize = response.data.chunk_size
        this.chunkOverlap = response.data.chunk_overlap
      } catch (error) {
        console.error('Error loading prompt content:', error)
      }
    },
    removeCategory(index) {
      this.categorySettings.splice(index, 1)
    },
    addCategory() {
      if (this.newCategory.trim()) {
        this.categorySettings.push(this.newCategory.trim())
        this.newCategory = ''
      }
    },
    async saveSettings() {
      let settingsSuccess = false;
      let promptSuccess = false;

      try {
        const settingsResponse = await axios.put('/api/settings', { 
          category_settings: this.categorySettings,
          selected_model: this.selectedModel
        });
        settingsSuccess = settingsResponse.status === 200;
      } catch (error) {
        console.error('Error saving settings:', error);
      }

      try {
        const promptResponse = await axios.post('/api/prompt', {
          model: this.selectedModel,
          prompt_template: this.promptContent,
          chunk_size: this.chunkSize,
          chunk_overlap: this.chunkOverlap
        });
        promptSuccess = promptResponse.status === 200;
      } catch (error) {
        console.error('Error saving prompt:', error);
      }

      if (settingsSuccess || promptSuccess) {
        alert('Settings saved successfully!');
      } else {
        alert('Error: Unable to save settings. Please try again.');
      }
    }
  }
}
</script>

<style scoped>
.settings {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #333;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

h1, h2 {
  color: #2c3e50;
  margin-bottom: 20px;
}

h1 {
  font-size: 2.5em;
  border-bottom: 2px solid #ff4d4d;
  padding-bottom: 10px;
}

h2 {
  font-size: 1.8em;
  margin-top: 30px;
}

.category-settings ul {
  list-style-type: none;
  padding: 0;
}

.category-settings li {
  background-color: #ffffff;
  margin-bottom: 10px;
  padding: 15px;
  border-radius: 4px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.add-category {
  display: flex;
  margin-top: 20px;
}

.add-category input {
  flex-grow: 1;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px 0 0 4px;
  font-size: 1em;
}

button {
  padding: 10px 15px;
  background-color: #ff4d4d;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  font-size: 1em;
}

button:hover {
  background-color: #ff3333;
}

.add-button {
  border-radius: 0 4px 4px 0;
}

.remove-button {
  padding: 5px 10px;
  background-color: #e74c3c;
}

.remove-button:hover {
  background-color: #c0392b;
}

.save-button {
  margin-top: 20px;
  width: 100%;
  padding: 15px;
  font-size: 1.2em;
  background-color: #2ecc71;
}

.save-button:hover {
  background-color: #27ae60;
}

textarea {
  width: 100%;
  margin-top: 10px;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 4px;
  resize: vertical;
  font-size: 1em;
  font-family: inherit;
}

textarea:focus, .add-category input:focus {
  outline: none;
  border-color: #ff4d4d;
  box-shadow: 0 0 0 2px rgba(255, 77, 77, 0.2);
}

.model-settings, .chunk-settings {
  margin-top: 20px;
}

.input-group {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.input-group label {
  flex: 0 0 120px;
  font-weight: bold;
}

.input-group input, .input-group select {
  flex: 1;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1em;
}

.input-group input:focus, .input-group select:focus {
  outline: none;
  border-color: #ff4d4d;
  box-shadow: 0 0 0 2px rgba(255, 77, 77, 0.2);
}
</style>