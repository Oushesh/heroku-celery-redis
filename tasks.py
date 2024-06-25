import os
from celery import Celery
from dotenv import load_dotenv
import time 

load_dotenv()

# Celery configuration
redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379/0') #For local development

#For production use redis_TLS_URL
redis_tls_url = os.getenv('REDIS_TLS_URL','rediss://:pd2d5a49e95897e1b3d0f0f8fbb43cffad27226cc3c12aa9c8622f240e716683a@ec2-44-206-187-141.compute-1.amazonaws.com:17720')


# Ensure ssl_cert_reqs parameter is set correctly
redis_ssl_cert_reqs = os.getenv('REDIS_SSL_CERT_REQS', 'CERT_REQUIRED')

"""
celery_app = Celery(
    'tasks',
    broker=redis_tls_url,
    backend=redis_tls_url,
    broker_transport_options={
        'ssl_cert_reqs': redis_ssl_cert_reqs
    },
)
"""

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
