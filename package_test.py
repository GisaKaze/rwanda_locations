from rwanda_locations.data import (
    get_provinces, get_districts_from_province, get_sectors_from_district,
    get_cells_from_sector, get_villages_from_cell, get_all_children
)

# Get all provinces
provinces = get_provinces()
print("Provinces:", provinces)

# Get districts in a specific province
districts = get_districts_from_province('East')
print("Districts in East Province:", districts)

# Get sectors in a specific district - For example: Nyagatare District
sectors = get_sectors_from_district('East', 'Nyagatare')
print("Sectors in Nyagatare District:", sectors)

# Get cells in a specific sector - For example: Nyagatare Sector
cells = get_cells_from_sector('East', 'Nyagatare', 'Nyagatare')
print("Cells in Nyagatare Sector:", cells)

# Get villages in a specific cell - For example: Barija Cell
villages = get_villages_from_cell('East', 'Nyagatare', 'Nyagatare', 'Barija')
print("Villages in Barija Cell:", villages)

# Get all children based on hierarchy level
children = get_all_children(province='East', district='Nyagatare', sector='Nyagatare')
print("Children in Nyagatare Sector:", children)