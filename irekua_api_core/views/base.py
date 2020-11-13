# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class IrekuaViewSet(GenericViewSet):
    def get_serializer_class(self):
        """
        Look for serializer class in self.serializer_action_classes, which
        should be a dict mapping action name (key) to serializer class (value),
        i.e.:

        class MyViewSet(MultiSerializerViewSetMixin, ViewSet):
            serializer_class = MyDefaultSerializer
            serializer_action_classes = {
               'list': MyListSerializer,
               'my_action': MyActionSerializer,
            }

            @action
            def my_action:
                ...

        If there's no entry for that action then just fallback to the regular
        get_serializer_class lookup: self.serializer_class, DefaultSerializer.

        """
        try:
            return self.serializer_action_classes[self.action]

        except (KeyError, AttributeError):
            return super().get_serializer_class()

    def get_permissions(self):
        try:
            permission_classes = self.permission_action_classes[self.action]

        except (KeyError, AttributeError):
            permission_classes = self.permission_classes

        return [permission() for permission in permission_classes]


class IrekuaReadOnlyViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, IrekuaViewSet
):
    pass


class IrekuaModelViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    IrekuaViewSet,
):
    pass
