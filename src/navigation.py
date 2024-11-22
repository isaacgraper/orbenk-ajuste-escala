import config.logging as log
log.set_logging()

import logging
logger = logging.getLogger(f"{__name__}.Navigation")

class Navigation:
    def __init__(self, page):
        self.page = page

        
    