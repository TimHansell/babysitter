#
# Initial implementation of prices - hardcoded as a dictionary of lists
#

families = { 'A': [15,15,15,15,15,15,20,20,20,20,20],
             'B': [12,12,12,12,12,8,8,16,16,16,16],
             'C': [21,21,21,21,15,15,15,15,15,15,15] }

timeSlots = [ '5pm', '6pm', '7pm', '8pm', '9pm', '10pm', '11pm', '12am', '1am', '2am', '3am', '4am']

def babysitter( starttime, endtime, family ):
    if  starttime not in timeSlots or starttime == '4am':
        return 'Start Time is invalid'
    elif endtime not in timeSlots or endtime == '5pm':
        return 'End Time is invalid'
    elif not timeSlots.index(starttime) < timeSlots.index(endtime):
        return 'Invalid Time Range'
    elif family not in families:
        return 'Family Invalid'
    else:
        total = 0
        for i in range(timeSlots.index(starttime), timeSlots.index(endtime)):
            total = total + families[family][i]
        return total
