import logging
logger = logging.getLogger(f"{__name__}.Pagination")

class Paginatio:
    def __init__(self, page):
        self.page = page
    
    def paginate(self):
        self.page.wait_for_selector("[ng-click=\"changePage('next')\"]", state="visible")
        self.page.click("[ng-click=\"changePage('next')\"]", delay=250)
        
        self.page.wait_for_load_state('load')
        self.page.wait_for_timeout(500)
        
        logger.info("Paginated to the next page...")