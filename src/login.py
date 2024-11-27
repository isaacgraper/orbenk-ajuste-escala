import logging
logger = logging.getLogger(f"{__name__}.Login")

from dotenv import load_dotenv 
import os

load_dotenv()

from src.click import Click

import time

class Login:
    def __init__(self, page):
        self.username = "bot@icop" or os.getenv("USERNAME")
        self.password = os.getenv("PASSWORD")
        self.page = page
        
        if not self.username or not self.password:
            logger.error("Password and username not found")
            raise ValueError("Password and username must be set in .env")
        
    def input_login(self):
        try:
            context = self.page.context
            context.clear_cookies()
            context.clear_browser_cache()
            self.page.reload(wait_until="load")
            logger.info("Page refreshed and loaded")
            
            logger.info("Inputing username")
            self.page.wait_for_selector("input[name='username']", timeout=30000)
            self.page.fill("input[name='username']", self.username)
            
            logger.info("Inputing password")
            self.page.wait_for_selector("input[name='password']", timeout=30000)
            self.page.fill("input[name='password']", self.password)

            Click.click(self.page, "div.login_user > button", 1000)
            
            self.page.wait_for_load_state('load')
            
            logger.info("Login sucessfully completed!")
        except TimeoutError:
            logger.error("Exceeded timeout to login")
        except Exception as e:
            logger.error(f"Error while trying to login: {e}", exc_info=True)