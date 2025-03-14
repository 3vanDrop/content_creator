from tests.base_test import BaseTest
from resources.upload_youtube import upload_videos_from_folder_v2
from . import CONFIG_YAML_KEY

import datetime
import random

class TestUploadYouTube(BaseTest):
    TAGS = [
        "TestDeGeografía", "TriviaGeográfica", "AprendeGeografía", "GeografíaParaTodos",
        "PruebaTuGeografía", "ExamenDeGeografía", "GeographyQuiz", "DesafíoGeográfico",
        "MejoraTuGeografía", "GeografíaFácil", "CapitalesDelMundo", "BanderasDelMundo",
        "RíosYMontañas", "ContinentesYOcéanos", "CulturaGeográfica", "MapasDelMundo",
        "EjerciciosDeGeografía", "AprenderGeografíaJugando", "QuizDeGeografía",
        "TestDeCapitales", "ComprensiónGeográfica", "GeografíaBásica", "GeografíaIntermedia",
        "GeografíaAvanzada", "CuriosidadesGeográficas", "PreparaciónGeográfica",
        "TriviaDeMapas", "PruebaDeConocimientos", "ExamenDeCulturaGeneral",
        "FluidezEnGeografía", "TrucosParaAprenderGeografía", "ConsejosDeGeografía",
        "TestDeBanderas", "TestDeRíos", "TestDeMontañas", "TestDeCulturaGeneral",
        "EducaciónGeográfica", "AprendizajeDeGeografía", "HabilidadesGeográficas",
        "ExpresionesGeográficas", "DatosCuriosos", "PronunciaciónGeográfica",
        "ComprensiónGeográfica", "EjerciciosInteractivos", "DesafíoGeográfico",
        "GeografíaParaViajar", "GeografíaParaEstudiantes", "GeografíaAcadémica"
    ]
    descripciones = [
        "¿Qué tanto sabes de geografía? ¡Descúbrelo ahora!", 
        "Pon a prueba tus conocimientos geográficos con este test rápido",
        "¿Te atreves a este desafío de geografía?", 
        "¡Solo el 10% conoce todos los datos! ¿Podrás tú?", 
        "Averigua tu nivel de geografía en solo 2 minutos", 
        "¿Eres un experto en geografía? ¡Compruébalo!", 
        "Un reto de geografía que no querrás perderte", 
        "¿Listo para demostrar tu dominio de la geografía mundial?", 
        "Demuestra qué tan bien conoces el mundo", 
        "¡Atrévete y sorpréndete con tu nivel de geografía!", 
        "¿Puedes responder correctamente sobre países y capitales? ¡Inténtalo!", 
        "Un test que pondrá a prueba tu conocimiento de mapas y banderas", 
        "¿Crees que dominas la geografía? ¡Compruébalo!", 
        "¡Solo para los que realmente saben de geografía!", 
        "¿Podrás alcanzar el nivel más alto? ¡Descúbrelo!", 
        "Un test de geografía que no te puedes perder", 
        "¿Eres parte del 5% que conoce todos los ríos y montañas?", 
        "¡Demuestra tu talento en geografía en solo 2 minutos!", 
        "¿Listo para un desafío sorprendente sobre el mundo?", 
        "¡Atrévete a descubrir qué tanto sabes de geografía!"
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
                                     custom_title="#TriviaGeografía - #Test #AprendeJugando",
                                     schedule_time=fecha_de_inicio,
                                     schedule_every_several_hours=tiempo_entre_videos)
