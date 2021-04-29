# geo-pt-api
 
Python version of [geo-pt-api](https://github.com/jfoclpf/geo-pt-api)!

Detect official divisional administrative regions of Portugal ("Carta Administrativa Oficial de Portugal - CAOP 2020", from [here](http://mapas.dgterritorio.pt/ATOM-download/CAOP-Cont/Cont_AAD_CAOP2020.zip)), providing GPS coordinates as input. You can use the public API [here](https://geo-pt-api.ew.r.appspot.com/docs).

It creates a HTTP server, whose GET request `/?lat=40.153687&lon=-8.514602` returns a JSON

```json
{
  "freguesia": "Anobra",
  "concelho": "Condeixa-A-Nova",
  "distrito":"Coimbra"
}
```

## How to install the API on your machine

(optional) $ python -m venv env && source env/bin/activate

1. $ pip install -r requirements.txt
2. $ uvicorn main:app --port :port:
