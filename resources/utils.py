import zipfile
import os
import logging
import time
import yaml
import csv
import shutil
from functools import wraps
from pathlib import Path

# Configura el logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Inicia el temporizador
        start_time = time.time()
        
        # Ejecuta la función
        result = func(*args, **kwargs)
        
        # Calcula el tiempo transcurrido
        elapsed_time = time.time() - start_time
        
        # Convierte el tiempo a minutos y segundos
        minutes, seconds = divmod(int(elapsed_time), 60)
        
        # Imprime el tiempo usando logger.info
        logger.info(f"{func.__name__} Finished in {minutes:02}:{seconds:02}")
        
        return result
    return wrapper


def read_yaml_conf(yaml_path=os.path.join(os.getcwd(), "conf.yaml")):
    """Carga la configuración desde el archivo conf.yaml."""
    with open(yaml_path, "r") as f:
        try:
            config = yaml.safe_load(f)
            if not config:
                logger.warning("⚠️ El archivo de configuración está vacío. Usando valores por defecto.")
                return {}

            # Convertir la lista de configuraciones en un diccionario
            config_dict = {}
            for item in config:
                if isinstance(item, dict):
                    config_dict.update(item)
            return config_dict

        except yaml.YAMLError as e:
            logger.error(f"❌ Error al leer el archivo de configuración: {e}")
            return {}


def read_csv(input_filepath, skip_headers=True):
    """
    Lee un archivo CSV separado por '|' y devuelve una lista de listas,
    donde cada lista interna representa una fila del archivo.

    :param input_filepath: Ruta del archivo CSV a leer.
    :param skip_headers: Si es True, omite la primera fila (encabezados). Si es False, la incluye.
    :return: Lista de listas con los elementos de cada fila.
    """
    data = []
    
    with open(input_filepath, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='	')
        
        # Si skip_headers es True, saltamos la primera fila
        if skip_headers:
            next(reader)  # Salta la primera fila (encabezados)
        
        # Agregamos cada fila como una lista a la lista principal
        for row in reader:
            data.append(row)
    
    return data


@time_it
def unzip_file(zip_filepath, destination_folder):
    """
    Descomprime un archivo ZIP en la carpeta de destino especificada.

    Parámetros:
    zip_filepath (str): Ruta del archivo ZIP que se desea descomprimir.
    destination_folder (str): Ruta de la carpeta donde se extraerán los archivos.

    Retorna:
    None
    """
    # Verifica si el archivo ZIP existe
    if not os.path.exists(zip_filepath):
        logger.info(f"El archivo {zip_filepath} no existe.")
        return

    # Verifica si la carpeta de destino existe, si no, la crea
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Abre el archivo ZIP
    with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
        # Extrae todos los archivos en la carpeta de destino
        zip_ref.extractall(destination_folder)
        logger.info(f"Archivos extraídos en {destination_folder}")


@time_it
def bulk_move_files(source_folder=".", file_extension="*.mp4", destination_folder="carpeta_destino"):
    """
    Busca recursivamente archivos con una extensión específica en una carpeta de origen
    y los mueve a una carpeta de destino.

    Parámetros:
    source_folder (str): Carpeta de origen donde se buscarán los archivos (por defecto ".").
    file_extension (str): Extensión de los archivos a buscar (por defecto "*.mp4").
    destination_folder (str): Carpeta de destino donde se moverán los archivos (por defecto "carpeta_destino").

    Retorna:
    None
    """
    # Crear la carpeta de destino si no existe
    Path(destination_folder).mkdir(parents=True, exist_ok=True)

    # Buscar archivos recursivamente en la carpeta de origen
    for file_path in Path(source_folder).rglob(file_extension):
        # Obtener el nombre del archivo
        file_name = file_path.name

        # Crear la ruta de destino
        destination_path = Path(destination_folder) / file_name

        # Mover el archivo
        shutil.move(str(file_path), str(destination_path))
        print(f"Movido: {file_path} -> {destination_path}")


if __name__ == "__main__":
    read_yaml_conf(yaml_path=r"C:\Users\erick\OneDrive\Escritorio\Content_creator\content_creator\conf.yaml")
