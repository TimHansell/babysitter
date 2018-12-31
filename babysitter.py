
def convertTime( time ):
    if time.endswith('pm'):
        return int(time[0:time.find('pm')])
    elif time.endswith('am'):
        return int(time[0:time.find('am')]) + 12
    else:
        return -1

def babysitter( family, starttime, endtime ):
    if convertTime(starttime) <  5 or convertTime(starttime) > 15:
        return 'Start Time is invalid'
    elif convertTime(endtime) > 16 or convertTime(endtime) < 6:
        return 'End Time is invalid'
    else:
        return 'fail'
