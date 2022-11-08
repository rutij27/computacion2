from celery import Celery

celery = Celery('matriz_calc')

celery.conf.update(
    broker_url = 'redis://localhost:6379/0',
    result_backend ='redis://localhost:6379/0',
    imports = (
        'tasks'
    )
)