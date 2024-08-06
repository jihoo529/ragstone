# Ragstone

Ragstone is a powerful, AI-driven solution for processing and responding to Request For Information (RFI) and Request For Proposal (RFP) documents. By leveraging Retrieval-Augmented Generation (RAG) technology, Ragstone automates the time-consuming task of searching through technical documents to answer complex RFI & RFP questions.

## Features

- **Intelligent RFI/RFP Processing**: Upload RFI/RFP documents in Excel format for automated analysis and response generation.
- **Interactive Chatbot**: Directly interact with the AI to ask questions about your technical documents.
- **Document Management**: Easily upload, delete, and manage documents in your knowledge base.
- **Vector Database**: Utilize ChromaDB to efficiently store and retrieve vector representations of your documents.
- **Multi-Container Architecture**: Leverages Docker for easy deployment and scalability.

## Technology Stack

- **Backend**: FastAPI
- **Frontend**: Vue.js
- **Database**: MongoDB
- **Web Server**: Nginx
- **AI Model**: Ollama (llama3.1)
- **Vector Database**: ChromaDB

## Prerequisites

- Docker and Docker Compose (latest stable versions recommended)
- Sufficient hardware to run Ollama (llama3.1) - check Ollama's official documentation for specific requirements

## Installation and Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ragstone.git
   cd ragstone
   ```

2. Configure environment variables:
   - Create a `.env` file in the root directory
   - Set necessary environment variables (refer to `config.yml` for required variables)

3. Build and start the Docker containers:
   ```
   docker-compose up -d --build
   ```

4. Access the application:
   - Frontend: `http://localhost`
   - Backend API documentation: `http://localhost:8000/docs`

## Usage

1. **Upload Documents**:
   - Navigate to the "Update Database" page
   - Select the relevant folder and upload your technical documents

2. **Process RFP**:
   - Upload your RFP Excel file
   - The system will automatically process and generate responses

3. **Chat with Bot**:
   - Use the chatbot interface to ask specific questions about your documents

4. **Manage Knowledge Base**:
   - Add or remove documents as needed
   - Populate the vector database for improved performance

## API Documentation

Detailed API documentation is available via Swagger UI. Access it at `http://127.0.0.1:8000/docs` when the backend is running.

## Configuration

Key configuration files:
- `docker-compose.yml`: Defines the multi-container Docker application
- `config.yml`: Contains application-specific configurations
- `nginx.conf`: Nginx web server configuration

Refer to these files for detailed settings and modify as needed.

## Contributing

Contributions to Ragstone are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` file for more information.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Vue.js](https://vuejs.org/)
- [MongoDB](https://www.mongodb.com/)
- [Nginx](https://www.nginx.com/)
- [Ollama](https://ollama.ai/)
- [ChromaDB](https://www.trychroma.com/)
- [Docker](https://www.docker.com/)

## Support

For support, please open an issue in the GitHub repository or contact the project maintainers.
