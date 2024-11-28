import time
import logging

logger = logging.getLogger(f"{__name__}.Process")

import config.dev as dev

from src.browser import Browser
from src.navigation import Navigation
from src.login import Login
from src.filter import Filter
from src.action import Action
from src.pagination import Pagination
from src.click import Click
from src.state.page_state import State
from src.report import Report

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
                
                browser.page.wait_for_load_state('load')
                login.input_login()
                
                nav = Navigation(browser.page)
                nav.navigate_to_inconsistencies()
                
                filter = Filter(browser.page)
                # filter.apply_100_lines()
                
                filter = Filter(browser.page)
                filter.apply_filter()
                
                self.start(browser.page)
                logger.warning("Process has been stopped!")
                browser.page.pause()
        except Exception as e:
            logger.error(f"An exception occurred during execute process: {e}", exc_info=True)
            
    def start(self, page):
        logger.info("Starting process...")
        
        try:    
            action = Action(page)
            while True:
                action.select_all_rows()
                
                if State.check_has_modal(page):
                     logger.info("Modal apperead")
                
                data = Report.get_data_and_return(page)
                Report.generate_report(data, "") # Include path for report data file
                 
                if self.complete(page):
                    paginate = Pagination(page)
                    if paginate.paginate():
                        logger.info("Page paginated!")
                    else:
                        logger.info("No more pages to process...")
                        return
                else:
                    logger.info("No more inconsistencies to process...")
                    return
        except TimeoutError:
            logger.error("Exceeded timeout for process")
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
            
            logger.info("Clicking into adjustment button")
            Click.click(page, adjust_button)
            
            adjust_path_buttons = [
                "[btn-radio=\"'CANCELED'\"]",
                "multiselect > div > div > div:nth-child(1) > div > i",
                "label[alt=\"Erro operacional\"]"
            ]
            
            for button in adjust_path_buttons:
                Click.click(page, button)
            
            adjustment_desc = "Cancelamento realizado via Bot: \"Não registrado\""
            page.fill("input#note", adjustment_desc)
            
            logger.info("Clicking into finish adjustment button")
            Click.click(page, "a.btn.button_link.btn-primary.ng-binding")
            
            logger.info("Process completed!")
            return True
        except TimeoutError:
            logger.error("Exceeded timeout for complete")
        except Exception as e:
            logger.error(f"An unexpected error occurred during complete process: {e}", exc_info=True)
            raise

    def restart(self):
        self.execute()
        
        