import logging
from os import getenv


class Config:
    APP_ENV = getenv('APP_ENV', 'local')

    ORDER_API_URL = getenv('ORDER_API_URL', 'http://localhost:8081')