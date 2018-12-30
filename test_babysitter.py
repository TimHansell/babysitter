import unittest
from babysitter import *

class BabySitterTests( unittest.TestCase ):
    
    def test_babysitterl( self ):
        self.assertEqual( babysitter('A', 4, 5 ), 'Start Time too early' ); 

unittest.main()
