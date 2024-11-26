import logging
logger = logging.getLogger(f"{__name__}.Page")

class Page:
    
    @staticmethod
    def click(page, element, delay, timeout):
        try:
            el = page.locator(element)
            el.wait_for(state="visible")
            el.hover()
            el.click(force=True, delay=delay, timeout=timeout)
            
            page.wait_for_selector(".js-loader-container", state="hidden", timeout=120000)

            page.wait_for_load_state('load')
        except Exception as e:
            logging.error(f"Failed to click on {element}: {str(e)}")
            raise