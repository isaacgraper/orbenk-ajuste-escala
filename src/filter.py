import config.logging as log
log.set_logging()

import logging
logger = logging.getLogger(f"{__name__}.Filter")

import time

from datetime import datetime, timedelta
from src.click import Page

class Filter:
    def __init__(self, page):
        self.page = page

    def apply_100_lines(self):
        try:
            logger.info("Clicking into filter lines")
            
            lines_btn = "div.app-content-body.nicescroll-continer > div.content-body > div.content-body-header > div.content-body-header-filters > div.filters-right > div > div > button:nth-child(2)"
            Page.click(self.page, lines_btn, 500, 0)
            
            logger.info("Selected hundred lines")
            lines_option = "div.content-body-header-filters > div.filters-right > div > div > ul > li:nth-child(4) > a"
            Page.click(self.page, lines_option, 500, 0)
            
            self.page.wait_for_load_state('load')
            logger.info("Hundred lines filter applied!")
        except Exception as e:
            logger.error(f"An exception occurred while trying to apply filter: {e}")
            
    def apply_filter(self):
        try:
            logger.info("Filtering inconsistencies...")
            
            Page.click(self.page, "#inconsistenciesFilter", 3000, 0)
            logger.info("Selecting inconsistencies type:")
            
            inconsistencies_type = ["Não registrado"]
            for label in inconsistencies_type:
                logger.info(f"{label}")
                self.page.select_option("select#clockingTypes", label=label)
            
            self.apply_date_filter()
            self.page.wait_for_load_state('load')
            
            logger.info("Clicking into filter")
            Page.click(self.page, "div.filter_container > div.hbox.filter_button.ng-scope > a.btn.button_link.btn-dark.ng-binding", 5000, 0)
            
            logger.info("Inconsistencies filter applied!")
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
            
            logger.info("Inconsistencies finishDate applied!")
        except Exception as e:
            logger.error(f"An exception occurred while trying to apply finishDate filter: {e}")