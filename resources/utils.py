import os
import logging
import time
import yaml
from functools import wraps

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


if __name__ == "__main__":
    read_yaml_conf(yaml_path=r"C:\Users\erick\OneDrive\Escritorio\Content_creator\content_creator\conf.yaml")
