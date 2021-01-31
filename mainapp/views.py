from django.http import JsonResponse
from pathlib import Path
from django.shortcuts import render
import json
from .Solutions.question1 import getProductionDetails

PARENT_DIR = Path(__file__).resolve().parent

# Create your views here.
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
    pass


def question3(request):
    pass