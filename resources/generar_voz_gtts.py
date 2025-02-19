from gtts import gTTS
import os

def generar_voz(texto_a_leer, idioma, output_path):
    # Crear el objeto gTTS
    tts = gTTS(text=texto_a_leer, lang=idioma)
    
    # Guardar el archivo MP3 en la ruta especificada
    tts.save(output_path)
    
    # Obtener la ruta absoluta del archivo generado
    ruta_absoluta = os.path.abspath(output_path)
    
    return ruta_absoluta

if __name__ == "__main__":
    generar_voz("Hola, este es un ejemplo de TTS con gTTS.",
                "es",
                "audio_gtts.mp3")
