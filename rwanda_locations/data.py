# rwanda_locations/data.py

import json
import os

def get_location_data():
    base_dir = os.path.dirname(__file__)
    data_path = os.path.join(base_dir, 'data', 'locations.json')
    with open(data_path, 'r') as file:
        return json.load(file)

def get_provinces():
    data = get_location_data()
    return dict.fromkeys(data.keys())  # Ensure dict return

def get_districts(province):
    data = get_location_data()
    return dict.fromkeys(data.get(province, {}).keys())  # Ensure dict return

def get_sectors(province, district):
    data = get_location_data()
    return dict.fromkeys(data.get(province, {}).get(district, {}).keys())  # Ensure dict return

def get_cells(province, district, sector):
    data = get_location_data()
    return dict.fromkeys(data.get(province, {}).get(district, {}).get(sector, {}).keys())  # Ensure dict return

def get_villages(province, district, sector, cell):
    data = get_location_data()
    return list(data.get(province, {}).get(district, {}).get(sector, {}).get(cell, []))  # Ensure list return

def get_districts_from_province(province):
    return get_districts(province)

def get_sectors_from_district(province, district):
    return get_sectors(province, district)

def get_cells_from_sector(province, district, sector):
    return get_cells(province, district, sector)

def get_villages_from_cell(province, district, sector, cell):
    return get_villages(province, district, sector, cell)

def get_all_children(province=None, district=None, sector=None, cell=None):
    data = get_location_data()
    if province:
        if district:
            if sector:
                if cell:
                    return get_villages(province, district, sector, cell)
                else:
                    return get_cells(province, district, sector)
            else:
                return get_sectors(province, district)
        else:
            return get_districts(province)
    else:
        return get_provinces()