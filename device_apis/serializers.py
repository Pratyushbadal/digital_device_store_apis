from rest_framework import serializers
from device_apis.models import Devices, DeviceSold, User


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = '__all__'


class DeviceSoldSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceSold
        # validate all the fields/columns
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # validate the given fields
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])  # set the password
        user.save()
        return user


class UserLoginTokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
