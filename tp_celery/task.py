from math import sqrt, log10
from celery import celery

@celery.task
def log(elemento) -> int:
    return log10(int(elemento))

@celery.task
def raiz(elemento) -> int:
    return sqrt(int(elemento))

@celery.task
def pot(elemento) -> int:
    return int(elemento)**int(elemento)