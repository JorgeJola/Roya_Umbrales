#Se cargan las librerias necesarias para llevar a cabo la API y las funciones dentro de esta
import pandas as pd
from fastapi import FastAPI, Form, Request
from enum import Enum
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

#DATA GENERAL DE LA API
app = FastAPI()
app.title = "Sistema de alerta de riesgos (Hemileia Vastatrix) por umbrales tomados de literatura. By: Jorge Andrés Jola Hernández"
app.version = "1.0.0"

@app.on_event("startup")
async def startup_event():
    global Cantidad_Nitrogeno
    Cantidad_Nitrogeno=0


@app.get('/Nitrogeno/{cantidad}')
def Nitrogeno(cantidad:float):
    Cantidad_Nitrogeno=cantidad

@app.get('/imprimir/{}')
def imprimir():   
    print(Cantidad_Nitrogeno)

