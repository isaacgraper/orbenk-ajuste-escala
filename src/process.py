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
        self.headless_mode = headless_mode
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
        except Exception as e:
            logger.info(f"An exception occurred in execute process: {e}")
    
    def handler(self, page):    
        return
    
    def start(self, page):
        logger.info("Starting process...")

        try:    
            action = Action(page)
            action.select_all_rows()
            
            self.complete(page)
            
            paginate = Pagination(page)
            paginate.paginate()
            
            time.sleep(30)
        except Exception as e:
            logger.info(f"An exception occurred in start process: {e}")
            
    def complete(self, page):
        
        adjust_button = "div.filters-right > button"
        
        page.wait_for_selector(adjust_button, state="visible")
        page.click(adjust_button, delay=250)
        
        adjust_path_buttons = ["[btn-radio=\"'CANCELED'\"]",
                               "multiselect > div > div > div:nth-child(1) > div > i", 
                               "label[alt=\"Erro operacional\"]"]
        
        for button in adjust_path_buttons:
            page.click(button, delay=250)
        
        # Descrição para "Não registrado"
        adjustment_desc = "Cancelamento realizado via Bot: \"Não registrado\""
        page.fill("input#note", adjustment_desc)
        
        page.wait_for_selector("a.btn.button_link.btn-primary.ng-binding")
        page.click("a.btn.button_link.btn-primary.ng-binding", delay=250)
        
        