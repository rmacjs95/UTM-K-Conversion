# -*- encoding: utf-8 -*-
from pyproj import Proj, transform
import sys

# UTM-K
proj_UTMK = Proj(init='epsg:5178')

# WGS84
proj_WGS84 = Proj(init='epsg:4326')

# WGS84 -> UTM-K Sample
x1, y1 = sys.argv[2], sys.argv[1]
x2, y2 = transform(proj_WGS84, proj_UTMK, x1, y1)
print(y2, x2)
