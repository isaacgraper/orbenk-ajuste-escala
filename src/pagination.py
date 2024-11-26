import logging
logger = logging.getLogger(f"{__name__}.Pagination")

from src.page import Page

class Pagination:
    def __init__(self, page):
        self.page = page
    
    def paginate(self):
        try:
            logger.info("Waiting for next page button to be visible...")
            self.page.wait_for_selector("[ng-click=\"changePage('next')\"]", state="visible", timeout=0)
            
            el = self.page.locator("[ng-click=\"changePage('next')\"]")
            if el.count() == 0:
                logger.info("No more pages to process.")
                return False
            
            logger.info("Clicking next page button")
            Page.click(self.page, "[ng-click=\"changePage('next')\"]", 2000, 0)
            
            self.page.wait_for_load_state('load')

            logger.info("Successfully paginated to the next page!")
            return True
        except Exception as e:
            logger.error(f"An unexpected error occurred during pagination: {e}", exc_info=True)
            return False