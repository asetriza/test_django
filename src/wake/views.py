from django.http import JsonResponse
from django.http import request

# Create your views here.


def wake(request):
    wake_message = {
        "Status": 200,
        "Message": "Ok",
        "Wake": "Waked",
        }

    return JsonResponse({"wake_message": wake_message})
