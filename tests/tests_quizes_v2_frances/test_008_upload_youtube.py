from tests.base_test import BaseTest
from resources.upload_youtube import upload_videos_from_folder

import datetime
import random

class TestUploadYouTube(BaseTest):
    TAGS = [
        "TestDeFrancés", "NivelDeFrancés", "AprendeFrancés", "FrancésParaTodos",
        "PruebaTuFrancés", "ExamenDeFrancés", "TestDeFrançais", "DesafíoDeFrancés",
        "MejoraTuFrancés", "FrancésFácil", "GramáticaFrancés", "VocabularioFrancés",
        "ComprensiónOralFrancés", "LecturaFrancés", "ExpresiónOralFrancés", "ExpresiónEscritaFrancés",
        "EjerciciosDeFrancés", "AprenderFrancésJugando", "QuizDeFrancés",
        "TestDeVocabularioFrancés", "ComprensiónLectoraFrancés", "FrancésBásico", "FrancésIntermedio",
        "FrancésAvanzado", "CertificaciónFrancés", "PreparaciónDELF", "PreparaciónDALF",
        "TCF", "PruebaDeIdiomas", "ExamenDeIdiomas", "FluidezEnFrancés",
        "TrucosParaAprenderFrancés", "ConsejosDeFrancés", "TestDeComprensiónOral",
        "TestDeLectura", "TestDeExpresiónEscrita", "TestDeExpresiónOral", "Idiomas",
        "EducaciónEnFrancés", "AprendizajeDeIdiomas", "HabilidadesLingüísticas",
        "ExpresionesEnFrancés", "VerbosEnFrancés", "PronunciaciónEnFrancés",
        "ComprensiónAuditivaFrancés", "EjerciciosInteractivos", "DesafíoLingüístico",
        "FrancésParaViajar", "FrancésParaNegocios", "FrancésAcadémico"
    ]
    descripciones = [
        "¿Qué nivel de francés tienes? ¡Descúbrelo ahora!", 
        "Pon a prueba tu francés con este test rápido", 
        "¿Te atreves a este desafío de francés?", 
        "¡Solo el 10% obtiene el nivel más alto! ¿Podrás tú?", 
        "Averigua tu nivel de francés en solo 2 minutos", 
        "¿Eres un experto en francés? ¡Compruébalo!", 
        "Un reto de francés que no querrás perderte", 
        "¿Listo para demostrar tu dominio del francés?", 
        "Demuestra qué tan bien hablas francés", 
        "¡Atrévete y sorpréndete con tu nivel!", 
        "¿Puedes responder correctamente en francés? ¡Inténtalo!", 
        "Un test que pondrá a prueba tu gramática y vocabulario en francés", 
        "¿Crees que dominas el francés? ¡Compruébalo!", 
        "¡Solo para los que realmente saben francés!", 
        "¿Podrás alcanzar el nivel más alto? ¡Descúbrelo!", 
        "Un test de francés que no te puedes perder", 
        "¿Eres parte del 5% que obtiene nivel avanzado?", 
        "¡Demuestra tu talento en francés en solo 3 minutos!", 
        "¿Listo para un desafío sorprendente en francés?", 
        "¡Atrévete a descubrir qué nivel de francés tienes!"
    ]
    random_tags = random.sample(TAGS, 10)
    descripcion = random.choice(descripciones)

    def test_upload_video(self):
        video_path = "/Users/karinalizarraga/Desktop/Workspace/Quizes_v2_Frances/final_videos"

        # mexico time is -3. So if 7:00am is given, it will do 4:00am
        # datetime.datetime(2025, 3, 3, 15, 26, 40)
        # datetime.datetime.now()
        # datetime.timedelta(hours=1)
        fecha_de_inicio = datetime.datetime.now()
        tiempo_entre_videos = 4  # horas

        upload_videos_from_folder(video_path,
                                  tags=[self.random_tags],
                                  description=(f"{self.descripcion}"
                                               " - #"+" #".join(self.random_tags)),
                                  custom_title="#DesafíoDeFrances - #Test #AprendeJugando",
                                  schedule_time=fecha_de_inicio,
                                  schedule_every_several_hours=tiempo_entre_videos)
