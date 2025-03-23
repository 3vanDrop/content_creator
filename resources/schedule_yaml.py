import yaml
from datetime import datetime, timedelta
import os
from enum import Enum

# Definir un Enum para los bloques
class Bloques(Enum):
    BLOQUE_1 = ("bloque_09", "9:00")  # Nombre y hora del bloque
    BLOQUE_2 = ("bloque_12", "12:00")
    BLOQUE_3 = ("bloque_13", "13:00")
    BLOQUE_4 = ("bloque_14", "14:00")
    BLOQUE_5 = ("bloque_15", "15:00")
    BLOQUE_6 = ("bloque_18", "18:00")

# Obtener la lista de bloques desde el Enum
BLOQUES = [bloque.value for bloque in Bloques]

# Constantes personalizables
FILE_PATH = 'schedule.yaml'  # Ruta del archivo YAML

# Cargar el archivo YAML (o crearlo si no existe)
def load_yaml(file_path):
    if not os.path.exists(file_path):
        # Crear un archivo YAML vacío si no existe
        with open(file_path, 'w') as file:
            yaml.safe_dump({}, file, default_flow_style=False)
        return {}
    with open(file_path, 'r') as file:
        return yaml.safe_load(file) or {}

# Guardar el archivo YAML
def save_yaml(file_path, data):
    with open(file_path, 'w') as file:
        yaml.safe_dump(data, file, default_flow_style=False)

# Buscar el siguiente bloque disponible
def look_up_for_next_available_block():
    data = load_yaml(FILE_PATH)  # Cargar datos desde el archivo YAML
    if not data:  # Si no hay registros en el YAML, devolver el primer bloque de la fecha actual
        current_date = datetime.now()
        date_str = current_date.strftime('%m/%d/%Y')
        block_name, block_time = Bloques.BLOQUE_1.value
        return datetime.strptime(f"{date_str} {block_time}", "%m/%d/%Y %H:%M")

    current_date = datetime.now()
    while True:  # Revisar indefinidamente hasta encontrar un bloque disponible
        date_str = current_date.strftime('%m/%d/%Y')
        if date_str in data:
            for block_name, block_time in BLOQUES:  # Usar la lista de bloques desde el Enum
                if block_name not in data[date_str] or data[date_str][block_name] is None:  # Si el bloque no existe o está vacío
                    # Combinar la fecha actual con la hora del bloque
                    block_datetime = datetime.strptime(f"{date_str} {block_time}", "%m/%d/%Y %H:%M")
                    return block_datetime
        else:
            # Si la fecha no existe, crear la fecha con el primer bloque disponible
            block_name, block_time = Bloques.BLOQUE_1.value
            block_datetime = datetime.strptime(f"{date_str} {block_time}", "%m/%d/%Y %H:%M")
            return block_datetime
        current_date += timedelta(days=1)  # Pasar al siguiente día

# Programar en el siguiente bloque disponible
def schedule_on_available_block(categoria):
    data = load_yaml(FILE_PATH)  # Cargar datos desde el archivo YAML
    current_date = datetime.now()
    while True:  # Revisar indefinidamente hasta encontrar un bloque disponible
        date_str = current_date.strftime('%m/%d/%Y')
        if date_str not in data:
            # Si la fecha no existe, crear la fecha con el primer bloque
            block_name, block_time = Bloques.BLOQUE_1.value
            data[date_str] = {block_name: categoria}
            save_yaml(FILE_PATH, data)  # Guardar cambios en el archivo YAML
            return datetime.strptime(f"{date_str} {block_time}", "%m/%d/%Y %H:%M")
        else:
            # Si la fecha existe, buscar el siguiente bloque disponible
            for block_name, block_time in BLOQUES:  # Usar la lista de bloques desde el Enum
                if block_name not in data[date_str] or data[date_str][block_name] is None:  # Si el bloque no existe o está vacío
                    data[date_str][block_name] = categoria
                    save_yaml(FILE_PATH, data)  # Guardar cambios en el archivo YAML
                    return datetime.strptime(f"{date_str} {block_time}", "%m/%d/%Y %H:%M")
        current_date += timedelta(days=1)  # Pasar al siguiente día solo si todos los bloques están llenos

# Ejemplo de uso
if __name__ == "__main__":
    # Verificar el próximo bloque disponible antes de programar
    print(f"Próximo bloque disponible: {look_up_for_next_available_block()}")

    # Programar una categoría en el siguiente bloque disponible
    categoria = "CUSTOM_NAME_ID"
    scheduled_block_datetime = schedule_on_available_block(categoria)
    print(f"Programado en: {scheduled_block_datetime}")

    # Verificar el próximo bloque disponible después de programar
    print(f"Próximo bloque disponible: {look_up_for_next_available_block()}")