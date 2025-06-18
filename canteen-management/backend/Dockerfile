# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend application code into the container at /app
COPY . .

# Make port 5000 available to the world outside this container
# (This is the port Flask development server runs on; Gunicorn will also use it or be configured)
EXPOSE 5000

# Define environment variables (if any, e.g., for production database URI)
# ENV FLASK_ENV production
# ENV DATABASE_URL postgresql://user:password@host:port/database

# Command to run the application using Gunicorn (production WSGI server)
# The CMD should be overridden if you need to pass specific Gunicorn settings or run migrations
# For this example, we assume app.py is the entry point and 'app' is the Flask instance.
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
