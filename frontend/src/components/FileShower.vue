<!-- src/components/FileShower.vue -->
<template>
    <div class="file-shower">
      <h2>List of documents under {{ category }} folder</h2>
      <p>(✔️: Document populated in DB)</p>
      <hr>
      <div v-if="loading">Loading...</div>
      <div v-if="!files || files.length === 0">No files found.</div>
      <div v-else class="file-list">
        <div v-for="file in files" :key="file.name" class="file-item">
          <span class="chroma-status">{{ file.inChroma ? '✔️' : '' }}</span>
          <span class="file-name">{{ file.name }}</span>
          <button @click="downloadFile(file.name)">Download</button>
          <button @click="deleteFile(file.name)">Delete</button>
        </div>
      </div>
      <hr>
    </div>
  </template>
  
  <script>
  import axios from 'axios';

  export default {
    name: 'FileShower',
    props: {
      category: {
        type: String,
        required: true
      },
      refreshTrigger: {
        type: Number,
        default: 0
      }
    },
    data() {
      return {
        files: [],
        loading: false
      }
    },
    watch: {
      category: {
        immediate: true,
        handler: 'fetchFiles'
      },
      refreshTrigger: 'fetchFiles'
    },
    mounted() {
      this.fetchFiles();
    },
    methods: {
      async fetchFiles() {
        this.loading = true;
        try {
          const response = await axios.get(`/api/files/${this.category}`);
          this.files = response.data;
        } catch (error) {
          console.error('Error fetching files:', error);
          // Handle error (e.g., show error message to user)
        } finally {
          this.loading = false;
        }
      },
      async downloadFile(fileName) {
        try {
          const response = await axios.get(`/api/download/${this.category}/${fileName}`, {
            responseType: 'blob'
          });
          const url = window.URL.createObjectURL(new Blob([response.data]));
          const link = document.createElement('a');
          link.href = url;
          link.setAttribute('download', fileName);
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);


          this.$emit('file-downloaded', fileName);
        } catch (error) {
          console.error(`Error downloading file ${fileName}:`, error);
          // Handle error (e.g., show error message to user)
        }
      },
      async deleteFile(fileName) {
        try {
          await axios.delete(`/api/delete/${this.category}/${fileName}`);
          console.log(`Deleted ${fileName}`);
          await this.fetchFiles();
          this.$emit('file-deleted', fileName);
        } catch (error) {
          console.error(`Error deleting file ${fileName}:`, error);
          // Handle error (e.g., show error message to user)
        }
      },
      refreshFileList() {
        this.fetchFiles();
      }
    }
  }
  </script>
  
<style scoped>
  .file-list {
    margin-top: 10px;
  }

  .file-item {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
  }

  .chroma-status {
    width: 20px;
  }

  .file-name {
    flex-grow: 1;
  }

  button {
    margin-left: 10px;
  }
</style>