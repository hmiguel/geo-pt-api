#import geopandas as gpd
from shapely.geometry import shape, Point
import pyproj
import fiona

class GeoPT(object):
        def __init__(self, shapefile):
                self.data = fiona.open(shapefile)
                self.transformer = pyproj.Transformer.from_crs("epsg:4326", self.data.crs.get('init', '').to_string())

        def __transform(self, lat, lon):
                return self.transformer.transform(lat, lon)

        def get_location(self, lat, lon):
                x, y = self.__transform(lat, lon)
                point = Point(x,y)
                #for index, feature in self.data.iterrows():
                #        if shape(feature['geometry']).contains(point):
                #                return {"freguesia" : feature['Freguesia'], "concelho" : feature['Concelho'], "distrito" : feature["Distrito"] }
                return {'x':x, 'y':y}

if __name__ == "__main__":
        geo = GeoPT("Cont_AAD_CAOP2020.shp")
        print(geo.get_location(40.153687,-8.514602))
