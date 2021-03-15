# Iniciar servicios para celery y celery beat

1. Iniciar el virtualenv
2. Iniciar celery worker
```celery -A apiprueba worker -l INFO```
3. Iniciar celery beat (después del worker de celery y en un proceso separado)
```celery -A apiprueba beat --scheduler django_celery_beat.schedulers:DatabaseScheduler -l INFO```