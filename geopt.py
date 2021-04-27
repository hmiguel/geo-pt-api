from shapely.geometry import shape, Point
import pyproj
import fiona

class GeoPT(object):
        def __init__(self, shapefile):
                self.data = fiona.open(shapefile)
                self.transformer = pyproj.Transformer.from_crs("epsg:4326", self.data.crs.get('init', ''))

        def __transform(self, lat, lon):
                return self.transformer.transform(lat, lon)

        def get_location(self, lat, lon):
                x, y = self.__transform(lat, lon)
                point = Point(x,y)
                for feature in self.data:
                        if shape(feature['geometry']).contains(point):
                                properties = feature.get('properties')
                                return {"freguesia" : properties.get('Freguesia',None), "concelho" : properties.get('Concelho',None), "distrito" : properties.get('Distrito', None) }
                return None

if __name__ == "__main__":
        geo = GeoPT("Cont_AAD_CAOP2020.shp")
        print(geo.get_location(40.153687,-8.514602))
