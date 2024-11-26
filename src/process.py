import config.dev as dev
from src.browser import Browser
from src.navigation import Navigation

import logging
logger = logging.getLogger(f"{__name__}.Process")

import time

from src.login import Login
from src.filter import Filter
from src.action import Action
from src.pagination import Pagination
from src.page import Page
from src.network.network import capture_response_on_filter

class Process:
    def __init__(self, headless_mode, url):
        self.headless_mode = headless_mode or dev.HEADLESS
        self.url = url or dev.URL
    
    def execute(self):
        logger.warning(f"Inicializing process in headless={self.headless_mode}")
        try:
            with Browser(self.headless_mode) as browser:
                browser.go_to_url(self.url)
                
                login = Login(browser.page)
                login.input_login()
                
                nav = Navigation(browser.page)
                nav.navigate_to_inconsistencies()
                
                filter = Filter(browser.page)
                filter.apply_100_lines()
                
                filter = Filter(browser.page)
                filter.apply_filter()
                
                browser.page.wait_for_selector(".js-content-load", state="hidden", timeout=0)
                
                response_data = capture_response_on_filter(browser.page, "clockings/inconsistenciessearchfilter")
                if response_data:
                    logger.info("Data has been loaded!")
                    logger.info(f"{response_data}")
                else:
                    logger.error("Somenthing went wrong retrieving the data...")
                
                self.start(browser.page)
                logger.warning("Process has been stopped!")
                time.sleep(999)
        except Exception as e:
            logger.error(f"An exception occurred during execute process: {e}", exc_info=True)
            
    def start(self, page):
        logger.info("Starting process...")

        try:
            action = Action(page)
            while True:                
                action.select_all_rows()
                
                if self.complete(page):
                    paginate = Pagination(page)
                    
                    page.wait_for_selector(".js-content-load", state="hidden", timeout=0)
                    
                    if paginate.paginate():
                        logger.info("Page paginated!")
                    else:
                        logger.info("No more pages to process...")
                        return
                else:
                    logger.info("No more inconsistencies to process...")
                    return
        except Exception as e:
            logger.error(f"An exception occurred during start process: {e}", exc_info=True)
            
    def complete(self, page):
        try:
            adjust_button = "div.filters-right > button"
            
            el = page.locator(adjust_button)
            classes = el.get_attribute("class")
            if classes and "button-disable" in classes:
                logger.info("Adjust inconsistencies button disabled")
                return False
            
            logger.info("Clicking into adjust button")
            Page.click(page, adjust_button, 1000, 30000)
            
            adjust_path_buttons = [
                "[btn-radio=\"'CANCELED'\"]",
                "multiselect > div > div > div:nth-child(1) > div > i",
                "label[alt=\"Erro operacional\"]"
            ]
            
            for button in adjust_path_buttons:
                Page.click(page, button, 1000, 30000)
            
            adjustment_desc = "Cancelamento realizado via Bot: \"Não registrado\""
            page.fill("input#note", adjustment_desc)
            
            logger.info("Clicking into finish ajustments button")
            Page.click(page, "a.btn.button_link.btn-primary.ng-binding", 2000, 30000)
            
            logger.info("Process completed!")
            return True
        except TimeoutError:
            logger.error(f"Exceeded timeout of 60000ms to comple process")
            return False
        except Exception as e:
            logger.error(f"An unexpected error occurred during complete process: {e}", exc_info=True)
            raise

    def restart(self):
        self.execute()
        
        