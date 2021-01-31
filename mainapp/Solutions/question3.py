import datetime as dt
from collections import defaultdict
import re

def defaultDictValue():
    return (
        {
            "total_belt1" : 0,
            "total_belt2" : 0,
            "count" : 0,
        }
    )

def getOnlyDigits(s):
    return int(re.search('[0-9]+',s).group())

def makeResultObj(key, obj):
    return (
        {
            'id' : key,
            'avg_belt1' : obj['total_belt1'],
            'avg_belt2' : obj['total_belt2']
        }
    )


def getresult(start_time, end_time, data):

    start_time = dt.datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%SZ')
    end_time = dt.datetime.strptime(end_time, '%Y-%m-%dT%H:%M:%SZ')

    result_dict = defaultdict(defaultDictValue)

    for obj in data:
        cur_time = dt.datetime.strptime(obj["time"], '%Y-%m-%d %H:%M:%S')
        if start_time <= cur_time <= end_time:
            # print(obj['id'])
            key = getOnlyDigits(obj['id'])
            if obj['state']:
                # belt1 value is to be considered 0 when the state is True
                result_dict[key]['total_belt2'] += obj['belt2']
            else:
                # belt2 value is to be considered 0 when the state is False
                result_dict[key]['total_belt1'] += obj['belt1']
            result_dict[key]['count'] += 1

    for key in result_dict:
        result_dict[key]['total_belt1'] //= result_dict[key]['count']
        result_dict[key]['total_belt2'] //= result_dict[key]['count']

    result_list = []
    for key in sorted(result_dict.keys()):
        result_list.append(makeResultObj(key,result_dict[key]))
    
    return result_list
        