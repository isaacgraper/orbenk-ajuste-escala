import logging
logger = logging.getLogger(f"{__name__}.Action")

class Action:
    def __init__(self, page):
        self.page = page

    def select_all_rows(self):
        try:
            logger.info("Selecting all rows in the table...")
            
            checkbox_selector = "div.content-table > table > thead > tr > th:nth-child(1) > label > i"
            
            self.page.wait_for_selector(checkbox_selector, state="visible")
            self.page.click(checkbox_selector, delay=250)
        except Exception as e:
            logger.error(f"Error while selecting rows: {e}", exc_info=True)

    def has_more_data(self) -> bool:
        try:
            logger.info("Checking if has more data...")
            
            return False
        except Exception as e:
            logger.error(f"Error during custom table action: {e}", exc_info=True)
    
    def has_modal(self) -> bool:
        pass
