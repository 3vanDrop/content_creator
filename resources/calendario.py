from ics import Calendar, Event
from datetime import datetime, timedelta

def crear_evento(titulo, descripcion, lugar, inicio, fin):
    """
    Crear un evento con formato icalendar.
    
    :param titulo: Título del evento.
    :param descripcion: Descripción del evento.
    :param lugar: Lugar donde se llevará a cabo el evento.
    :param inicio: Fecha y hora de inicio en formato datetime.
    :param fin: Fecha y hora de fin en formato datetime.
    :return: Evento agregado al calendario.
    """
    evento = Event()
    evento.name = titulo
    evento.begin = inicio
    evento.end = fin
    evento.description = descripcion
    evento.location = lugar
    return evento

def agregar_eventos_a_calendario(titulo="Evento de ejemplo", descripcion="Descripción del evento", 
                                 lugar="Ubicación", inicio=None, fin=None):
    """
    Agregar un evento a un archivo .ics.
    
    :param titulo: Título del evento (default: "Evento de ejemplo").
    :param descripcion: Descripción del evento (default: "Descripción del evento").
    :param lugar: Lugar del evento (default: "Ubicación").
    :param inicio: Fecha y hora de inicio del evento (default: datetime.now()).
    :param fin: Fecha y hora de fin del evento (default: 1 hora después de 'inicio').
    """
    if inicio is None:
        inicio = datetime.now()
    if fin is None:
        fin = inicio + timedelta(hours=1)  # Definir una duración de 1 hora si no se especifica el fin

    # Crear el evento
    evento = crear_evento(titulo, descripcion, lugar, inicio, fin)

    # Verificar si ya existe un archivo .ics
    try:
        with open("mi_calendario.ics", "r") as archivo:
            calendario = Calendar(archivo.read())
    except FileNotFoundError:
        # Si el archivo no existe, se crea uno nuevo
        calendario = Calendar()

    # Agregar el nuevo evento al calendario
    calendario.events.add(evento)

    # Guardar el calendario con el nuevo evento
    with open("mi_calendario.ics", "w") as archivo:
        archivo.writelines(calendario)

    print(f"Evento '{titulo}' agregado correctamente al calendario.")
