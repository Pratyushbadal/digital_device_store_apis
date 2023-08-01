from abc import ABC

from rest_framework import serializers
from device_apis.models import Devices, DeviceSold, User


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = '__all__'

        def create(self, validated_data):
            device = Devices.objects.create(**validated_data)
            device.save()
            return device


class DeviceSoldSerializer(serializers.Serializer):
    device_id = serializers.IntegerField()

    def create(self, validated_data):
        device_sold = DeviceSold.objects.create(**validated_data)
        device_sold.save()
        return device_sold


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


class DeviceUpdateSerializer(serializers.Serializer):
    name = serializers.CharField()
    model = serializers.CharField()
    price = serializers.IntegerField()
    description = serializers.CharField()
    ram = serializers.CharField()
    internal_storage = serializers.CharField()
    battery = serializers.CharField()
    camera = serializers.CharField()
    processor = serializers.CharField()

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.model = validated_data.get('model', instance.model)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.ram = validated_data.get('ram', instance.ram)
        instance.internal_storage = validated_data.get('internal_storage', instance.internal_storage)
        instance.battery = validated_data.get('battery', instance.batery)
        instance.camera = validated_data.get('camera', instance.camera)
        instance.processor = validated_data.get('processor', instance.processor)
        instance.save()
        return instance
