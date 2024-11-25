import config.logging as log
log.set_logging()

import logging
logger = logging.getLogger(f"{__name__}.Filter")

import time

from datetime import datetime, timedelta
from src.state.page_state import State

class Filter:
    def __init__(self, page):
        self.page = page

    def apply_100_lines(self):
        try:
            logger.info("Clicking into filter lines")
            
            self.page.click("div.app-content-body.nicescroll-continer > div.content-body > div.content-body-header > div.content-body-header-filters > div.filters-right > div > div > button:nth-child(2)", delay=250)
            
            logger.info("Selecting hundred lines..")
            
            self.page.click("div.content-body-header-filters > div.filters-right > div > div > ul > li:nth-child(4) > a", delay=2000)
            
            self.page.wait_for_load_state('load')
        except Exception as e:
            logger.error(f"An exception occurred while trying to apply filter: {e}")
            
    def apply_filter(self):
        try:
            logger.info("Clicking into filter button")
            
            self.page.wait_for_selector("i#inconsistenciesFilter", state="visible")
            self.page.click("i#inconsistenciesFilter", delay=1000)
            
            logger.info("Selecting inconsistencies type:")
            
            inconsistencies_type = ["Não registrado"]
            
            for label in inconsistencies_type:
                logger.info(f"{label}")
                self.page.select_option("select#clockingTypes", label=label)
            
            self.page.wait_for_load_state('load')
            
            self.apply_date_filter()
            
            logger.info("Clicking into filter")
            
            self.page.click("a.btn.button_link.btn-dark", delay=1000)
        except Exception as e:
            logger.error(f"An exception occurred while trying to apply filter: {e}")

    def apply_date_filter(self):
        try:
            logger.info("Input date filter for 1 week ago...")
            
            today = datetime.now()
            one_week_ago = today - timedelta(days=8)
            formatted_date = one_week_ago.strftime("%Y-%m-%d")
            
            logger.info(f"Applying finishDate filter with value: {formatted_date}")
            self.page.fill("input#finishDate", formatted_date)
            
            self.page.wait_for_load_state('load')
        except Exception as e:
            logger.error(f"An exception occurred while trying to apply finishDate filter: {e}")
    
    def sort_date_filter():
        pass