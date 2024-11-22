import config.dev as dev
from src.browser import Browser
from src.navigation import Navigation

import logging
logger = logging.getLogger(f"{__name__}.Process")

import time

from src.login import Login

class Process:
    def execute(self):
        with Browser(headless=False) as browser:
            browser.go_to_url(dev.URL)
            
            login = Login(browser.page)
            login.input_login()
            
            time.sleep(20)
            
            
            
                