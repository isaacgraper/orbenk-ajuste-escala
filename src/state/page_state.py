import logging
logger = logging.getLogger(f"{__name__}.State")

class State:
    
    @staticmethod
    def check_has_modal_load_content(page):
        while True:
            try:
                if page.wait_for_selector("div.js-content-load", state="invisible"):
                    logger.info("Modal content loaded and invisible!")
                    return True
                else:
                    logger.warning("Waiting for modal content to load and become invisible...")
                    page.wait_for_timeout(3000)
            except Exception as e:
                logger.error(f"Error while checking modal content: {e}")
                return False
                
    @staticmethod
    def check_has_modal(page):
        pass
    
    @staticmethod
    def check_has_more_data(page):
        try:
            logger.info("Checking if has more data...")
            
            return False
        except Exception as e:
            logger.error(f"Error during custom table action: {e}", exc_info=True)