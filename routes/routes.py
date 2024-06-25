## Routes contain the previous endpoints from main_test_celery_ai_agent

from fastapi import HTTPException
from fastapi import Query, APIRouter
from fastapi.responses import StreamingResponse
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles
from typing import Any
import json
from fastapi.testclient import TestClient
import os
from pydantic import BaseModel
from tasks import process_website_task, get_celery_job_update

