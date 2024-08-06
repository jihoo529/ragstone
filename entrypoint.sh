#!/bin/bash
set -e

echo "Starting Ollama server..."
/bin/ollama serve &
sleep 10  # Wait for server startup

echo "🔴 Retrieving llama3.1 model..."
ollama pull llama3.1
echo "🟢 Model retrieved!"

echo "🔴 Retrieving qwen2:1.5b model..."
ollama pull qwen2:1.5b
echo "🟢 Model retrieved!"

echo "🔴 Retrieving phi3 model..."
ollama pull phi3
echo "🟢 Model retrieved!"

echo "🔴 Retrieving gemma2:2b model..."
ollama pull gemma2:2b
echo "🟢 Model retrieved!"

wait  # Keep container running
