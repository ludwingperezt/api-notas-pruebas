from django.db import models

class Nota(models.Model):
    """
    """
    titulo = models.TextField(verbose_name='Titulo', blank=False, null=False)
    texto = models.TextField(verbose_name='Texto', blank=True, null=True)

    def __str__(self):
        return self.titulo

class LogNota(models.Model):
    nota = models.ForeignKey(Nota, on_delete=models.CASCADE)
    fecha_creacion         = models.DateTimeField(auto_now_add=True)
    fecha_modificacion     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nota.titulo


class LogTareaPeriodica(models.Model):
    fecha_creacion         = models.DateTimeField(auto_now_add=True)