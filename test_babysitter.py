import unittest
from babysitter import *

class BabySitterTests( unittest.TestCase ):
    
    def test_babysitter( self ):
        self.assertEqual( babysitter('A', '4pm', '5pm' ), 'Start Time too early' ); 

if __name__ == '__main__':
    unittest.main()
