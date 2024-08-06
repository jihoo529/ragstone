FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend directory
COPY . .

# Set the Python path to include the app directory
ENV PYTHONPATH=/app

EXPOSE 8000

# Update the CMD to use the correct path to main.py
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]