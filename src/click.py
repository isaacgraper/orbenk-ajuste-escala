import logging
logger = logging.getLogger(f"{__name__}.Click")

class Click:
    @staticmethod
    def click(page, element, delay=1000, timeout=60000, force=False):
        try:
            el = page.locator(element)
            el.scroll_into_view_if_needed()

            el.wait_for(state='visible', timeout=timeout)
            
            try:
                el.click(delay=delay, timeout=timeout, force=force)
            except:
                try:
                    el.click(delay=delay, timeout=timeout, force=True)
                except:
                    page.evaluate('element => element.click()', el)
            
            page.wait_for_load_state('load')
        except Exception as e:
            logging.error(f"Failed to click on {element}: {str(e)}")
            raise