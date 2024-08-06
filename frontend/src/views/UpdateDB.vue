<!-- src/views/UpdateDB.vue -->
<template>
  <div class="update-db">
    <h1>Manage your documents, Update DB</h1>
    
    <SelectCategory @category-selected="handleCategorySelection" />
    
    <FileUploader 
      v-if="selectedCategory"
      :category="selectedCategory"
      @files-selected="handleFilesSelected"
      @upload-requested="handleUploadRequest"
      ref="fileUploader"
    />
    
    <FileShower 
      v-if="selectedCategory"
      :category="selectedCategory"
      ref="fileShower"
    />
    
    <div class="action-buttons">
      <button @click="convertMarkdown">Convert Markdown from PDF files</button>
      <button @click="clearDatabase">Clear database {{ selectedCategory }}</button>
      <button @click="populateDatabase" :disabled="isPopulating">Populate database {{ selectedCategory }}</button>
    </div>
    
    <div v-if="showConversionProgress" class="progress-container">
      <h3>Markdown Conversion Progress:</h3>
      <div class="progress-header">
        <div v-if="isConverting" class="spinner"></div>
        <span v-if="isConverting">Generating Markdown from PDF...</span>
        <span v-else>✅ Markdown conversion complete</span>
      </div>
      <button @click="dismissConversionProgress" class="dismiss-button">Dismiss</button>
    </div>

    <div v-if="showProgressContainer" class="progress-container">
      <h3>Progress Log:</h3>
      <div class="progress-header">
        <div v-if="isPopulating" class="spinner"></div>
        <span v-if="isPopulating">Population in progress...</span>
        <span v-else>✅Population complete</span>
      </div>
      <div class="progress-log" ref="progressLog">
        <p v-for="(message, index) in progressMessages" :key="index" :class="{ 'new-message': index === progressMessages.length - 1 }">
          {{ message }}
        </p>
      </div>
      <button @click="dismissProgressContainer" class="dismiss-button">Dismiss</button>
    </div>
  </div>
</template>

<script>
import SelectCategory from '@/components/SelectCategory.vue'
import FileUploader from '@/components/FileUploader.vue'
import FileShower from '@/components/FileShower.vue'
import axios from 'axios';

export default {
  name: 'UpdateDB',
  components: {
    SelectCategory,
    FileUploader,
    FileShower
  },
  data() {
    return {
      selectedCategory: '',
      files: [],
      isPopulating: false,
      progressMessage: [],
      socket: null,
      showProgressContainer: false,
      showConversionProgress: false,
      updateTrigger: 0
    }
  },
  methods: {
    handleCategorySelection(category) {
      this.selectedCategory = category;
    },
    handleFilesSelected(files) {
      console.log('Files selected:', files)
    },
    async handleUploadRequest(formData) {
      if (!this.selectedCategory) return;

      try {
        formData.append('category', this.selectedCategory)

        const response = await axios.post('/api/upload', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });

        if (response.data.status_code == 400) {
          alert('File already exist!!')
          return
        }
        console.log('Upload successful:', response.data);

        this.$refs.fileUploader.reset();
        this.$refs.fileShower.refreshFileList();
      } catch (error) {
        console.error('Upload failed:', error.response ? error.response.data : error);
      }
    },
    async refreshFileList() {
      try {
        if (this.$refs.fileShower) {
          await this.$refs.fileShower.fetchFiles();
        } else {
          console.log('FileShower component not mounted yet');
          this.needsRefresh = true;
        }
      } catch (error) {
        console.error('Error fetching file list:', error);
      }
    },
    async convertMarkdown() {
      if (!this.selectedCategory) {
        alert('Please select an Category first.');
        return;
      }

      this.isConverting = true;
      this.showConversionProgress = true;
      
      try {
        const response = await axios.get(`/api/convert-markdown/${this.selectedCategory}`);
        if (response.data.success) {
          alert('Successfully generated Markdown files from PDFs')
          console.log(response.data.result);
        } else {
          alert('Markdown conversion failed.');
        }
      } catch (error) {
        console.error('Error converting to markdown:', error);
        alert('An error occurred during markdown conversion. Please try again.');
      } finally {
        this.isConverting = false;
        this.showConversionProgress = false;
        await this.refreshFileList(); // Refresh file list after conversion attempt
      }
    },
    async clearDatabase() {
      if (!this.selectedCategory) {
        alert('Please select an category first.');
        return;
      }
      try {
        const response = await axios.get(`/api/clear-database/${this.selectedCategory}`);
        if (response.data.success) {
          alert('Database successfully cleared!');
          console.log(`Database cleared for ${this.selectedCategory}`);
          await this.refreshFileList();
        } else {
          alert(`Failed to clear database: ${response.data.message}`);
        }
      } catch (error) {
        console.error('Error clearing database:', error);
        alert('An error occurred while clearing the database. Please try again.');
      }
    },

    async populateDatabase() {
      if (!this.selectedCategory) {
        alert('Please select an category first.');
        return;
      }

      this.isPopulating = true;
      this.progressMessages = [];
      this.showProgressContainer = true;
      
      const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
      this.socket = new WebSocket(`${protocol}//${window.location.host}/api/ws/populate_db/${this.selectedCategory}`);

      this.socket.onmessage = (event) => {
        this.progressMessages.push(event.data);
        this.updateTrigger += 1; // Force update
        this.$nextTick(() => {
          this.scrollToBottom();
        });
      };

      this.socket.onclose = () => {
        this.isPopulating = false;
        this.progressMessages.push('Population completed or connection closed.');
        this.updateTrigger += 1; // Force update
        this.$nextTick(() => {
          this.scrollToBottom();
        });
        this.refreshFileList();
      };

      this.socket.onerror = (error) => {
        console.error('WebSocket error:', error);
        this.isPopulating = false;
        this.progressMessages.push('Error occurred during population.');
        this.updateTrigger += 1; // Force update
        this.$nextTick(() => {
          this.scrollToBottom();
        });
      };
    },

    dismissProgressContainer() {
      this.showProgressContainer = false;
    },

    dismissConversionProgress() {
      this.showConversionProgress = false;
    },

    scrollToBottom() {
      const logContainer = this.$refs.progressLog;
      if (logContainer) {
        logContainer.scrollTop = logContainer.scrollHeight;
      }
    }
  },
  watch: {
    selectedCategory(newVal) {
      if (newVal) {
        this.refreshFileList();
      }
    },
    updateTrigger() {
      this.$forceUpdate();
    }
  },

  mounted() {
    if (this.selectedCategory) {
      this.refreshFileList();
    }
  }
}
</script>

<style scoped>
.update-db {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.action-buttons {
  margin-top: 20px;
}

button {
  margin-right: 10px;
  padding: 10px 15px;
  background-color: #ff4d4d;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #ff3333;
}

.progress-header {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.progress-container {
  margin-top: 20px;
  padding: 10px;
  background-color: #f0f0f0;
  border-radius: 4px;
  position: relative;
}

.progress-log {
  max-height: 200px;
  overflow-y: auto;
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 30px;
}

.progress-log p {
  margin: 5px 0;
  transition: background-color 0.5s ease;
}

.new-message {
  background-color: #e6f7ff;
  animation: fadeBackground 2s forwards;
}

@keyframes fadeBackground {
  from { background-color: #e6f7ff; }
  to { background-color: transparent; }
}

.dismiss-button {
  position: absolute;
  bottom: 10px;
  right: 10px;
  background-color: #ff4d4d;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 5px 10px;
  cursor: pointer;
  font-size: 0.8em;
}

.dismiss-button:hover {
  background-color: #ff3333;
}

.spinner {
  border: 2px solid #f3f3f3;
  border-top: 2px solid #ff4d4d;
  border-radius: 50%;
  width: 20px;
  height: 20px;
  animation: spin 1s linear infinite;
  margin-right: 10px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>