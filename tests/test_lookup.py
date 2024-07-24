# tests/test_lookup.py

import unittest
from rwanda_locations.lookup import (
    retrieve_districts, retrieve_sectors, retrieve_cells, retrieve_villages
)

class TestLookup(unittest.TestCase):

    def test_retrieve_districts(self):
        districts = retrieve_districts("East")
        self.assertIsInstance(districts, dict)
        self.assertIn("Bugesera", districts)

    def test_retrieve_sectors(self):
        sectors = retrieve_sectors("East", "Bugesera")
        self.assertIsInstance(sectors, dict)
        self.assertIn("Gashora", sectors)

    def test_retrieve_cells(self):
        cells = retrieve_cells("East", "Bugesera", "Gashora")
        self.assertIsInstance(cells, dict)
        self.assertIn("Biryogo", cells)

    def test_retrieve_villages(self):
        villages = retrieve_villages("East", "Bugesera", "Gashora", "Biryogo")
        self.assertIsInstance(villages, list)
        self.assertIn("Bidudu", villages)

if __name__ == '__main__':
    unittest.main()
