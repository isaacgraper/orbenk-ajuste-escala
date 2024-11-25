import logging
logger = logging.getLogger(f"{__name__}.Pagination")

class Pagination:
    def __init__(self, page):
        self.page = page
    
    def paginate(self):
    
        try:
            logger.debug("Waiting for next page button to be visible...")
            self.page.wait_for_selector("[ng-click=\"changePage('next')\"]", state="visible")
        
            logger.debug("Clicking next page button...")
            self.page.click("[ng-click=\"changePage('next')\"]", delay=250, timeout=0)
            
            # verificar se tiver mais paginas
        
            self.page.wait_for_load_state('load')
            self.page.wait_for_timeout(500)
            
            logger.info("Successfully paginated to the next page.")
            return 
        except Exception as e:
            logger.error(f"An unexpected error occurred during pagination: {e}", exc_info=True)