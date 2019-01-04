import unittest
from babysitter import *

class BabySitterTests( unittest.TestCase ):

    def test_FamilyRates(self):
        rateA = FamilyRate(10);
        self.assertEqual(10, rateA.getRate( '5pm' ))

    def test_babysitterStartTimeIsInvalid(self):
        self.assertEqual( 'Start Time is invalid', babysitter('4pm', '7pm', 'A'))
        self.assertEqual( 'Start Time is invalid', babysitter('5am', '7am', 'B'))

    def test_babysitterEndTimeIsInvalid(self):
        self.assertEqual( 'End Time is invalid', babysitter('5pm', '5am', 'A'))
        self.assertEqual( 'End Time is invalid', babysitter('6pm', '10am', 'C'))

    def test_babysitterInvalidTimeRange(self):
        self.assertEqual( 'Invalid Time Range', babysitter( '10pm', '9pm', 'A'))

    def test_babysitterFamilyIsInvalid(self):
        self.assertEqual( 'Family Invalid', babysitter('5pm', '10pm', 'D'))

    def test_babysitterFamilyABefore11(self):
        self.assertEqual( 30, babysitter('5pm', '7pm', 'A'))

    def test_babysitterFamilyBMiddleOfNight(self):
        self.assertEqual( 60 , babysitter( '9pm', '2am', 'B'))

    def test_babysitterFamilyCAllNightLong(self):
        self.assertEqual( 189, babysitter( '5pm', '4am', 'C'))

if __name__ == '__main__':
    unittest.main()
