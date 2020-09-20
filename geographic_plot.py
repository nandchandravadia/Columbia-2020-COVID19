import pandas as pd
import matplotlib as plt
import geopandas as gpd
import geoplot as gplt
import geoplot.crs as gcrs


#read in air-traffic CSV data
file = "./data/airport_traffic.csv"
air_traffic = pd.read_csv(file)


gplt.pointplot(air_traffic['center_point_geom'])


