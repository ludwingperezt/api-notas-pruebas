from rest_framework import serializers
from notas.models import Nota

class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = ['id', 'titulo', 'texto',]
    