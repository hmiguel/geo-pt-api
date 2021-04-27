import geopandas as gpd
from shapely.geometry import shape, Point
import pyproj

class GeoPT(object):
        def __init__(self, shapefile):
                self.data = gpd.read_file(shapefile)
                self.transformer = pyproj.Transformer.from_crs("epsg:4326", self.data.crs.to_string())

        def transform(self, lat, lon):
                return self.transformer.transform(lat, lon)

        def get_location(self, lat, lon):
                x, y = self.transform(lat, lon)
                point = Point(x,y)
                for index, feature in self.data.iterrows():
                        if shape(feature['geometry']).contains(point):
                                return {"freguesia" : feature['Freguesia'], "concelho" : feature['Concelho'], "distrito" : feature["Distrito"] }
                return None

if __name__ == "__main__":
        geo = GeoPT("Cont_AAD_CAOP2020.shp")
        print(geo.get_location(40.153687,-8.514602))