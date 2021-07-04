from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
# Create your views here.
@api_view(["GET"])
def hello(request):
    return JsonResponse({"message":"Hello World"})

#  Create URL shortner API
@api_view(['POST'])
def url_encode(request):
    url = request.POST.get('url')
    print("url :", url)
    return JsonResponse({"Message":"200"})
