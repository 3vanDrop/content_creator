from resources.generar_voz import generar_voz
import pathlib
import os

def test_audio_gtts():
    audio_path = generar_voz("Hola este es un test case para generar audio.",
                             output_file="test_audio.mp3")
    
    assert pathlib.Path(audio_path).exists(), f"Existe {audio_path}"
    os.remove(audio_path)

def test_audio_gtts_2():
    audio_path = generar_voz("Hola este es un segundo test case para generar audio.",
                             output_file="test_audio2.mp3")
    
    assert pathlib.Path(audio_path).exists(), f"Existe {audio_path}"
    os.remove(audio_path)