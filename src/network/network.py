import logging
logger = logging.getLogger(f"{__name__}.Network")

from src.filter import Filter

def capture_response_on_filter(page, target):
    response_data = None

    def handle_response(response):
        nonlocal response_data
        
        if target in response.url:
            try:
                logger.info(f"Waiting for \"{response.url}\" data")
                response_data = response.json()
            except Exception as e:
                logger.error(f"An error occurred during handle response: {e}")

    page.on("response", handle_response)

    while response_data is None:
        logger.info("Waiting for data to be retrieved...")
        page.wait_for_timeout(500)
    
    if response_data is None:
        logger.error(f"Response not captured in the given target: {target}")

    return response_data
