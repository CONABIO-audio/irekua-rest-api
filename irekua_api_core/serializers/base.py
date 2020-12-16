from rest_framework import serializers
from irekua_api_core.fields import SelectField


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
