import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(basedir, ".env"))

WB_TOKEN = os.environ.get("TOKEN")
DATABASE_URL = os.environ.get("POSTGRESQL_DATABASE_URL")
