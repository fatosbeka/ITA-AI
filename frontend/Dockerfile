# Frontend Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy the frontend's requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the entire frontend code
COPY . .

# Expose the port for Streamlit (default is 8501)
EXPOSE 8501

# Start the Streamlit app
CMD ["streamlit", "run", "app.py"]
