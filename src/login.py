import config.logging as log
log.set_logging()

import logging
logger = logging.getLogger(f"{__name__}.Login")

from dotenv import load_dotenv 
import os

load_dotenv()

class Login:
    def __init__(self, page):
        self.username = os.getenv("USERNAME")
        self.password = os.getenv("PASSWORD")
        self.page = page
        
    def login(self):
        logger.info("Input username")
        self.page.fill("input[name='username']", self.username)
        import config.logging as log
log.set_logging()

import logging
logger = logging.getLogger(f"{__name__}.Navigation")

from dotenv import load_dotenv 
import os

load_dotenv()

class Login:
    def __init__(self, page):
        self.username = "bot@icop"
        self.password = os.getenv("PASSWORD")
        self.page = page
        
        if not self.username or not self.password:
            logger.error("Password and username not found")
            raise ValueError("Password and username must be set in .env")
        
    def input_login(self):
        try:
            self.page.fill("input[name='username']", self.username)
            self.page.fill("input[name='password']", self.password)

            self.page.click("div.login_user > button", delay=250)
            
            self.page.wait_for_load_state('networkidle')
            
            logger.info("Login sucessfully completed!")
        except Exception as e:
            logger.error(f"Error while trying to login: {e}", exc_info=True)