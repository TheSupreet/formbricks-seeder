import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("FORMBRICKS_BASE_URL")
MGMT_KEY = os.getenv("FORMBRICKS_MANAGEMENT_API_KEY")
CLIENT_KEY = os.getenv("FORMBRICKS_CLIENT_API_KEY")
