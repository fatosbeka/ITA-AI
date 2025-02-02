# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY backend/requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port your app runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "backend/app.py"]
