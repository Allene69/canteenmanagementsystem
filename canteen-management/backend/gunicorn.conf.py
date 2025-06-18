# Gunicorn configuration file (gunicorn.conf.py)
# Example: Not directly used by the current Dockerfile CMD, but good for reference

# Number of worker processes
# workers = 4 # Adjust based on your server's CPU cores (e.g., 2-4 per core)

# The socket to bind to
# bind = "0.0.0.0:5000" # Same as in Dockerfile CMD

# Logging
# accesslog = "-" # Log to stdout
# errorlog = "-"  # Log to stderr

# Worker class (for performance, gevent or eventlet can be used if app is async-compatible)
# worker_class = "sync"

# You would typically copy this file into your Docker image and modify the CMD
# in the Dockerfile to use it, e.g.:
# CMD ["gunicorn", "-c", "gunicorn.conf.py", "app:app"]
