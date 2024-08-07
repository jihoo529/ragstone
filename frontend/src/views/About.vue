<template>
  <div class="about-container">
    <h1>How to Use Ragstone🗿</h1>
    
    <section>
      <h2>1. Upload RFI Document</h2>
      <p>You can upload Microsoft Excel (.xlsx) or .csv documents that contain the questions listed.</p>
      <p>Make sure your file is formatted correctly with the questions you want to automate.</p>
      <p>RFP document should contain 2 columns, with headers "Questions" and "Answers". Uploading RFI document can only contain values in "Questions" column, and Ragstone will answer for each question automatically.</p>
      <img src="../assets/rfp_example.png" alt="RFP Example" class="image-example">
    </section>

    <section>
      <h2>2. Chat to Chatbot</h2>
      <p>Select a data center from the dropdown menu and ask questions about the specified data center.</p>
      <p>The chatbot will provide relevant information based on the selected data center.</p>
    </section>

    <section>
      <h2>3. Update DB</h2>
      <p>First choose the specific category</p>
      <p>You can upload, download, or delete documents in the server folder for chosen datacenter.</p>
      <p>Additionally, you can populate the vector database from these documents so that Ragstone can read from the database.</p>
      <ul>
        <li><strong>Convert Markdown from PDF files button</strong>: You can generate Markdown (.md) files from PDF files that you uploaded to the folder.</li>
        <li><strong>Why do we use .md files?</strong>: Markdown (.md) files are lightweight, easy to parse, and directly readable by many text-processing tools.</li>
        <li><strong>Clear database button</strong>: You can clear existing data in ChromaDB vector database.</li>
        <li><strong>Populate database button</strong>: After you upload documents to a folder in the server, this doesn't mean the document information is populated in vector database. As Ragstone only reads from the vector database, you can populate the vector database from the documents uploaded in the chosen datacenter folder.</li>
      </ul>
      <img src="../assets/pipeline_diagram.png" alt="Pipeline Diagram" class="image-example">
    </section>

    <section>
      <h2>4. Settings</h2>
      
      <h3>4.1 Category Management</h3>
      <p>Manage your document categories:</p>
      <ul>
        <li>Add new categories to organize your documents</li>
        <li>Remove existing categories (warning: this will delete associated documents)</li>
        <li>Edit category names to better reflect your document structure</li>
      </ul>
      
      <h3>4.2 Model Selection</h3>
      <p>Choose from the following AI models:</p>
      <ul>
        <li>LLaMA 3.1 (8B parameters): Balanced performance and accuracy</li>
        <li>Qwen2 (1.5B parameters): Faster, but may be less accurate for complex tasks</li>
        <li>Phi3 (3B parameters): Good balance of speed and capability</li>
        <li>Gemma2 (2B parameters): Efficient model with strong performance on various tasks</li>
      </ul>
      
      <h3>4.3 Chunk Settings</h3>
      <p>Adjust how documents are processed:</p>
      <ul>
        <li>Chunk Size:
          <ul>
            <li>Minimum recommended: 512 or 1024 tokens</li>
            <li>Smaller chunks: More accurate answers, but slower processing and may miss broader context</li>
            <li>Larger chunks: Faster processing, but may be less precise for specific queries</li>
          </ul>
        </li>
        <li>Chunk Overlap:
          <ul>
            <li>Recommended: 300 tokens</li>
            <li>Larger overlap: Better context preservation between chunks, but increases processing time</li>
          </ul>
        </li>
      </ul>
      
      <h3>4.4 Prompt Settings</h3>
      <p>Customize the instructions given to the AI model:</p>
      <ul>
        <li>Edit the detailed prompt to guide the AI's responses</li>
        <li>Tailor instructions for specific use cases or query types</li>
        <li>Fine-tune the AI's tone, style, or focus based on your needs</li>
      </ul>
    </section>

    <section>
      <h2>4. Source Code</h2>
      <p>You can find the source code of this application in the following GitHub link:</p>
      <a href="https://github.com/jihoo529/ragstone" target="_blank">https://github.com/jihoo529/ragstone</a>
    </section>

    <section>
      <h2>5. Support</h2>
      <p>If you face any problem, bugs, or issues, please send email to the following addresses:</p>
      <a href="mailto:jihoolee529@gmail.com">jihoolee529@gmail.com</a>
    </section>
  </div>
</template>

<script>
export default {
  name: "AppAbout"
};
</script>

<style scoped>
.about-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

h1 {
  color: #333;
  border-bottom: 2px solid #ff5252;
  padding-bottom: 10px;
  font-family: Arial, sans-serif;
}

h2 {
  color: #d32f2f;
  margin-top: 30px;
  font-family: Arial, sans-serif;
}

p {
  line-height: 1.6;
}

ul {
  padding-left: 20px;
}

li {
  margin-bottom: 10px;
}

.image-example {
  max-width: 100%;
  height: auto;
  margin: 20px 0;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

a {
  color: #007bff;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}
</style>