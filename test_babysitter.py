import unittest
from babysitter import *

class BabySitterTests( unittest.TestCase ):

    def test_convertTimeReturnsNumber(self):
        self.assertEqual( 5, convertTime('5pm'))
        self.assertEqual( 16, convertTime('4am'))

    def test_babysitterStartTimeIsInvalid(self):
        self.assertEqual( 'Start Time is invalid', babysitter('4pm', '7pm', 'A'))
        self.assertEqual( 'Start Time is invalid', babysitter('5am', '7am', 'B'))

    def test_babysitterEndTimeIsInvalid(self):
        self.assertEqual( 'End Time is invalid', babysitter('5pm', '5am', 'A'))
        self.assertEqual( 'End Time is invalid', babysitter('6pm', '5pm', 'C'))

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
