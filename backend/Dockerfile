# Backend Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy the backend's requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the entire backend code
COPY . .

# Expose the backend port (e.g., FastAPI default is 8000)
EXPOSE 8000

# Start FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
