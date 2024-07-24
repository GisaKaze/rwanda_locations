# tests/test_data.py

import unittest
from rwanda_locations.data import (
    get_provinces, get_districts_from_province, get_sectors_from_district,
    get_cells_from_sector, get_villages_from_cell, get_all_children
)

class TestData(unittest.TestCase):

    def test_get_provinces(self):
        provinces = get_provinces()
        self.assertIsInstance(provinces, dict)
        self.assertIn('East', provinces)

    def test_get_districts_from_province(self):
        districts = get_districts_from_province('East')
        self.assertIsInstance(districts, dict)
        self.assertIn('Bugesera', districts)

    def test_get_sectors_from_district(self):
        sectors = get_sectors_from_district('East', 'Bugesera')
        self.assertIsInstance(sectors, dict)
        self.assertIn('Gashora', sectors)

    def test_get_cells_from_sector(self):
        cells = get_cells_from_sector('East', 'Bugesera', 'Gashora')
        self.assertIsInstance(cells, dict)
        self.assertIn('Biryogo', cells)

    def test_get_villages_from_cell(self):
        villages = get_villages_from_cell('East', 'Bugesera', 'Gashora', 'Biryogo')
        self.assertIsInstance(villages, list)
        self.assertIn('Rugunga', villages)

    def test_get_all_children_provinces(self):
        children = get_all_children()
        self.assertIsInstance(children, dict)
        self.assertIn('East', children)

    def test_get_all_children_districts(self):
        children = get_all_children(province='East')
        self.assertIsInstance(children, dict)
        self.assertIn('Bugesera', children)

    def test_get_all_children_sectors(self):
        children = get_all_children(province='East', district='Bugesera')
        self.assertIsInstance(children, dict)
        self.assertIn('Gashora', children)

    def test_get_all_children_cells(self):
        children = get_all_children(province='East', district='Bugesera', sector='Gashora')
        self.assertIsInstance(children, dict)
        self.assertIn('Biryogo', children)

    def test_get_all_children_villages(self):
        children = get_all_children(province='East', district='Bugesera', sector='Gashora', cell='Biryogo')
        self.assertIsInstance(children, list)
        self.assertIn('Bidudu', children)


if __name__ == '__main__':
    unittest.main()
