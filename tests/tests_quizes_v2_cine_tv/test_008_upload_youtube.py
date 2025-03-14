from tests.base_test import BaseTest
from resources.upload_youtube import upload_videos_from_folder_v2
from . import CONFIG_YAML_KEY

import datetime
import random

class TestUploadYouTube(BaseTest):
    TAGS = [
        "TriviaDeCine", "TriviaDeTV", "AprendeCine", "CineParaTodos",
        "PruebaTuCine", "ExamenDeCine", "MovieQuiz", "DesafíoCinematográfico",
        "MejoraTuCulturaCinéfila", "CineFácil", "PelículasClásicas", "SeriesDeTV",
        "Hollywood", "CineInternacional", "ActoresYActrices", "DirectoresFamosos",
        "EjerciciosDeCine", "AprenderCineJugando", "QuizDeCine",
        "TestDePelículas", "ComprensiónCinematográfica", "CineBásico", "CineIntermedio",
        "CineAvanzado", "CuriosidadesDeCine", "PreparaciónCinéfila",
        "TriviaDeSeries", "PruebaDeConocimientos", "ExamenDeCulturaCinematográfica",
        "FluidezEnCine", "TrucosParaAprenderCine", "ConsejosDeCine",
        "TestDeSeries", "TestDeActores", "TestDeDirectores", "TestDeCulturaGeneral",
        "EducaciónCinematográfica", "AprendizajeDeCine", "HabilidadesCinéfilas",
        "ExpresionesDeCine", "DatosCuriosos", "CronologíaDeCine",
        "ComprensiónCinematográfica", "EjerciciosInteractivos", "DesafíoCinéfilo",
        "CineParaEstudiantes", "CineParaTodos", "CulturaCinematográfica"
    ]
    descripciones = [
        "¿Qué tanto sabes de cine y TV? ¡Descúbrelo ahora!", 
        "Pon a prueba tus conocimientos cinematográficos con este test rápido",
        "¿Te atreves a este desafío de cine y TV?", 
        "¡Solo el 10% de los cinéfilos conoce todos los datos! ¿Podrás tú?", 
        "Averigua tu nivel de cultura cinematográfica en solo 2 minutos", 
        "¿Eres un experto en cine y TV? ¡Compruébalo!", 
        "Un reto de cine que no querrás perderte", 
        "¿Listo para demostrar tu dominio del séptimo arte?", 
        "Demuestra qué tan bien conoces las películas y series", 
        "¡Atrévete y sorpréndete con tu nivel de cultura cinéfila!", 
        "¿Puedes responder correctamente sobre películas clásicas? ¡Inténtalo!", 
        "Un test que pondrá a prueba tu conocimiento de series y actores", 
        "¿Crees que dominas el mundo del cine? ¡Compruébalo!", 
        "¡Solo para los que realmente saben de cine y TV!", 
        "¿Podrás alcanzar el nivel más alto? ¡Descúbrelo!", 
        "Un test de cine y TV que no te puedes perder", 
        "¿Eres parte del 5% que conoce todas las películas icónicas?", 
        "¡Demuestra tu talento cinéfilo en solo 2 minutos!", 
        "¿Listo para un desafío sorprendente sobre cine y TV?", 
        "¡Atrévete a descubrir qué tanto sabes de películas y series!"
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
        fecha_de_inicio = datetime.datetime.now()
        tiempo_entre_videos = 8  # horas

        upload_videos_from_folder_v2(video_path,
                                     tags=TestUploadYouTube.random_tags,
                                     description=TestUploadYouTube.descripcion,
                                     custom_title="#Trivia #CineTV - #Quiz #CulturaGeneral",
                                     schedule_time=fecha_de_inicio,
                                     schedule_every_several_hours=tiempo_entre_videos)
