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
                filter.apply_filter()
                
                self.start(browser.page)
                logger.warning("Process has been stopped!")
        except Exception as e:
            logger.info(f"An exception occurred in execute process: {e}")
            
    def start(self, page):
        logger.info("Starting process...")

        try:
            # verificar registros antes de entrar no looping
            
            
            action = Action(page) # processamento
            while True:
                # condicao de parada do looping, sempre verificar antes de processar a pagina
                
                action.select_all_rows()
                
                if self.complete(page):
                    paginate = Pagination(page)
                    if paginate.paginate(): 
                        logger.info("Page paginated!")
                    else: # nao tem mais pagina
                        logger.info("No more pages to process, ending process...")
                        return
            
        except Exception as e:
            logger.info(f"An exception occurred in start process: {e}")
            
    def complete(self, page):
        adjust_button = "div.filters-right > button"
        
        page.wait_for_selector(adjust_button, state="visible")
        page.click(adjust_button, delay=500)
        
        adjust_path_buttons = ["[btn-radio=\"'CANCELED'\"]",
                               "multiselect > div > div > div:nth-child(1) > div > i", 
                               "label[alt=\"Erro operacional\"]"]
        
        for button in adjust_path_buttons:
            page.click(button, delay=500)
        
        adjustment_desc = "Cancelamento realizado via Bot: \"Não registrado\""
        page.fill("input#note", adjustment_desc)
        
        page.wait_for_selector("a.btn.button_link.btn-primary.ng-binding")
        page.click("a.btn.button_link.btn-primary.ng-binding", delay=500, timeout=0)
        
        page.wait_for_load_state('load')
        
        logger.info("Process complete!")
        return True

def restart():
    pass
        
        