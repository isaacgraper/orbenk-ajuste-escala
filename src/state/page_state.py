import logging
logger = logging.getLogger(f"{__name__}.State")

class State:
    
    @staticmethod
    def check_has_modal_load_content(page):
        try:
            modal = page.wait_for_selector("div.js-content-load", state="visible", timeout=10000)
            if modal:
                logger.info("Modal content appeared")

                while True:
                    display_value = page.evaluate(
                        """() => {
                            const element = document.querySelector("div.js-loader-container");
                            return element ? window.getComputedStyle(element).display : null;
                        }"""
                    )
                    
                    if display_value == "none":
                        logger.info("Modal disappeared")
                        break
                    
                    logger.info("Waiting for modal to disappear...")
                    page.wait_for_timeout(2000)
            else:
                logger.warning("Modal content did not load within the timeout period.")
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