from tests.base_test import BaseTest
from resources.upload_youtube import upload_videos_from_folder_v3
from . import CONFIG_YAML_KEY

import datetime
import random

class TestUploadYouTube(BaseTest):
    TAGS = [
        "TriviaDeTV", "SeriesDeLos90", "AprendeTV", "TVParaTodos",
        "PruebaTuTV", "ExamenDeTV", "TVQuiz", "DesafíoDeTV",
        "MejoraTuCulturaTV", "TVFácil", "SeriesClásicas", "TVShows",
        "NostalgiaDeLos90", "CulturaPop", "ActoresYActrices", "PersonajesInolvidables",
        "EjerciciosDeTV", "AprenderTVJugando", "QuizDeTV",
        "TestDeSeries", "ComprensiónTV", "TVBásico", "TVIntermedio",
        "TVAvanzado", "CuriosidadesDeTV", "PreparaciónTV",
        "TriviaDeSeries", "PruebaDeConocimientos", "ExamenDeCulturaTV",
        "FluidezEnTV", "TrucosParaAprenderTV", "ConsejosDeTV",
        "TestDePersonajes", "TestDeActores", "TestDeEpisodios", "TestDeCulturaGeneral",
        "EducaciónTV", "AprendizajeDeTV", "HabilidadesTV",
        "ExpresionesDeTV", "DatosCuriosos", "CronologíaDeTV",
        "ComprensiónTV", "EjerciciosInteractivos", "DesafíoTV",
        "TVParaEstudiantes", "TVParaTodos", "CulturaTV"
    ]
    descripciones = [
        "¿Qué tanto sabes de los TV Shows de los 90s? ¡Descúbrelo ahora!", 
        "Pon a prueba tus conocimientos de series clásicas con este test rápido",
        "¿Te atreves a este desafío de TV Shows de los 90s?", 
        "¡Solo el 10% de los fans conoce todos los datos! ¿Podrás tú?", 
        "Averigua tu nivel de cultura TV en solo 2 minutos", 
        "¿Eres un experto en series de los 90s? ¡Compruébalo!", 
        "Un reto de TV que no querrás perderte", 
        "¿Listo para demostrar tu dominio de las series clásicas?", 
        "Demuestra qué tan bien conoces los TV Shows de los 90s", 
        "¡Atrévete y sorpréndete con tu nivel de cultura TV!", 
        "¿Puedes responder correctamente sobre tus series favoritas? ¡Inténtalo!", 
        "Un test que pondrá a prueba tu conocimiento de personajes y episodios", 
        "¿Crees que dominas las series de los 90s? ¡Compruébalo!", 
        "¡Solo para los que realmente saben de TV Shows clásicos!", 
        "¿Podrás alcanzar el nivel más alto? ¡Descúbrelo!", 
        "Un test de TV Shows de los 90s que no te puedes perder", 
        "¿Eres parte del 5% que conoce todos los detalles de las series?", 
        "¡Demuestra tu talento de fan en solo 2 minutos!", 
        "¿Listo para un desafío sorprendente sobre los 90s?", 
        "¡Atrévete a descubrir qué tanto sabes de las series de los 90s!"
    ]
    random_tags = lambda: random.sample(TestUploadYouTube.TAGS, 10)
    descripcion = lambda: (f"{random.choice(TestUploadYouTube.descripciones)}"
                                " - #"+" #".join(TestUploadYouTube.random_tags()))

    def test_upload_video(self):
        video_path = self.config[CONFIG_YAML_KEY]["final_videos"]

        # mexico time is -3. So if 7:00am is given, it will do 4:00am
        # datetime.datetime(2025, 3, 3, 15, 26, 40)
        # datetime.datetime.now()
        # datetime.timedelta(hours=1)
        fecha_de_inicio = datetime.datetime(2025, 3, 17, 16)
        tiempo_entre_videos = 24  # horas

        upload_videos_from_folder_v3(video_path,
                                     tags=TestUploadYouTube.random_tags,
                                     description=TestUploadYouTube.descripcion,
                                     custom_title="#Trivia #90sShows - #Quiz #CulturaGeneral",
                                     schedule_time=fecha_de_inicio,
                                     schedule_every_several_hours=tiempo_entre_videos)
