import os
import logging
import time

from dotenv import load_dotenv 
load_dotenv()

from src.click import Click

logger = logging.getLogger(f"{__name__}.Login")

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
            retry = 3
            current_url = self.page.url
            
            while current_url == "https://orbenk.nexti.com/#/login" and retry > 0:
                logger.info("Attempting login...")
                
                self.page.wait_for_selector("input[name='username']", timeout=30000)
                time.sleep(2)
                self.page.fill("input[name='username']", self.username)
                logger.info("Username inputted successfully.")
                
                self.page.wait_for_selector("input[name='password']", timeout=30000)
                time.sleep(2)
                self.page.fill("input[name='password']", self.password)
                logger.info("Password inputted successfully.")

                Click.click(self.page, "div.login_user > button", 1000)
                self.page.wait_for_load_state('load')

                current_url = self.page.url
                logger.info(f"Current URL: {current_url}")
                
                retry -= 1
            
            if current_url != "https://orbenk.nexti.com/#/login":
                logger.info("Login successfully completed!")
            else:
                logger.error("Login failed after 3 attempts.")
        
        except TimeoutError:
            logger.error("Exceeded timeout while trying to login.")
        except Exception as e:
            logger.error(f"Error while trying to login: {e}", exc_info=True)