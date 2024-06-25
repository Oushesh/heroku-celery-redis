#web: ./heroku-setup.sh
#Web: chmod +x heroku-setup.sh
#web: playwright install chromium
#web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker main_test_celery_ai_agent:app
#web: gunicorn -c gunicorn_config.py main_test_celery_ai_agent:app

web: uvicorn main_celery:app
worker: celery -A tasks worker --loglevel=INFO
