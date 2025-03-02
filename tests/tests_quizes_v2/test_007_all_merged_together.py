import os
import time
from pathlib import Path
from resources.generar_voz import generar_voz as edgetts_generar_voz
from resources.media_join import join_audio, video_audio_join, video_join
from tests.base_test import BaseTest
from resources.utils import read_csv, unzip_file
from resources.utils import bulk_move_files


class TestTTSAudio(BaseTest):
    TOTAL_FILES_PER_QUIZ = 20
    TOTAL_QUIZES = 10  # Should match the CSV

    def test_000_cleanup_files(self):
        # === PRECONDITION === pages.zip shall exist
        self._precheck()

        pages_vid_folder = str(Path(self.config["Quizes"]["video_quiz_pages_folder"]))
        audio_path = str(Path(self.config["Quizes"]["audio_to_join"]).parent)
        non_audio_videos = str(Path(self.config["Quizes"]["video_to_join"]).parent)
        final_videos = str(Path(self.config["Quizes"]["video_output_join"]).parent)
        self.clean_up_workspace(pages_vid_folder)
        self.clean_up_workspace(audio_path)
        self.clean_up_workspace(non_audio_videos)

        new_folder = os.path.join(final_videos, f"old.{int(time.time())}")
        os.mkdir(new_folder)

        bulk_move_files(source_folder=final_videos,
                        file_extension="*.mp4",
                        destination_folder=new_folder)

    def test_001_generate_all_audio_files(self):
        # === PRECONDITION === pages.zip shall exist
        self._precheck()

        quizes = read_csv(self.config["Quizes"]["input_multiple_csv"])
        audio_path = lambda x: self.config["Quizes"]["audio_to_join"].replace("*", str(x))

        for i, quiz in enumerate(quizes):
            self.logger.info(f"len={len(quiz)}, preguntas={quiz}")
            self.generate_quiz_audio(preguntas=quiz,
                                     output_final_audio=audio_path(i))

    def test_002_join_quiz_video_pages(self):
        # === PRECONDITION === pages.zip shall exist
        self._precheck()

        total_files_per_quiz = self.TOTAL_FILES_PER_QUIZ
        total_quizes = self.TOTAL_QUIZES
        total_pages = total_files_per_quiz * total_quizes

        self._unzip_pages()

        video_counter = 0
        for page in range(1, total_pages+1, total_files_per_quiz):
            self._join_quiz_pages(start_page=page,
                                  files_per_quiz=total_files_per_quiz,
                                  video_quiz_count=video_counter)
            video_counter += 1

    def test_003_join_quiz_video_final(self):
        # === PRECONDITION === pages.zip shall exist
        self._precheck()

        total_quizes = 10
        audio_path = lambda x: self.config["Quizes"]["audio_to_join"].replace("*", str(x))
        video_path = lambda x: self.config["Quizes"]["video_to_join"].replace("*", str(x))
        dst_path = lambda x: self.config["Quizes"]["video_output_join"].replace("*", str(x)).replace("&", "#")

        for i in range(total_quizes): # 0 - 9
            self.logger.info(f"Joining Final Video {i}...")
            video_audio_join(video_path(i), audio_path(i),
                             output_resolution="1080x1920",
                             output_path=dst_path(i))

    def generate_quiz_audio(self, preguntas: list, output_final_audio: str):
        intro_audio = self.config["Quizes"]["intro_audio"]
        nivel_facil = self.config["Quizes"]["facil_audio"]
        end_facil = self.config["Quizes"]["end_facil_audio"]
        nivel_medio = self.config["Quizes"]["medio_audio"]
        nivel_dificil = self.config["Quizes"]["dificil_audio"]
        ultima_pregunta = self.config["Quizes"]["ultima_audio"]
        end_audio = self.config["Quizes"]["end_audio"]
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
        pregunta = edgetts_generar_voz(pregunta,
                                        output_file="test_audio1.mp3",
                                        expected_duration_ms=3100)
        if respuesta != None:
            respuesta = edgetts_generar_voz(f"{respuesta}...",
                                            output_file="test_audio2.mp3",
                                            expected_duration_ms=2500)

        tic_tac_audio = self.config["Quizes"]["tic_tac_audio"]
        success_audio = self.config["Quizes"]["success_audio"]
        siguiente_audio = self.config["Quizes"]["siguiente_audio"]
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
            
    def _join_quiz_pages(self, start_page, files_per_quiz, video_quiz_count):
        self.logger.info(f"Creating Video Quiz #{video_quiz_count}")
        video_path = lambda x: self.config["Quizes"]["video_to_join"].replace("*", str(x))
        pages_path = lambda x: self.config["Quizes"]["video_quiz_pages"].replace("*", str(x))
        list_of_videos = list()
        for i in range(start_page, start_page+files_per_quiz):
            self.logger.info(f"== Video Quiz #{video_quiz_count} - Page {i}")
            list_of_videos.append(pages_path(i))
        
        video_join(*list_of_videos, output_resolution="1080x1920",
                   output_path=video_path(video_quiz_count))
        self.logger.info(f"** Completed Video Quiz #{video_quiz_count} **")

        assert self.file_exists(video_path(video_quiz_count))

    def _unzip_pages(self):
        zip_folder = self.config["Quizes"]["zip_filepath"]
        zip_filename = self.config["Quizes"]["zip_filename"]
        dst_folder = self.config["Quizes"]["video_quiz_pages_folder"]

        unzip_file(os.path.join(zip_folder, zip_filename),
                   destination_folder=dst_folder)

    def _precheck(self):
        zip_folder = self.config["Quizes"]["zip_filepath"]
        zip_filename = self.config["Quizes"]["zip_filename"]
        zip_filepath = os.path.join(zip_folder, zip_filename)

        assert self.file_exists(zip_filepath), f"Expecting {zip_filename} to exist within: {zip_folder}"