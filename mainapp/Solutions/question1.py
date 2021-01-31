import datetime as dt

SHIFT_A_START = dt.time(6, 0, 0)
SHIFT_B_START = dt.time(14, 0, 0)
SHIFT_C_START = dt.time(20, 0, 0)

def getProductionDetails(start_time, end_time, data, result):

    start_time = dt.datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%SZ')
    end_time = dt.datetime.strptime(end_time, '%Y-%m-%dT%H:%M:%SZ')

    for obj in data:
        cur_time = dt.datetime.strptime(obj["time"], '%Y-%m-%d %H:%M:%S')
        if start_time <= cur_time <= end_time:
            if SHIFT_A_START < cur_time.time() < SHIFT_B_START:
                shift = 'shiftA'
            elif SHIFT_B_START < cur_time.time() < SHIFT_C_START:
                shift = 'shiftB'
            else:
                shift = 'shiftC'

            if obj['production_A'] :
                result[shift]['production_A_count'] += 1
            
            if obj['production_B'] :
                result[shift]['production_B_count'] += 1
    
    return result