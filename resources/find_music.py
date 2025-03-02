import requests
import os
import time
from bs4 import BeautifulSoup

def descargar_clip_musica(url, nombre_archivo):
    """Descarga un clip de música desde una URL y lo guarda en un archivo."""
    try:
        respuesta = requests.get(url, stream=True)
        respuesta.raise_for_status()

        with open(nombre_archivo, 'wb') as archivo:
            for chunk in respuesta.iter_content(chunk_size=8192):
                archivo.write(chunk)

        print(f"Clip de música descargado y guardado como '{nombre_archivo}'")
        return nombre_archivo  # Devuelve el path del archivo descargado
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar el clip de música: {e}")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None

def search_open_source_music(query, time_limit):
    """Busca clips de música de código abierto y los descarga dentro de un límite de tiempo."""
    paths_descargados = []
    tiempo_inicio = time.time()

    # Aquí iría la lógica para buscar URLs de clips de música de código abierto
    # Puedes usar APIs de plataformas de música o realizar web scraping
    # Este es solo un ejemplo de URLs de prueba:
    urls_musica = [
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
    ]

    for url in urls_musica:
        tiempo_actual = time.time()
        tiempo_transcurrido = tiempo_actual - tiempo_inicio

        if tiempo_transcurrido >= time_limit:
            print("Se ha alcanzado el límite de tiempo. No se descargarán más clips.")
            break

        nombre_archivo = f"clip_{len(paths_descargados) + 1}.mp3"
        path_descargado = descargar_clip_musica(url, nombre_archivo)

        if path_descargado:
            paths_descargados.append(path_descargado)

    return paths_descargados

if __name__ == "__main__":
    query = "música relajante"  # Reemplaza con tu búsqueda
    time_limit = 10  # Límite de tiempo en segundos

    paths = search_open_source_music(query, time_limit)

    if paths:
        print("Clips de música descargados:")
        for path in paths:
            print(path)