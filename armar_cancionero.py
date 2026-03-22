import json
import os
import re

def es_linea_de_acordes(linea):
    """Detecta si una línea contiene solo acordes de música (A-G, m, 7, etc)"""
    if not linea.strip(): return False
    palabras = linea.split()
    # Patrón para acordes: Notas A-G, sostenidos, bemoles, séptimas, bajos, etc.
    patron = r'^([A-G][#b]?(m|maj|min|dim|aug|sus|add|2|4|5|6|7|9|11|13)*(/?[A-G][#b]?)?)$'
    return all(re.match(patron, p) for p in palabras)

def formatear_acordes_con_corchetes(linea):
    """Transforma 'C    G7' en '[C]    [G7]' manteniendo los espacios exactos."""
    return re.sub(r'(\S+)', r'[\1]', linea)

def actualizar_indice(nueva_cancion, momento):
    """Agrega la canción al index.json global para el menú del celular."""
    indice_path = 'canciones/index.json'
    data = {"categorias": []}
    
    if os.path.exists(indice_path):
        with open(indice_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

    # Buscar si ya existe la categoría (momento de la misa)
    cat = next((c for c in data["categorias"] if c["nombre"] == momento), None)
    if not cat:
        cat = {"nombre": momento, "songs": []}
        data["categorias"].append(cat)

    # Evitar duplicados
    if not any(s["id"] == nueva_cancion["id"] for s in cat["songs"]):
        cat["songs"].append({
            "id": nueva_cancion["id"],
            "titulo": nueva_cancion["titulo"]
        })
        cat["songs"].sort(key=lambda x: x["titulo"])

    with open(indice_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def procesar():
    if not os.path.exists('entrada.txt'):
        print("❌ Error: No se encontró el archivo 'entrada.txt'")
        return

    with open('entrada.txt', 'r', encoding='utf-8') as f:
        # Leemos líneas eliminando saltos de línea pero NO espacios al final
        lineas = [l.rstrip('\n\r') for l in f.readlines()]

    if len(lineas) < 3:
        print("❌ Error: El archivo debe tener Título, Momento y Tono en las primeras 3 líneas.")
        return

    titulo = lineas[0].strip()
    momento = lineas[1].strip()
    tonalidad = lineas[2].strip()
    
    cuerpo_final = []

    # Empezamos desde la línea 3 (donde empieza la música)
    i = 3
    while i < len(lineas):
        l1 = lineas[i]
        
        if es_linea_de_acordes(l1):
            # 1. Convertimos la línea de acordes a formato [C]    [G]
            linea_acordes_pro = formatear_acordes_con_corchetes(l1)
            cuerpo_final.append(linea_acordes_pro)
            
            # 2. Si la línea de abajo es la letra, la agregamos tal cual
            if i + 1 < len(lineas) and not es_linea_de_acordes(lineas[i+1]):
                cuerpo_final.append(lineas[i+1])
                i += 2
            else:
                i += 1
        else:
            # Líneas de texto sueltas o vacías
            cuerpo_final.append(l1)
            i += 1

    # Crear el diccionario de la canción (sin el campo artista)
    cancion = {
        "id": titulo.lower().replace(" ", "-").translate(str.maketrans("áéíóú", "aeiou")),
        "titulo": titulo,
        "momento": momento,
        "tonalidad_original": tonalidad,
        "cuerpo": "\n".join(cuerpo_final)
    }

    # Guardar el JSON individual
    os.makedirs('canciones', exist_ok=True)
    archivo_salida = f"canciones/{cancion['id']}.json"
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        json.dump(cancion, f, indent=2, ensure_ascii=False)

    # Actualizar el índice general
    actualizar_indice(cancion, momento)
    
    print(f"✅ ¡Canción '{titulo}' procesada!")
    print(f"📂 Archivo generado: {archivo_salida}")

if __name__ == "__main__":
    procesar()