import logging
logger = logging.getLogger(f"{__name__}.Click")

class Click:
    
    @staticmethod
    def click(page, element, delay, timeout):
        try:
            el = page.locator(element)
            el.wait_for(state="visible")
            el.hover()
            el.click(force=True, delay=delay, timeout=timeout)
            
            page.wait_for_load_state('load')
        except Exception as e:
            logging.error(f"Failed to click on {element}: {str(e)}")
            raise
        
    @staticmethod
    def safe_click(page, element, delay, timeout, blocking_selector=None):
        try:
            el = page.locator(element)
            el.wait_for(state="visible", timeout=timeout)

            if blocking_selector:
                logging.info("Waiting for blocking element to disappear...")
                page.wait_for_selector(blocking_selector, state="hidden", timeout=timeout)

            logging.info(f"Hovering over {element}")
            el.hover()

            logging.info(f"Clicking on {element}")
            el.click(force=True, delay=delay, timeout=timeout)

            page.wait_for_load_state('load')
            logging.info("Click action completed successfully.")
        except Exception as e:
            logging.error(f"Failed to click on {element}: {str(e)}")
            raise