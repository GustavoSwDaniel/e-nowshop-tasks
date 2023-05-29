from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379')

if __name__ == '__main__':
    app.worker_main()