import json
from django.core.exceptions import ValidationError as DjangoValidationError
from django.core.exceptions import PermissionDenied as DjangoPermissionDenied

from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.exceptions import PermissionDenied
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action
from rest_framework.response import Response
from crispy_forms.utils import render_crispy_form

from irekua_upload.models import Operation
from irekua_api_core.views import IrekuaReadOnlyViewSet
from irekua_api_operations import serializers


TEMPLATE_NAME = 'irekua_api_operations/result.html'


class OperationRenderer(BrowsableAPIRenderer):
    def get_post_form(self, renderer_context):
        view = renderer_context['view']
        request = renderer_context['request']
        operation = view.get_object().get_operation()
        form = operation.get_form(request)
        return render_crispy_form(form, context=renderer_context)

    def get_context(self, data, accepted_media_type, renderer_context):
        context = super().get_context(data, accepted_media_type, renderer_context)
        context['post_form'] = self.get_post_form(renderer_context)

        content = json.loads(context['content'])
        if 'result' in content:
            context['content'] = json.dumps(content['result'], indent=4)

        return context


class OperationViewSet(IrekuaReadOnlyViewSet):
    queryset = Operation.objects.all()

    serializer_action_classes = {
        'retrieve': serializers.OperationDetailSerializer
    }

    serializer_class = serializers.OperationSerializer

    @action(
        detail=True,
        methods=['post'],
        renderer_classes=[JSONRenderer, OperationRenderer],
    )
    def run(self, request, pk=None):
        operation = self.get_object().get_operation()

        try:
            request.accepted_renderer.template = TEMPLATE_NAME
        except Exception as error:
            pass

        try:
            data = operation.dispatch(request)

        except DjangoPermissionDenied as error:
            raise PermissionDenied(error) from error

        except DjangoValidationError as error:
            raise ValidationError(error.message_dict) from error

        if data['stderr']:
            st = status.HTTP_500_INTERNAL_SERVER_ERROR
        else:
            st = status.HTTP_200_OK

        return Response(data, status=st)
