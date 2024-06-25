import os
import time
from fastapi import FastAPI, HTTPException
from celery.result import AsyncResult
from pydantic import BaseModel
from tasks import celery_app, add
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class JobRequest(BaseModel):
    x: int
    y: int

@app.post("/start_add_job")
async def start_add_job(request: JobRequest):
    task = add.apply_async((request.x, request.y))
    return {"task_id": task.id}

@app.get("/get_job_status/{task_id}")
async def get_job_status(task_id: str):
    task_result = AsyncResult(task_id, app=celery_app)
    if task_result.state == 'PENDING':
        return {"status": task_result.state}
    elif task_result.state != 'FAILURE':
        return {
            "status": task_result.state,
            "result": task_result.result
        }
    else:
        return {
            "status": task_result.state,
            "result": str(task_result.info)
        }

@app.get("/poll_job_status/{task_id}")
async def poll_job_status(task_id: str):
    while True:
        task_result = AsyncResult(task_id, app=celery_app)
        if task_result.state == 'SUCCESS':
            return {"status": task_result.state, "result": task_result.result}
        elif task_result.state == 'FAILURE':
            return {"status": task_result.state, "result": str(task_result.info)}
        time.sleep(1)
