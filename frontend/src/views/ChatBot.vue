<!-- src/views/ChatBot.vue -->
<template>
  <div class="chatbot-container">
    <h1>Query about Category</h1>
    
    <SelectCategory @category-selected="handleCategorySelection" />
    
    <p v-if="selectedCategory">Selected category: {{ selectedCategory }}</p>
    
    <div class="chat-interface" v-if="selectedCategory">
      <div class="chat-messages">
        <div v-for="(message, index) in chatMessages" :key="index" 
            :class="['message', message.sender]">
          <div class="message-text">{{ message.text }}</div>
          <div v-if="message.sources && message.sources.length" class="message-sources">
            <strong>Sources:</strong>
            <ul>
              <li v-for="(source, sourceIndex) in message.sources" :key="sourceIndex">
                {{ source }}
              </li>
            </ul>
          </div>
        </div>
        <div v-if="isLoading" class="message bot loading">
          <span class="dot"></span>
          <span class="dot"></span>
          <span class="dot"></span>
        </div>
      </div>
      <div class="chat-input">
        <input 
          v-model="userMessage" 
          @keyup.enter="sendMessage" 
          placeholder="Type your message here..." 
          :disabled="isLoading"
        />
        <button @click="sendMessage" :disabled="isLoading">Send</button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';
import SelectCategory from '@/components/SelectCategory.vue';

export default {
  name: "ChatBot",
  components: {
    SelectCategory
  },
  setup() {
    const selectedCategory = ref('');
    const userMessage = ref('');
    const chatMessages = ref([]);
    const isLoading = ref(false);

    function handleCategorySelection(category) {
      selectedCategory.value = category;
      chatMessages.value = [];
      console.log(`category selected: ${category}`);
    }

    async function sendMessage() {
      if (userMessage.value.trim() && !isLoading.value) {
        const userMsg = userMessage.value;
        chatMessages.value.push({ sender: 'user', text: userMsg });
        userMessage.value = '';
        isLoading.value = true;

        try {
          const response = await axios.post('/api/chat', {
            message: userMsg,
            category: selectedCategory.value
          });

          chatMessages.value.push({
            sender: 'bot',
            text: response.data.response,
            sources: response.data.sources
          });
        } catch (error) {
          console.error('Error sending message:', error);
          chatMessages.value.push({
            sender: 'bot',
            text: 'Sorry, I encountered an error.',
            sources: []
          });
        } finally {
          isLoading.value = false;
        }
      }
    }

    return {
      selectedCategory,
      userMessage,
      chatMessages,
      isLoading,
      handleCategorySelection,
      sendMessage
    };
  }
};
</script>

<style scoped>
.chatbot-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.chat-interface {
  margin-top: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  overflow: hidden;
}

.chat-messages {
  height: 300px;
  overflow-y: auto;
  padding: 10px;
  background-color: #fff5f5;
}

.message {
  max-width: 70%;
  margin-bottom: 10px;
  padding: 8px 12px;
  border-radius: 18px;
  clear: both;
}

.message.user {
  float: right;
  background-color: #ff8a80;
  color: white;
  border-bottom-right-radius: 4px;
}

.message.bot {
  float: left;
  background-color: #e6e6e6;
  color: black;
  border-bottom-left-radius: 4px;
}

.chat-input {
  display: flex;
  padding: 10px;
  background-color: #fff;
}

input {
  flex-grow: 1;
  padding: 8px 12px;
  border: 1px solid #ccc;
  border-radius: 20px;
  font-size: 14px;
}

button {
  margin-left: 10px;
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

.loading {
  display: flex;
  justify-content: center;
  align-items: center;
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

.message-sources {
  font-size: 0.8em;
  margin-top: 5px;
}

.message-sources ul {
  margin: 5px 0;
  padding-left: 20px;
}

@keyframes wave {
  0%, 60%, 100% {
    transform: initial;
  }
  30% {
    transform: translateY(-10px);
  }
}
</style>