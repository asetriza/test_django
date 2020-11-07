from django.http import JsonResponse
from django.http import request

# Create your views here.


def flights(request):
    page_num = request.GET.get("page", 1)
    comments = [
        {
            "name": "Asset",
        },
        {
            "name": "Asset2",
        },
    ]

    return JsonResponse({"comments": comments})


def flight(request):
    id = request.GET.get("id", 1)
    comments = {
        "name": "Asset",
    }
    return JsonResponse({"comments": comments})