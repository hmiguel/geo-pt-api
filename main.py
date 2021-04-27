from fastapi import FastAPI, HTTPException
import geopt

app = FastAPI()

geo = geopt.GeoPT("Cont_AAD_CAOP2020.shp")

@app.get("/")
def get_location_info(lat: long, lon: long):
    location = geo.get_location(lat, lon)
    return location if location else HTTPException(status_code=404, detail="Location not found: Coordinates out of range!")
