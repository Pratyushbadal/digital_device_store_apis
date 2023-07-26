from django.http import HttpResponse, JsonResponse

# Create your views here.


def home(request):
    return HttpResponse("Hello world", status=200)

