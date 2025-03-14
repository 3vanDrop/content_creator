from resources.generar_voz import generar_voz as edgetts_generar_voz
from resources.media_join import join_audio
from resources.utils import read_csv
from tests.base_test import BaseTest
import random


class TestTTSAudio(BaseTest):

    inicio_pregunta = ["¿Qué significa ", "¿Como traduces ", "¿Que quiere decir ",
                       "¿Qué es ", "¿Sábes que es "]
    randomly_pick = lambda self: random.choice(TestTTSAudio.inicio_pregunta)

    def test_multiple_quizes(self):
        quizes = read_csv(self.config["Quizes_v2_Frances"]["input_multiple_csv"])
        audio_path = lambda x: self.config["Quizes_v2_Frances"]["audio_to_join"].replace("*", str(x))

        for i, quiz in enumerate(quizes):
            self.logger.info(f"len={len(quiz)}, preguntas={quiz}")
            self.generate_quiz_audio(preguntas=quiz,
                                     output_final_audio=audio_path(i))

    def generate_quiz_audio(self, preguntas: list, output_final_audio: str):
        intro_audio = self.config["Quizes_v2_Frances"]["intro_audio"]
        nivel_facil = self.config["Quizes_v2_Frances"]["facil_audio"]
        end_facil = self.config["Quizes_v2_Frances"]["end_facil_audio"]
        nivel_medio = self.config["Quizes_v2_Frances"]["medio_audio"]
        nivel_dificil = self.config["Quizes_v2_Frances"]["dificil_audio"]
        ultima_pregunta = self.config["Quizes_v2_Frances"]["ultima_audio"]
        end_audio = self.config["Quizes_v2_Frances"]["end_audio"]
        audios_generados = [intro_audio, nivel_facil]

        # Primer pregunta/respuesta
        pregunta_1 = self._generar_pregunta(1, preguntas[0], preguntas[1],
                                            siguiente=True)
        audios_generados.append(pregunta_1)

        # Segunda pregunta/respuesta
        pregunta_2 = self._generar_pregunta(2, preguntas[2], preguntas[3],
                                            siguiente=True)
        audios_generados.append(pregunta_2)

        # Estuvo facil? + Nivel medio
        audios_generados += [end_facil, nivel_medio]

        # Tercera pregunta/respuesta
        pregunta_3 = self._generar_pregunta(3, preguntas[4], preguntas[5],
                                            siguiente=True)
        audios_generados.append(pregunta_3)

        # Cuarta pregunta/respuesta
        pregunta_4 = self._generar_pregunta(4, preguntas[6], preguntas[7],
                                            siguiente=True)
        audios_generados.append(pregunta_4)

        # Nivel dificil
        audios_generados.append(nivel_dificil)

        # Quinta pregunta/respuesta
        pregunta_5 = self._generar_pregunta(5, preguntas[8], preguntas[9],
                                            siguiente=True)
        audios_generados.append(pregunta_5)

        # Sexta pregunta/respuesta
        pregunta_6 = self._generar_pregunta(6, preguntas[10], preguntas[11],
                                            siguiente=True)
        audios_generados.append(pregunta_6)

        # Nivel experto
        audios_generados.append(ultima_pregunta)


        # Experto pregunta/respuesta
        pregunta_7 = self._generar_pregunta(7, preguntas[12], None,
                                            siguiente=False)
        audios_generados.append(pregunta_7)

        # Deja la respuesta en los comentarios
        audios_generados.append(end_audio)

        join_audio(*audios_generados, output_file=output_final_audio)
        self.logger.info(f"=== {output_final_audio} Completado! ===")

    def _generar_pregunta(self, num, pregunta, respuesta, siguiente=False):
        audio_to_join = []
        pregunta = edgetts_generar_voz(self.randomly_pick() + pregunta + "?",
                                        output_file="test_audio1.mp3",
                                        expected_duration_ms=3100)
        if respuesta != None:
            respuesta = edgetts_generar_voz(f"{respuesta}...",
                                            output_file="test_audio2.mp3",
                                            expected_duration_ms=2500)

        tic_tac_audio = self.config["Quizes_v2_Frances"]["tic_tac_audio"]
        success_audio = self.config["Quizes_v2_Frances"]["success_audio"]
        siguiente_audio = self.config["Quizes_v2_Frances"]["siguiente_audio"]
        audio_to_join += [pregunta]
        if respuesta != None:
            audio_to_join += [tic_tac_audio, success_audio, respuesta]

        if siguiente:
            audio_to_join.append(siguiente_audio)

        assert self.file_exists(pregunta), f"No Existe {pregunta}!"

        if respuesta != None:
            assert self.file_exists(respuesta), f"No Existe {respuesta}!"

        pregunta_output = f"pregunta_{num}.mp3"
        join_audio(*audio_to_join, output_file=pregunta_output)

        return pregunta_output

