import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        """Tests the repr definition of class Location"""
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    def test_Location_name(self):
        """Test to see if name returned from function is correct"""
        loc = Location('Santa Cruz', 28.0, 41.0)
        self.assertEqual(loc.name, 'Santa Cruz')

    def test_Location_lat(self):
        """Test to see if lat returned from Location is correct"""
        loc = Location('Santa Cruz', 28.0, 41.0)
        self.assertAlmostEqual(loc.lat, 28.0)

    def test_Location_lon(self):
        """Test to see if lon returned from Location is correct"""
        loc = Location('Santa Cruz', 28.0, 41.0)
        self.assertAlmostEqual(loc.lon, 41.0)

if __name__ == "__main__":
        unittest.main()
