from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, generics, permissions
import device_apis.serializers as api_serializers
from device_apis.models import Devices, DeviceSold, User
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import authenticate

# Create your views here.
@api_view(["GET"])
def home(request):
    message = {"message": "Hello, world"}
    return Response(message, status=200)


@api_view(["GET", "DELETE", "PUT"])
def list_devices(request):
    devices = [{"id": 1, "name": "MI 1", },
               {"id": 2, "name": "MI 2", },
               {"id": 3, "name": "Iphone 13", },
               {"id": 4, "name": "MI 4"}]
    return Response(devices, status=200)


class DeviceCreateView(generics.ListCreateAPIView):
    serializer_class = api_serializers.DeviceSerializer


queryset = Devices.objects.all()
permission_classes = [permissions.IsAuthenticated]


def post(self, request, *args, **kwargs):
    print("request.data", self.request.data)
    return Response({"message": "Device created successfully"}, status=200)


class UserRegister(generics.GenericAPIView):
    serializer_class = api_serializers.UserRegisterSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        print("request.data", self.request.data)
        check_valid_data = self.serializer_class(data=self.request.data)
        if check_valid_data.is_valid(raise_exception=True):
            user = check_valid_data.create(validated_data=check_valid_data.validated_data)
            return Response({"userId": user.id,
                             "message": "User created successfully"}, status=200)
        return Response({"message": "Invalid request",
                        "error": self.serializer_class.errors}, status=400)


class UserLogin(generics.GenericAPIView):
    serializer_class = api_serializers.UserLoginTokenSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        print("request.data", self.request.data)
        check_valid_request = self.serializer_class(data=self.request.data)
        if check_valid_request.is_valid(raise_exception=True):
            user = authenticate(username=check_valid_request.validated_data['username'],
                                password=check_valid_request.validated_data['password'])
            if user:
                token = AccessToken.for_user(user)
                return Response({"userId": user.id, "token": str(token)}, status=200)
            return Response({"message": "Invalid credentials"}, status=400)
