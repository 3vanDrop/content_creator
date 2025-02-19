import logging
import time
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
