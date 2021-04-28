from fastapi import FastAPI, HTTPException
import geopt, os

abspath = os.path.dirname(os.path.abspath(__file__))

app = FastAPI(title="Geo PT API",
    description="Detect official divisional administrative regions of Portugal",
    version="1.0.0",)

geo = geopt.GeoPT(os.path.join(abspath, "shapes"))

@app.get("/")
def get_location_info(lat: float, lon: float):
    location = geo.get_location(lat, lon)
    return location if location else HTTPException(status_code=404, detail="Location not found: Coordinates out of range!")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)