import multiprocessing

workers = 4  # Number of worker processes
worker_class = 'uvicorn.workers.UvicornWorker'  # Worker class
timeout = 300  # Timeout in seconds
#bind = "0.0.0.0:{}".format(os.getenv("PORT", "8000"))  # Bind to port
