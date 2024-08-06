<template>
  <div class="upload-doc-container">
    <h1>Upload Your RFI Document</h1>
    <SelectCategory @category-selected="handleCategorySelection" />
    <p v-if="selectedCategory">Selected Category: {{ selectedCategory }}</p>
    
    <FileUploader
      v-if="selectedCategory"
      :category="selectedCategory"
      @files-selected="handleFilesSelected"
      @upload-requested="handleUploadRequest"
      ref="fileUploader"
    />
    
    <div v-if="isLoading" class="spinner-container">
      <div class="spinner"></div>
      <p>
        Uploading and processing file...
        <span v-if="progress.total > 0">
          {{ progress.percentage }}% complete
          ({{ progress.current }} out of {{ progress.total }} queries processed)
        </span>
      </p>
      <div class="progress-bar">
        <div class="progress" :style="{ width: progress.percentage + '%' }"></div>
      </div>
    </div>

    <div v-if="uploadStatus" :class="['status-message', uploadStatus.type]">
      {{ uploadStatus.message }}
    </div>
    
    <button v-if="downloadReady" @click="downloadData" class="download-button">Download RFP</button>
  </div>
</template>

<script>
import { mapState, mapMutations, mapActions } from 'vuex'
import SelectCategory from '@/components/SelectCategory.vue'
import FileUploader from '@/components/FileUploader.vue'

export default {
  name: "UploadDoc",
  components: {
    SelectCategory,
    FileUploader
  },
  computed: {
    ...mapState('upload', [
      'isLoading',
      'progress',
      'uploadStatus',
      'downloadReady',
      'fileName',
      'selectedCategory'
    ])
  },
  methods: {
    ...mapMutations('upload', [
      'setLoading',
      'setProgress',
      'setUploadStatus',
      'setDownloadReady',
      'setFileName',
      'setSelectedCategory',
      'resetState'
    ]),
    ...mapActions('upload', ['saveStateToLocalStorage']),
    handleCategorySelection(category) {
      this.setSelectedCategory(category)
      this.saveStateToLocalStorage()
    },
    handleFilesSelected(files) {
      console.log('Files selected:', files)
    },
    async handleUploadRequest(formData) {
      if (!this.selectedCategory) return;

      this.setLoading(true)
      this.setUploadStatus(null)
      this.setDownloadReady(false)
      this.setProgress({ current: 0, total: 0, percentage: 0 })
      this.saveStateToLocalStorage()

      try {
        formData.append('category', this.selectedCategory)

        const response = await fetch(`/api/upload-rfp/${this.selectedCategory}`, {
          method: 'POST',
          body: formData,
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const reader = response.body.getReader();
        const decoder = new TextDecoder();

        let done = false;
        while (!done) {
          const { value, done: readerDone } = await reader.read();
          done = readerDone;
          
          if (value) {
            const chunk = decoder.decode(value, { stream: !done });
            const lines = chunk.split('\n');
            
            for (const line of lines) {
              if (line.startsWith('data:')) {
                try {
                  const data = JSON.parse(line.slice(5));
                  if (data.progress) {
                    this.setProgress(data.progress)
                    this.saveStateToLocalStorage()
                  } else if (data.file_ready) {
                    this.setDownloadReady(true)
                    this.setFileName(data.filename)
                    this.saveStateToLocalStorage()
                    // Fetch the file blob
                    const fileResponse = await fetch(`/api/get-processed-file/${this.SelectCategory}/${this.fileName}`);
                    if (fileResponse.ok) {
                      const fileBlob = await fileResponse.blob();
                      const reader = new FileReader();
                      reader.onloadend = () => {
                        const base64data = reader.result;
                        localStorage.setItem('fileData', base64data);
                      }
                      reader.readAsDataURL(fileBlob);
                    } else {
                      throw new Error('Failed to fetch the processed file');
                    }
                  }
                } catch (parseError) {
                  console.error('Error parsing server message:', parseError);
                }
              }
            }
          }
        }

        this.setUploadStatus({
          type: 'success',
          message: 'File uploaded and processed successfully!'
        })
        this.saveStateToLocalStorage()

        this.$refs.fileUploader.reset();
        if (this.$refs.fileShower) {
          this.$refs.fileShower.refreshFileList();
        }
      } catch (error) {
        console.error('Upload failed:', error);
        this.setUploadStatus({
          type: 'error',
          message: `An error occurred during upload: ${error.message}`
        })
        this.saveStateToLocalStorage()
      } finally {
        this.setLoading(false)
        this.saveStateToLocalStorage()
      }
    },
    downloadData() {
      const fileData = localStorage.getItem('fileData');
      if (!fileData) {
        console.error('No file data found');
        return;
      }

      const byteCharacters = atob(fileData.split(',')[1]);
      const byteNumbers = new Array(byteCharacters.length);
      for (let i = 0; i < byteCharacters.length; i++) {
        byteNumbers[i] = byteCharacters.charCodeAt(i);
      }
      const byteArray = new Uint8Array(byteNumbers);
      const blob = new Blob([byteArray], {type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'});

      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = this.fileName;
      document.body.appendChild(a);
      a.click();
      window.URL.revokeObjectURL(url);
      document.body.removeChild(a);
    }
  },
  created() {
    this.$store.dispatch('upload/loadStateFromLocalStorage')
  },
  beforeUnmount() {
    this.saveStateToLocalStorage()
  }
};
</script>

<style scoped>
.upload-doc-container {
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

.status-message {
  margin-top: 20px;
  padding: 10px;
  border-radius: 4px;
}

.status-message.success {
  background-color: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}

.status-message.error {
  background-color: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}

.spinner-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
}

.spinner {
  border: 4px solid #f3f3f3;
  border-top: 4px solid #ff4d4d;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.progress-bar {
  width: 100%;
  height: 20px;
  background-color: #f3f3f3;
  border-radius: 10px;
  margin-top: 10px;
  overflow: hidden;
}

.progress {
  height: 100%;
  background-color: #ff4d4d;
  transition: width 0.5s ease-in-out;
}
</style>