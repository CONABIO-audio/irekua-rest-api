from rest_framework.serializers import ModelSerializer


class IrekuaModelSerializer(ModelSerializer):
    pass


class IrekuaUserModelSerializer(IrekuaModelSerializer):
    def create(self, validated_data):
        request = self.context["request"]
        validated_data["created_by"] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context["request"]
        validated_data["modified_by"] = request.user
        return instance
