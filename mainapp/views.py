from django.http import JsonResponse
from pathlib import Path
from django.shortcuts import render
import json
import datetime as dt
from .Solutions.question1 import getProductionDetails
from .Solutions.question2 import (
    getRunTimeAndDownTime, 
    displayTime, 
    getUtilization
)
from .Solutions.question3 import getresult

PARENT_DIR = Path(__file__).resolve().parent

# Create your views here.
def index(request):
    return render(request, 'index.html')


def question1(request):

    path_to_json_file = PARENT_DIR.joinpath('JsonData','sample_json_1.json')
    with open(path_to_json_file) as f:
        data = json.load(f)
    
    start_time = request.GET.get('start_time')
    end_time = request.GET.get('end_time')

    result = {
        "shiftA" :{ "production_A_count" :0, "production_B_count" :0},
        "shiftB" :{ "production_A_count" :0, "production_B_count" :0},
        "shiftC" :{ "production_A_count" :0, "production_B_count" :0},
    }

    if start_time and end_time:
        result = getProductionDetails(
                    start_time,
                    end_time,
                    data,
                    result
                 )

    return JsonResponse(result)


def question2(request):

    runtime = dt.timedelta(0)
    downtime = dt.timedelta(0)
    utilisation = 0

    path_to_json_file = PARENT_DIR.joinpath('JsonData','sample_json_2.json')
    with open(path_to_json_file) as f:
        data = json.load(f)

    start_time = request.GET.get('start_time')
    end_time = request.GET.get('end_time')

    if start_time and end_time:
        runtime, downtime = getRunTimeAndDownTime(
                                start_time,
                                end_time,
                                data
                            )
    
    utilisation = getUtilization(runtime, downtime)

    return JsonResponse({
                "runtime" : displayTime(runtime),
                "downtime": displayTime(downtime),
                "utilisation": round(utilisation,2)
            })


def question3(request):
    start_time = request.GET.get('start_time')
    end_time = request.GET.get('end_time')

    path_to_json_file = PARENT_DIR.joinpath('JsonData','sample_json_3.json')
    with open(path_to_json_file) as f:
        data = json.load(f)

    result_list = []

    if start_time and end_time:
        result_list = getresult(start_time, end_time, data)
    
    return JsonResponse(result_list, safe=False)
