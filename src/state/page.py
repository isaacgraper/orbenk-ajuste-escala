import logging
logger = logging.getLogger(f"{__name__}.Page")

import time

class Page:
    def __init__(self, page):
        self.page = page
        
    @staticmethod
    def check_modal_load_content(self):
        while True:
            try:
                if self.page.wait_for_selector("div.js-content-load", state="invisible"):
                    logger.info("Modal content loaded and invisible!")
                    break
                else:
                    logger.warning("Waiting for modal content to load and become invisible...")
                    time.sleep(5)
            except Exception as e:
                logger.error(f"Error while checking modal content: {e}")
                break
                
    @staticmethod
    def check_modal():
        pass