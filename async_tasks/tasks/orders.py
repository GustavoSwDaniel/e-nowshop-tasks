import logging
from app import app
import time
import requests
from config import Config
logger = logging.getLogger(__name__)


@app.task
def decrement_product_of_inventory(order_uuid):

    time.sleep(5)
    logger.info(f'Decrement product of inventory {order_uuid}')
    response = requests.patch(f'{Config.ORDER_API_URL}/orders/{order_uuid}/products/decrement')
    if response.status_code != 204:
        logger.info(f'Error to decrement product of inventory {order_uuid}')