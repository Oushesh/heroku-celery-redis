import os
from celery import Celery
from dotenv import load_dotenv
import time 

load_dotenv()

# Celery configuration
#redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379/0') #For local development

#For production use redis_TLS_URL
redis_url = os.getenv('REDIS_TLS_URL')

celery_app = Celery(
    'tasks',
    broker=redis_url,
    backend=redis_url,
)

@celery_app.task
def add(x, y):
    counter = 0
    while counter<=50:
        counter+=1
        print (counter)
        time.sleep(5)
    return x + y
