#!/bin/bash

# Start Redis server
redis-server &

# Give Redis a few seconds to start
sleep 3

# Start Celery worker
celery -A tasks worker --loglevel=INFO &

# Give Celery a few seconds to start
sleep 3

# Start FastAPI with Uvicorn
uvicorn main_celery:app --reload
