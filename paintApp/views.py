from django.shortcuts import render

from django.http import HttpResponse
import json
from paintApp.vrp import routePlot

# from .models import Question


# Create your views here.
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def vote2(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def index(request):
    # return HttpResponse("You're voting on question %s.")
    return render(request, 'paintApp/templates/index.html')


def opt(request):
    print(request.content_params)       # url 请求参数
    route = json.loads(request.POST.get('route'))   # 线路
    pickup = json.loads(request.POST.get('pickup')) # 提货点
    delivery = json.loads(request.POST.get('delivery')) # 需求点
    vehicle = json.loads(request.POST.get('vehicle'))   # 车辆
    #  重量图
    routePlot.weight(route, vehicle)
    return render(request, 'paintApp/templates/index.html')