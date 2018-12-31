import unittest
from babysitter import *

class BabySitterTests( unittest.TestCase ):

    def test_convertTimeReturnsNumber(self):
        self.assertEqual( 5, convertTime('5pm'))
        self.assertEqual( 16, convertTime('4am'))

    def test_babysitterStartTimeIsInvalid(self):
        self.assertEqual( 'Start Time is invalid', babysitter('A', '4pm', '7pm'))
        self.assertEqual( 'Start Time is invalid', babysitter('A', '5am', '7am'))

    def test_babysitterEndTimeIsInvalid(self):
        self.assertEqual( 'End Time is invalid', babysitter('A', '5pm', '5am'))
        self.assertEqual( 'End Time is invalid', babysitter('A', '6pm', '5pm'))

if __name__ == '__main__':
    unittest.main()
