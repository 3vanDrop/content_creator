from tests.base_test import BaseTest
from resources.upload_youtube import upload_videos_from_folder_v2
from . import CONFIG_YAML_KEY

import datetime
import random

class TestUploadYouTube(BaseTest):
    TAGS = [
        "TestDeAlemán", "NivelDeAlemán", "AprendeAlemán", "AlemánParaTodos",
        "PruebaTuAlemán", "ExamenDeAlemán", "GermanTest", "DesafíoDeAlemán",
        "MejoraTuAlemán", "AlemánFácil", "GramáticaAlemán", "VocabularioAlemán",
        "ListeningAlemán", "ReadingAlemán", "SpeakingAlemán", "WritingAlemán",
        "EjerciciosDeAlemán", "AprenderAlemánJugando", "QuizDeAlemán",
        "TestDeVocabulario", "ComprensiónLectora", "AlemánBásico", "AlemánIntermedio",
        "AlemánAvanzado", "CertificaciónAlemán", "PreparaciónGoethe", "PreparaciónTestDaF",
        "AlemánParaViajar", "PruebaDeIdiomas", "ExamenDeIdiomas", "FluidezEnAlemán",
        "TrucosParaAprenderAlemán", "ConsejosDeAlemán", "TestDeListening",
        "TestDeReading", "TestDeWriting", "TestDeSpeaking", "Idiomas",
        "EducaciónEnAlemán", "AprendizajeDeIdiomas", "HabilidadesLingüísticas",
        "ExpresionesEnAlemán", "VerbosEnAlemán", "PronunciaciónEnAlemán",
        "ComprensiónAuditiva", "EjerciciosInteractivos", "DesafíoLingüístico",
        "AlemánParaNegocios", "AlemánAcadémico", "CulturaAlemana"
    ]
    descripciones = [
        "¿Qué nivel de alemán tienes? ¡Descúbrelo ahora!", 
        "Pon a prueba tu alemán con este test rápido",
        "¿Te atreves a este desafío de alemán?", 
        "¡Solo el 10% obtiene el nivel más alto! ¿Podrás tú?", 
        "Averigua tu nivel de alemán en solo 2 minutos", 
        "¿Eres un experto en alemán? ¡Compruébalo!", 
        "Un reto de alemán que no querrás perderte", 
        "¿Listo para demostrar tu dominio del alemán?", 
        "Demuestra qué tan bien hablas alemán", 
        "¡Atrévete y sorpréndete con tu nivel!", 
        "¿Puedes responder correctamente en alemán? ¡Inténtalo!", 
        "Un test que pondrá a prueba tu gramática y vocabulario", 
        "¿Crees que dominas el alemán? ¡Compruébalo!", 
        "¡Solo para los que realmente saben alemán!", 
        "¿Podrás alcanzar el nivel más alto? ¡Descúbrelo!", 
        "Un test de alemán que no te puedes perder", 
        "¿Eres parte del 5% que obtiene nivel avanzado?", 
        "¡Demuestra tu talento en alemán en solo 3 minutos!", 
        "¿Listo para un desafío sorprendente en alemán?", 
        "¡Atrévete a descubrir qué nivel de alemán tienes!"
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
        tiempo_entre_videos = 6  # horas

        upload_videos_from_folder_v2(video_path,
                                     tags=TestUploadYouTube.random_tags,
                                     description=TestUploadYouTube.descripcion,
                                     custom_title="#DesafíoDeAlemán - #Test #AprendeJugando",
                                     schedule_time=fecha_de_inicio,
                                     schedule_every_several_hours=tiempo_entre_videos)
