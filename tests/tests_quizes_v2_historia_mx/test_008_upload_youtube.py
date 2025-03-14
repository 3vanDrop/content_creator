from tests.base_test import BaseTest
from resources.upload_youtube import upload_videos_from_folder_v2
from . import CONFIG_YAML_KEY

import datetime
import random

class TestUploadYouTube(BaseTest):
    TAGS = [
        "TestDeHistoria", "TriviaHistoriaMexico", "AprendeHistoria", "HistoriaDeMéxico",
        "PruebaTuHistoria", "ExamenDeHistoria", "HistoryQuiz", "DesafíoHistórico",
        "MejoraTuHistoria", "HistoriaFácil", "CulturaMexicana", "IndependenciaDeMéxico",
        "RevoluciónMexicana", "PersonajesHistóricos", "ArqueologíaMexicana", "MéxicoPrehispánico",
        "EjerciciosDeHistoria", "AprenderHistoriaJugando", "QuizDeHistoria",
        "TestDeCulturaMexicana", "ComprensiónHistórica", "HistoriaBásica", "HistoriaIntermedia",
        "HistoriaAvanzada", "CuriosidadesHistóricas", "PreparaciónHistórica",
        "TriviaDeMéxico", "PruebaDeConocimientos", "ExamenDeCulturaMexicana",
        "FluidezEnHistoria", "TrucosParaAprenderHistoria", "ConsejosDeHistoria",
        "TestDeIndependencia", "TestDeRevolución", "TestDePersonajes", "TestDeCulturaGeneral",
        "EducaciónHistórica", "AprendizajeDeHistoria", "HabilidadesHistóricas",
        "ExpresionesHistóricas", "DatosCuriosos", "CronologíaHistórica",
        "ComprensiónHistórica", "EjerciciosInteractivos", "DesafíoHistórico",
        "HistoriaParaEstudiantes", "HistoriaParaTodos", "HistoriaAcadémica"
    ]
    descripciones = [
        "¿Qué tanto sabes de la historia de México? ¡Descúbrelo ahora!", 
        "Pon a prueba tus conocimientos históricos con este test rápido",
        "¿Te atreves a este desafío de historia de México?", 
        "¡Solo el 10% de los Mexicanos conoce todos los datos históricos! ¿Podrás tú?", 
        "Averigua tu nivel de historia en solo 2 minutos", 
        "¿Eres un experto en historia de México? ¡Compruébalo!", 
        "Un reto de historia que no querrás perderte", 
        "¿Listo para demostrar tu dominio de la historia mexicana?", 
        "Demuestra qué tan bien conoces la historia de México", 
        "¡Atrévete y sorpréndete con tu nivel de historia!", 
        "¿Puedes responder correctamente sobre la Independencia de México? ¡Inténtalo!", 
        "Un test que pondrá a prueba tu conocimiento de la Revolución Mexicana", 
        "¿Crees que dominas la historia de México? ¡Compruébalo!", 
        "¡Solo para los que realmente saben de historia mexicana!", 
        "¿Podrás alcanzar el nivel más alto? ¡Descúbrelo!", 
        "Un test de historia de México que no te puedes perder", 
        "¿Eres parte del 5% que conoce todos los personajes históricos?", 
        "¡Demuestra tu talento en historia en solo 2 minutos!", 
        "¿Listo para un desafío sorprendente sobre la historia de México?", 
        "¡Atrévete a descubrir qué tanto sabes de la historia de México!"
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
        tiempo_entre_videos = 12  # horas

        upload_videos_from_folder_v2(video_path,
                                     tags=TestUploadYouTube.random_tags,
                                     description=TestUploadYouTube.descripcion,
                                     custom_title="#TriviaHistoria #Mexico - #Test #AprendeJugando",
                                     schedule_time=fecha_de_inicio,
                                     schedule_every_several_hours=tiempo_entre_videos)
