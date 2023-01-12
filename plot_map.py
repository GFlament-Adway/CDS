from netCDF4 import Dataset as NetCDFFile
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap

# Opening the downloaded file
nc = NetCDFFile('eur11_rca4_CNRM-CERFACS-CNRM-CM5_rcp45_fwi-daily-proj_20060101_20061231_v2.nc')

# Handling the data from this file.
temperature = nc.variables["fwi-daily-proj"][:]
lat = nc.variables["rlat"][:]
lon = nc.variables["rlon"][:]
lons, lats = np.meshgrid(lon, lat)

# Creating the basemap.
plt.figure()
map = Basemap(projection='tmerc', llcrnrlon=-5.5, llcrnrlat=42.5, urcrnrlon=10.5, urcrnrlat=52.5, lon_0=0.36,
              lat_0=44.7, resolution='i')

x, y = map(lons, lats)

# Adding points to the map
poi_lat = [2.2637]
poi_lon = [48.884]
assert len(poi_lon) == len(poi_lat), "Data of your poi has a problem"
poi_x, poi_y = map(poi_lat, poi_lon)
for i in range(len(poi_lat)):
    map.scatter(poi_x, poi_y, marker='o', color='r', zorder=5)

map.drawcoastlines()
map.fillcontinents(color='coral', lake_color='aqua')
# draw parallels and meridians.
map.drawmapboundary(fill_color='aqua')
plt.title("Transverse Mercator Projection")
plt.show()
# temp = map.contourf(x, y, temperature[-1, :, :])

# cb = map.colorbar(temp, "bottom", size="5%", pad="2%")
#plt.title('Fire risk index')
# cb.set_label('Fire risk index')
#plt.show()
