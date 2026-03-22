from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import requests
import re
import json
from typing import Optional
from pathlib import Path

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

NOTAS = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
MAPEO = {'Db':'C#', 'Eb':'D#', 'Gb':'F#', 'Ab':'G#', 'Bb':'A#', 'Fb':'E', 'Cb':'B'}

def trasponer_acorde(acorde, semitonos):
    if not acorde: return ""
    reg = r'^([A-G][#b]?)(.*)'
    match = re.match(reg, acorde)
    if not match: return acorde
    raiz, sufijo = match.groups()
    raiz = MAPEO.get(raiz, raiz)
    if raiz not in NOTAS: return acorde
    nueva_raiz = NOTAS[(NOTAS.index(raiz) + semitonos) % 12]
    return nueva_raiz + sufijo

def calcular_distancia(orig, dest):
    def limpiar(n):
        # Quitar sufijos (m, 7, maj, etc)
        n = n.replace('m','').replace('7','').replace('maj','')
        # Las notas pueden ser: C, C#, Db, etc.
        # Si está en MAPEO (bemol), convertir a sostenido
        if n in MAPEO:
            return MAPEO[n]
        # Si es sostenido o nota natural, devolver tal cual
        if n in NOTAS:
            return n
        # Si tiene dos caracteres y el segundo es # o b
        if len(n) > 1 and n[1] in ['#','b']:
            nota_base = n[:2]
            if nota_base in MAPEO:
                return MAPEO[nota_base]
            if nota_base in NOTAS:
                return nota_base
        # Por defecto, primer carácter (nota natural)
        return n[:1]
    
    o, d = limpiar(orig), limpiar(dest)
    if o in NOTAS and d in NOTAS:
        return (NOTAS.index(d) - NOTAS.index(o)) % 12
    return 0

# URL de tu servidor local de archivos (Opción 2)
URL_BASE = "http://127.0.0.1:8080/" 

current_dir = Path(__file__).parent

@app.get("/cancion/{id}")
async def get_cancion(id: str, tono_elegido: Optional[str] = None):
    archivo = current_dir / "canciones" / f"{id}.json"
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=404)
    
    if tono_elegido:
        dist = calcular_distancia(data["tonalidad_original"], tono_elegido)
        # Transponer solo lo que está entre brackets
        data["cuerpo"] = re.sub(r'\[(.*?)\]', 
                               lambda m: f"[{trasponer_acorde(m.group(1), dist)}]", 
                               data["cuerpo"])
        data["tonalidad_actual"] = tono_elegido
    else:
        data["tonalidad_actual"] = data["tonalidad_original"]
    return data

# Servir archivos estáticos (HTML, JSON, etc)
app.mount("/", StaticFiles(directory=str(current_dir), html=True), name="static")