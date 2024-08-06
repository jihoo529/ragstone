<!-- src/components/FileUploader.vue -->
<template>
    <div class="file-uploader">
      <input 
        type="file" 
        @change="onFileSelected" 
        ref="fileInput"
        :accept="accept"
        multiple
      >
      <button @click="onUploadClicked" :disabled="!hasSelectedFiles">
        {{ uploadButtonText }}
      </button>
      <div v-if="selectedFiles.length > 0">
        <p>Selected file(s):</p>
        <ul>
          <li v-for="file in selectedFiles" :key="file.name">{{ file.name }}</li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'FileUploader',
    props: {
      accept: {
        type: String,
        default: '*'
      },
      uploadButtonText: {
        type: String,
        default: 'Upload'
      }
    },
    data() {
      return {
        selectedFiles: []
      }
    },
    computed: {
      hasSelectedFiles() {
        return this.selectedFiles.length > 0
      }
    },
    methods: {
      onFileSelected(event) {
        this.selectedFiles = Array.from(event.target.files)
        this.$emit('files-selected', this.selectedFiles)
      },
      onUploadClicked() {
        if (this.hasSelectedFiles) {
          const formData = new FormData()
          this.selectedFiles.forEach(file => {
            formData.append('files', file)
          })
          this.$emit('upload-requested', formData)
        }
      },
      reset() {
        this.selectedFiles = []
        this.$refs.fileInput.value = ''
      }
    }
  }
  </script>
  
  <style scoped>
  .file-uploader {
    margin-bottom: 20px;
    font-family: Arial, sans-serif;
  }
  
  input[type="file"] {
    margin-bottom: 10px;
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
  
  button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
  }
  
  ul {
    list-style-type: none;
    padding-left: 0;
  }
  
  li {
    margin-bottom: 5px;
  }
  </style>