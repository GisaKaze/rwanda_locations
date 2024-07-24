# rwanda_locations/lookup.py

from .data import (
    get_districts_from_province,
    get_sectors_from_district,
    get_cells_from_sector,
    get_villages_from_cell
)

def retrieve_districts(province):
    return get_districts_from_province(province)

def retrieve_sectors(province, district):
    return get_sectors_from_district(province, district)

def retrieve_cells(province, district, sector):
    return get_cells_from_sector(province, district, sector)

def retrieve_villages(province, district, sector, cell):
    return get_villages_from_cell(province, district, sector, cell)
