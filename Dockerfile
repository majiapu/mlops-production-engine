# 1. Use an official, lightweight Python base image based on Linux Debian Slim
FROM python:3.9-slim

# 2. Set environment variables to optimize Python performance inside the container
# Prevents Python from writing .pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1

# Forces stdout/stderr streams to be unbuffered so logs appear in real-time
ENV PYTHONUNBUFFERED=1

# 3. Set the working directory inside the container
WORKDIR /app

# 4. Install dependencies first to leverage Docker layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application code into the container
COPY ./app ./app

# 6. Expose port 8000 (the port FastAPI listens on)
EXPOSE 8000

# 7. Specify the command to run the application when the container starts
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]