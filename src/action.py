import logging
logger = logging.getLogger(f"{__name__}.Action")

class Action:
    def __init__(self, page):
        self.page = page

    def select_all_rows(self):
        try:
            self.page.wait_for_load_state('load')
            
            logger.info("Selecting all rows in the table...")
            
            checkbox_selector = "div.content-table > table > thead > tr > th:nth-child(1) > label > i"
            
            logger.info("Waiting for checkbox be visible...")
            self.page.wait_for_selector(checkbox_selector, state="visible")
            
            logger.info("Clicking checkbox button...")
            self.page.click(checkbox_selector, delay=1000, timeout=0)
            
            logger.info("Selected all rows in the table!")
            return
        except Exception as e:
            logger.error(f"Error while selecting rows: {e}", exc_info=True)
