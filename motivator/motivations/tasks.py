from celery import shared_task
from .models import Motivation

@shared_task
def make_motivation_visible():
    Motivation.objects.filter(is_visible=False).update(is_visible=True)
