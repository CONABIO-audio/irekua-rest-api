from rest_framework import serializers
from rest_framework.relations import ObjectDoesNotExist
from rest_framework.relations import ObjectValueError
from rest_framework.relations import ObjectTypeError


class hashabledict(dict):
    def __hash__(self):
        return hash(tuple(sorted(self.items())))


class SelectField(serializers.HyperlinkedRelatedField):
    def to_internal_value(self, data):
        try:
            return self.get_object(None, None, {self.lookup_url_kwarg: data})
        except (ObjectDoesNotExist, ObjectValueError, ObjectTypeError):
            self.fail("does_not_exist")
        return super().to_internal_value(data)

    def to_representation(self, value):
        return hashabledict(id=value.pk, url=super().to_representation(value))
