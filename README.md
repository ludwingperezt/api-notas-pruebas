# api-notas-pruebas

Este proyecto es una API escrita en django como prototipo de funcionamiento para varios conceptos:
- Despligue en DigitalOcean app platform
- Uso básico de celery
- Uso básico de celery beat
- Funcionamiento de celery y celery beat en DigitalOcean app platform.

Se trata de una aplicación de notas, cada una tiene un título y un texto asociado.
La fecha de creación de cada nota se apunta en una entidad de nombre LogNota, la
cual está asociada a cada nota y se inserta mediante una llamada a una función
asíncrona utilizando celery (solo para demostrar el funcionamiento).

También existe una función asíncrona de nombre tarea_periodica que inserta entidades
en una tabla de nombre LogTareaPeriodica solo para verificar que el sistema de 
tareas programadas/repetitivas (celery beat) está funcionando.
