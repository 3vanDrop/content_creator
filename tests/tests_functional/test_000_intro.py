from resources.generar_voz import generar_voz as edgetts_generar_voz
from tests.base_test import BaseTest

from pydub import AudioSegment

class TestNombresIntro(BaseTest):
    intros = [
        "¿Buscas el nombre perfecto para tu bebé? ¡Estos tienen un significado poderoso!",
        "Si quieres que tu bebé tenga un nombre único, ¡mira estos!",
        "Los nombres más bellos con un significado especial… ¿Cuál te gusta más?",
        "Nombres con historia y personalidad… ¿Cuál elegirías para tu bebé?",
        "Este nombre es tendencia en 2025 y su significado te sorprenderá…",
        "¡No elijas un nombre para tu bebé sin ver esto! Estos tienen un significado increíble…",
        "¿Sabías que algunos nombres pueden traer buena suerte? Aquí te dejo los mejores…",
        "Estos nombres no solo son hermosos, ¡también tienen significados sorprendentes!",
        "Si buscas un nombre con personalidad y significado, ¡estos te van a encantar!",
        "¿Quieres un nombre único y especial? Estos son los favoritos del 2025…",
        "¿Quieres que el nombre de tu bebé tenga un significado poderoso? Aquí tienes los mejores…" 
    ]
    def test_intro(self):
        for i, intro in enumerate(self.intros):
            EXPECTED_DURATION = 5000
            audio_path1 = edgetts_generar_voz(intro,
                                              output_file=f"intro{i}.mp3",
                                              expected_duration_ms=EXPECTED_DURATION)

            audio_duration = len(AudioSegment.from_file(audio_path1))
            assert self.file_exists(audio_path1), f"Existe {audio_path1}"
            assert abs(audio_duration - EXPECTED_DURATION) < 200,\
            f"Expecting audio lenght to differ within +/-200. audio_duration={audio_duration}, "\
            f"EXPECTED_DURATION={EXPECTED_DURATION}"

