import time
import logging
logger = logging.getLogger(f"{__name__}.Filter")

from datetime import datetime, timedelta
from src.click import Click

class Filter:
    def __init__(self, page):
        self.page = page

    def apply_100_lines(self):
        try:
            logger.info("Clicking into filter lines")
            
            lines_btn = "div.app-content-body.nicescroll-continer > div.content-body > div.content-body-header > div.content-body-header-filters > div.filters-right > div > div > button:nth-child(2)"
            
            time.sleep(2)
            Click.click(self.page, lines_btn)
            
            logger.info("Selected hundred lines")
            lines_option = "div.content-body-header-filters > div.filters-right > div > div > ul > li:nth-child(4) > a"
            
            time.sleep(2)
            Click.click(self.page, lines_option)
            
            self.page.wait_for_load_state('load')
            time.sleep(5)
            
            logger.info("Hundred lines filter applied!")
        except TimeoutError:
            logger.error("Exceeded timeout for pagination")
        except Exception as e:
            logger.error(f"An exception occurred while trying to apply filter: {e}")
            
    def apply_filter(self):
        try:
            logger.info("Filtering inconsistencies...")
            
            time.sleep(2)
            Click.click(self.page, "#inconsistenciesFilter")
            
            logger.info("Selecting inconsistencies type:")
            
            inconsistencies_type = ["Não registrado"]
            for label in inconsistencies_type:
                logger.info(f"{label}")
                
                time.sleep(2)
                self.page.select_option("select#clockingTypes", label=label)
            
            self.apply_date_filter()
            self.page.wait_for_load_state('load')
            
            logger.info("Clicking into filter")
            
            time.sleep(2)
            Click.click(self.page, "div.filter_container > div.hbox.filter_button.ng-scope > a.btn.button_link.btn-dark.ng-binding")
            
            
            self.page.wait_for_load_state('load')
            time.sleep(5)
            
            logger.info("Inconsistencies filter applied!")
        except TimeoutError:
            logger.error("Exceeded timeout for pagination")
        except Exception as e:
            logger.error(f"An exception occurred while trying to apply filter: {e}")

    def apply_date_filter(self):
        try:
            logger.info("Input date filter for 1 week ago...")
            
            today = datetime.now()
            one_week_ago = today - timedelta(days=8)
            formatted_date = one_week_ago.strftime("%Y-%m-%d")
            
            logger.info(f"Applying finishDate filter with value: {formatted_date}")
            
            time.sleep(2)
            self.page.fill("input#finishDate", formatted_date)
            
            self.page.wait_for_load_state('load')
            time.sleep(5)
            
            logger.info("Inconsistencies finishDate applied!")
        except TimeoutError:
            logger.error("Exceeded timeout for pagination")
        except Exception as e:
            logger.error(f"An exception occurred while trying to apply finishDate filter: {e}")