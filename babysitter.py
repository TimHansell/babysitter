#
# Hardcoded implementation of the one hour time slots for babysitting
#
timeSlots = [ '5pm', '6pm', '7pm', '8pm', '9pm', '10pm', '11pm', '12am', '1am', '2am', '3am', '4am']

def validTimeSlot( slot ):
    return slot in timeSlots

def validTimeRange( start, end ):
    return (validTimeSlot(start) and
            validTimeSlot(end)  and
            timeSlots.index(start) < timeSlots.index(end))

def getTimeRange( start, end ):
    if validTimeRange(start, end ):
        return timeSlots[ timeSlots.index(start):timeSlots.index(end)]

# Initial implementation of prices - hardcoded as a dictionary of lists
#
class FamilyRate(object):

    def __init__(self, defaultRate):
        self.rates = {}
        for hour in timeSlots:
            self.rates[hour] = defaultRate

    def setRate(self, slot, rate):
        self.rates[slot] = rate

    def setRateRange(self, start, end, rate):
        if validTimeRange(start, end):
            for hour in getTimeRange(start, end):
                self.rates[hour] = rate

    def getRate(self, slot):
        if slot in timeSlots:
            return self.rates[slot]
        else:
            return 0

#
# the babysitter function takes a starttime and endtime as strings in the form ##am or ##pm
# and a family name as a string (currently 'A' 'B' 'C' are the hardcoded families
#
def babysitter( starttime, endtime, family ):
    families = {}
    families['A'] = FamilyRate(20)
    families['A'].setRateRange('5pm', '11pm', 15)

    families['B'] = FamilyRate(16)
    families['B'].setRateRange('5pm', '10pm', 12)
    families['B'].setRateRange('10pm', '12am', 8)

    families['C'] = FamilyRate(15)
    families['C'].setRateRange('5pm', '9pm', 21)

    if  not validTimeSlot(starttime):
        return 'Start Time is invalid'
    elif not validTimeSlot(endtime):
        return 'End Time is invalid'
    elif not validTimeRange(starttime, endtime):
        return 'Invalid Time Range'
    elif family not in families:
        return 'Family Invalid'
    else:
        total = 0
        for hour in getTimeRange( starttime, endtime ):
            total = total + families[family].getRate(hour)
        return total
