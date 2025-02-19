import edge_tts
import asyncio
import os

async def generar_audio(texto, voz="es-MX-DaliaNeural", output_file="voz_generada.mp3"):
    """Genera un archivo MP3 con el texto en voz sintética y devuelve su ruta absoluta."""
    # Crear el comunicador de edge-tts
    communicate = edge_tts.Communicate(texto, voice=voz)
    
    # Guardar el archivo de audio
    await communicate.save(output_file)
    
    # Obtener la ruta absoluta
    path_absoluto = os.path.abspath(output_file)
    
    return path_absoluto

# Llamar la función de forma síncrona
def generar_voz(texto, voz="es-MX-JorgeNeural", output_file="voz_generada.mp3"):
    return asyncio.run(generar_audio(texto, voz))

if __name__ == "__main__":
    # Ejemplo de uso
    ruta_audio = generar_voz("Hola, este es un ejemplo de voz generada con edge-tts.")
    print(f"Archivo guardado en: {ruta_audio}")
