from playwright.sync_api import sync_playwright

import config.logging as log
log.set_logging()

import logging
logger = logging.getLogger(f"{__name__}.Browser")



import time

class Browser:
    def __init__(self, headless=True):
        logger.info("Initializing browser...")
        self.headless = headless
        self.browser = None
        self.page = None

    def __enter__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=self.headless)
        self.page = self.browser.new_page()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            if self.browser:
                self.browser.close()
            if hasattr(self, 'playwright'):
                self.playwright.stop()
        except Exception as e:
            logger.error(f"Error during cleanup: {e}", exc_info=True)
        finally:
            if exc_type:
                logger.error(f"An exception occurred: {exc_value}", exc_info=True)
        
    def go_to_url(self, url):
        if self.page:
            if not url:
                logger.error(f"Error no URL specified: {url}")
            else:
                start_time = time.time()
                logger.info(f"Navigating to URL: {url}")
                self.page.goto(url)
                logger.info(f"Navigation completed in {time.time() - start_time:.2f} seconds")
            
