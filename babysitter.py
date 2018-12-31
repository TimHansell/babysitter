#
# Initial implementation of prices - hardcoded as a dictionary of lists
#

families = { 'A': [15,15,15,15,15,15,20,20,20,20,20],
             'B': [12,12,12,12,12,8,8,16,16,16,16],
             'C': [21,21,21,21,15,15,15,15,15,15,15] }

def inValidFamily( family ):
    return families.get(family) == None

def convertTime( time ):
    if time.endswith('pm'):
        return int(time[0:time.find('pm')])
    elif time.endswith('am'):
        return int(time[0:time.find('am')]) + 12
    else:
        return -1

def babysitter( starttime, endtime, family ):
    if convertTime(starttime) <  5 or convertTime(starttime) > 15:
        return 'Start Time is invalid'
    elif convertTime(endtime) > 16 or convertTime(endtime) < 6:
        return 'End Time is invalid'
    elif inValidFamily(family):
        return 'Family Invalid'
    else:
        total = 0
        for i in range(convertTime(starttime), convertTime(endtime)):
            total = total + families[family][i-5]
        return total
