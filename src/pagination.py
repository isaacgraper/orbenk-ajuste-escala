import logging
logger = logging.getLogger(f"{__name__}.Pagination")

from src.click import Click

class Pagination:
    def __init__(self, page):
        self.page = page
    
    def paginate(self):
        try:
            next_page_button = "[ng-click=\"changePage('next')\"]"
            
            self.page.locator(next_page_button)
            if next_page_button.count() == 0:
                logger.info("Change page to next page desapperead")
                return False
             
            logger.info("Waiting for next page button to be visible...")
            self.page.wait_for_selector(next_page_button, state="visible", timeout=60000)
            
            logger.info("Clicking next page button")
            Click.click(self.page, next_page_button)
            
            self.page.wait_for_load_state('load')

            logger.info("Successfully paginated to the next page!")
            return True
        except TimeoutError:
            logger.error("Exceeded timeout for pagination")
        except Exception as e:
            logger.error(f"An unexpected error occurred during pagination: {e}", exc_info=True)
            return False