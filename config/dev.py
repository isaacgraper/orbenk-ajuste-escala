from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD= os.getenv("PASSWORD")
URL = os.getenv("URL_DEV")
HEADLESS=True