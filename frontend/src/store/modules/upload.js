export default {
    namespaced: true,
    state: () => ({
      isLoading: false,
      progress: {
        current: 0,
        total: 0,
        percentage: 0
      },
      uploadStatus: null,
      downloadReady: false,
      fileName: '',
      selectedCategory: ''
    }),
    mutations: {
      setLoading(state, isLoading) {
        state.isLoading = isLoading
      },
      setProgress(state, progress) {
        state.progress = progress
      },
      setUploadStatus(state, status) {
        state.uploadStatus = status
      },
      setDownloadReady(state, ready) {
        state.downloadReady = ready
      },
      setFileName(state, name) {
        state.fileName = name
      },
      setSelectedCategory(state, category) {
        state.selectedCategory = category
      },
      resetState(state) {
        Object.assign(state, {
          isLoading: false,
          progress: { current: 0, total: 0, percentage: 0 },
          uploadStatus: null,
          downloadReady: false,
          fileName: '',
          selectedCategory: ''
        })
      }
    },
    actions: {
      saveStateToLocalStorage({ state }) {
        localStorage.setItem('uploadState', JSON.stringify(state))
      },
      loadStateFromLocalStorage({ commit }) {
        const savedState = localStorage.getItem('uploadState')
        if (savedState) {
          const parsedState = JSON.parse(savedState)
          Object.keys(parsedState).forEach(key => {
            commit(`set${key.charAt(0).toUpperCase() + key.slice(1)}`, parsedState[key])
          })
        }
      }
    }
  }