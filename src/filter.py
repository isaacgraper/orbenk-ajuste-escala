import config.logging as log
log.set_logging()

import logging
logger = logging.getLogger(f"{__name__}.Filter")

import time

class Filter:
    def __init__(self, page):
        self.page = page

    def apply_100_lines(self):
        try:
            logger.info("Clicking into filter lines")
            self.page.click("div.app-content-body.nicescroll-continer > div.content-body > div.content-body-header > div.content-body-header-filters > div.filters-right > div > div > button:nth-child(2)", delay=250)
            time.sleep(10)
            
            logger.info("Selecting hundred lines..")
            self.page.click("div.content-body-header-filters > div.filters-right > div > div > ul > li:nth-child(4) > a", delay=250)
            time.sleep(10)
        except Exception as e:
            logger.error(f"An exception occurred while trying to apply filter: {e}")
            
    def apply_filter(self):
        try:
            logger.info("Clicking into filter button")
            self.page.click("i#inconsistenciesFilter", delay=250)
            
            logger.info("Selecting inconsistencies type:")
            
            # Tipos de inconsistências para "Não registrado"
            inconsistencies_type = ["Não registrado"]
            
            for label in inconsistencies_type:
                logger.info(f"{label}")
                self.page.select_option("select#clockingTypes", label=label)
            
            logger.info("Clicking into filter")
            self.page.click("a.btn.button_link.btn-dark", delay=500)
        except Exception as e:
            logger.error(f"An exception occurred while trying to apply filter: {e}")
