from celery import Celery
from async_tasks.config_celery import Config



app = Celery('tasks', broker=Config.REDIS_HOST)

if __name__ == '__main__':
    app.worker_main()
