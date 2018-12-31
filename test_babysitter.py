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

if __name__ == '__main__':
    unittest.main()
