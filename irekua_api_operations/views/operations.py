import contextlib

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from irekua_upload.models import Operation
from irekua_api_core.views import IrekuaReadOnlyViewSet
from irekua_api_operations import serializers


@contextlib.contextmanager
def capture():
    import sys
    from io import StringIO

    oldout, olderr = sys.stdout, sys.stderr

    try:
        out = [StringIO(), StringIO()]
        sys.stdout, sys.stderr = out
        yield out

    finally:
        sys.stdout, sys.stderr = oldout, olderr
        out[0] = out[0].getvalue()
        out[1] = out[1].getvalue()


class OperationViewSet(IrekuaReadOnlyViewSet):
    queryset = Operation.objects.all()

    serializer_action_classes = {
        'retrieve': serializers.OperationDetailSerializer
    }

    serializer_class = serializers.OperationSerializer

    def get_template_names(self):
        names = super().get_template_names()
        print('template names', names)
        return names

    @action(detail=True, methods=['post'])
    def run(self, request, pk=None):
        operation = self.get_object().get_operation()

        if not operation.has_run_permission(request):
            return Response(status=status.HTTP_403_Forbidden)

        with capture() as out:
            result = operation.run()

        data = {
            'result': result,
            'stdout': out[0],
            'stderr': out[1],
        }

        return Response(
            data,
            status=status.HTTP_200_OK,
            template_name='irekua_api_operations/result.html')
