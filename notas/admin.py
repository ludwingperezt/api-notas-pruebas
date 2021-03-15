from django.contrib import admin
from notas.models import Nota, LogNota, LogTareaPeriodica

admin.site.register(Nota)
admin.site.register(LogNota)
admin.site.register(LogTareaPeriodica)