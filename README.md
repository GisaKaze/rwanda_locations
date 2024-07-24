# Rwanda Locations

`rwanda_locations` is a Python package designed to provide easy access to Rwandan location metadata. This includes hierarchical data from provinces down to villages, as well as various utility functions to retrieve and manipulate this data.

## Features

- Retrieve provinces
- Retrieve districts within a specific province
- Retrieve sectors within a specific district
- Retrieve cells within a specific sector
- Retrieve villages within a specific cell
- Get all child locations for a given level of hierarchy

## Installation

You can install the package using pip. If you're installing from a local directory, navigate to the directory containing `setup.py` and run:

```bash
pip install .
# As the package is established by PyPI, you can install it using:
pip install rwanda_locations
```

## Usage
Here’s how to use the package in your Python application:

```bash
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
```


## License
This project is licensed under the MIT [License]() - see the LICENSE file for details.

## Contributing
Feel free to open issues and submit pull requests to improve the package. Your contributions are welcome!


## Contact
For any questions or feedback, please contact Fredson Gisa Kaze at [fredson.coder@gmail.com]()

## Acknowledgements
Thank you for using `rwanda_locations`. We hope it helps you efficiently work with Rwandan location data!


## Changelog
1.0
* initial release
* province names and other entities up-to villages(Imidugudu)
* lookup() method
* shapefile URLs for various regions