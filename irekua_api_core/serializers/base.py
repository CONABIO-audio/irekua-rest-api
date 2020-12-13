from rest_framework import serializers


class hashabledict(dict):
    def __hash__(self):
        return hash(tuple(sorted(self.items())))


class SelectField(serializers.HyperlinkedRelatedField):
    def to_representation(self, value):
        return hashabledict(id=value.pk, url=super().to_representation(value))


class IrekuaModelSerializer(serializers.ModelSerializer):
    serializer_related_field = SelectField


class IrekuaUserModelSerializer(IrekuaModelSerializer):
    def create(self, validated_data):
        request = self.context["request"]
        validated_data["created_by"] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context["request"]
        validated_data["modified_by"] = request.user
        return instance
