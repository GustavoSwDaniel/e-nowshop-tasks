import logging
from os import getenv


class Config:
    APP_ENV = getenv('APP_ENV', 'local')

    ORDER_API_URL = getenv('ORDER_API_URL', 'http://localhost:8081')
    REDIS_HOST = getenv('REDIS_HOST', 'redis://default:SAqnNRV1EJ30HNOmEbAQdVTSuZfOC4h7@redis-12445.c284.us-east1-2.gce.cloud.redislabs.com:12445')
    REDIS_USER = getenv('REDIS_USER', '')
    REDIS_PASSWORD = getenv('REDIS_PASSWORD', '')
