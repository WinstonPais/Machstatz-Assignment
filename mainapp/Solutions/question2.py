import datetime as dt

def getRunTimeAndDownTime(start_time, end_time, data):

    start_time = dt.datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%SZ')
    end_time = dt.datetime.strptime(end_time, '%Y-%m-%dT%H:%M:%SZ')

    runtime = 0
    downtime = 0

    for obj in data:
        cur_time = dt.datetime.strptime(obj["time"], '%Y-%m-%d %H:%M:%S')
        if start_time <= cur_time <= end_time:
            if obj['runtime'] > 1021:
                runtime += 1021
                downtime += obj['runtime'] - 1021
            else: 
                runtime += obj['runtime']
            
            downtime += obj['downtime']

    return dt.timedelta(seconds=runtime), dt.timedelta(seconds=downtime)


def displayTime(time):
    seconds = time.seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f'{hours}h:{minutes}m:{seconds}s'


def getUtilization(runtime, downtime):
    if runtime.seconds + downtime.seconds:
        return ( runtime.seconds/(runtime.seconds + downtime.seconds) ) * 100
    else:
        return 0