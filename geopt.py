from shapely.geometry import shape, Point
import pyproj
import geopandas as gpd
import os

class Region(object):
        def __init__(self, shapefile):
                self.data = gpd.read_file(shapefile)
                self.transformer = pyproj.Transformer.from_crs("epsg:4326", self.data.crs)
                
class GeoPT(object):
        def __init__(self, shapedir):
                self.regions = [Region(x) for x in self.__load_shapedir(shapedir)]

        def __load_shapedir(self, shape_path):
                return [shape_path] if not os.path.isdir(shape_path) else [os.path.join(shape_path, file) for file in os.listdir(shape_path) if file.endswith(".shp")]

        def __transform(self, region, lat, lon):
                return region.transformer.transform(lat, lon)

        def get_location(self, lat, lon):
                for region in self.regions:
                        x, y = self.__transform(region, lat, lon)
                        point = Point(x,y)
                        for index, feature in region.data.iterrows():
                                if shape(feature['geometry']).contains(point):
                                        return {"freguesia" : feature.get('Freguesia',None), "concelho" : feature.get('Concelho',None), "distrito" : feature.get('Distrito', None), "ilha": feature.get('Ilha', None) }                 
                return None

if __name__ == "__main__":
        geo = GeoPT("shapes") 
        print(geo.get_location(40.153687,-8.514602))
        print(geo.get_location(36.987866, -25.095279))
        print(geo.get_location(37.797937, -25.348359))
        print(geo.get_location(38.584861, -28.687783))
        print(geo.get_location(32.765599, -17.053399))
