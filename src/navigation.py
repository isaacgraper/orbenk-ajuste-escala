import config.logging as log
log.set_logging()

import logging
logger = logging.getLogger(f"{__name__}.Navigation")

import config.dev as dev

import time

class Navigation:
    def __init__(self, page):
        self.page = page

    def navigate_to_inconsistencies(self):
        try:
            start_time = time.time()
            
            logger.info("Navigating to inconsistencies")
            self.page.goto(f"{dev.URL}#/inconsistencies", wait_until="networkidle")
            
            logger.info(f"Navigation completed in {time.time() - start_time:.2f} seconds")
        except Exception as e:
            logger.error(f"An exception occurred while trying to navigate into inconsistencies: {e}")
            
    
    