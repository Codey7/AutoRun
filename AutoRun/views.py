from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json

from AutoRun.models import User
# Create your views here.
def index(request) :
    return HttpResponse("Hello world!")

@require_http_methods(["GET"])
def show_user(request):
    response = {}
    try:
        users = User.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", users))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

