from celery import shared_task
from notas.models import Nota, LogNota, LogTareaPeriodica
from django.utils import timezone

@shared_task(ignore_result=True)
def log_nota(id_nota):
    nota = Nota.objects.get(pk=id_nota)
    LogNota.objects.create(nota=nota)

@shared_task(ignore_result=True)
def tarea_periodica():
    LogTareaPeriodica.objects.create()