# api-notas-pruebas

Este proyecto es una API escrita en django como prototipo de funcionamiento para 
varios conceptos:
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

Para que funcione correctamente el proyecto en un equipo local es necesario contar con
rabbitmq y redis.  Postgres es opcional.  Para solventar esto existe un archivo
docker-compose.yml en la raíz del proyecto de django con la configuración correcta
de esos servicios para ser ejecutados en contenedores.

Condiciones para desplegar en DO app platform:
1. El proyecto django no debe estar en carpetas internas, debe ser la raiz
   del repositorio y del proyecto.
2. Si se va a utilizar celery, es preferible usar redis como message broker y
   como result backend, esto debido a que es más fácil usar un servicio de redis
   administrado y configurarlo en el proyecto.

## Conclusión

Es posible usar DO app platform pero resulta muy caro su uso, por ejemplo,
se deben pagar por cada uno de los siguientes servicios:
- La app principal
- El worker de celery
- El worker de celery beat
- La base de datos postgres administrada
- El servicio de redis administrado