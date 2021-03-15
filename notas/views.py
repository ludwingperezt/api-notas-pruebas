from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from notas.models import Nota
from notas.serializers import NotaSerializer
from notas.tasks import log_nota

class NotaViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer
    permission_classes = [permissions.AllowAny,]

    def perform_create(self, serializer):
        nota = serializer.save()
        id_nota = serializer.data['id']
        log_nota.delay(id_nota)