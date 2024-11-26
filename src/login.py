import logging
logger = logging.getLogger(f"{__name__}.Login")

from dotenv import load_dotenv 
import os

load_dotenv()

from src.click import Page

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
            self.page.fill("input[name='username']", self.username)
            
            self.page.fill("input[name='password']", self.password)

            Page.click(self.page, "div.login_user > button", 1000, 30000)
            
            self.page.wait_for_load_state('networkidle')
            
            logger.info("Login sucessfully completed!")
        except Exception as e:
            logger.error(f"Error while trying to login: {e}", exc_info=True)