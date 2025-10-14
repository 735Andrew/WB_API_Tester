import time
from fastapi import FastAPI
from sqlalchemy import create_engine
from .task_2 import router
from config import DATABASE_URL
from .models import Sales, Base


app = FastAPI()
app.include_router(router=router)


time.sleep(5)
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
