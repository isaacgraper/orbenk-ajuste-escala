import logging
logger = logging.getLogger(f"{__name__}.State")

from playwright.sync_api import expect

from src.click import Click

class State:
    
    @staticmethod
    def check_has_modal_load_content(page):
        try:
            modal = page.wait_for_selector("div.js-content-load", state="visible", timeout=0)
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
        try:
            modal = page.locator("div.modal-content")
            
            is_visible = modal.evaluate(
                "(el) => el.offsetWidth > 0 && el.offsetHeight > 0 && window.getComputedStyle(el).visibility !== 'hidden'"
            )
            
            if is_visible:
                Click.click(page, "div.close")
                return True
            else:
                return False
        except Exception as e:
            logger.error(f"Error while checking if modal apperead: {e}")
            return False
        
    
    @staticmethod
    def check_has_more_data(page):
        try:
            logger.info("Checking if has more data...")
            
            return False
        except Exception as e:
            logger.error(f"Error during custom table action: {e}", exc_info=True)