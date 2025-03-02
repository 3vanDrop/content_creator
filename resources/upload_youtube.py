import os
import datetime
import shutil
import time
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.http
from pathlib import Path

def upload_to_youtube(
    video_path,
    tags=None,
    description="",
    status="public",
    schedule_time=None,
    custom_title=None
):
    """Sube un video a YouTube con opciones adicionales."""
    try:
        # Autenticación con OAuth 2.0
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            "client_secret_1076071101464-bm19qlcf7nj4o5ieav3jem0rai0bu4f7.apps.googleusercontent.com.json", ["https://www.googleapis.com/auth/youtube.upload"]
        )
        credentials = flow.run_local_server(port=0)
        youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

        # Configuración automática del título y descripción
        video_filename = os.path.basename(video_path).replace("VEED", "").strip()
        title = custom_title if custom_title else os.path.splitext(video_filename)[0]  # Usa el nombre del archivo como título
        tags = tags or []
        description = description or ""

        # Configurar la fecha de publicación programada
        publish_at = None
        if schedule_time:
            publish_at = schedule_time.isoformat("T") + "Z"  # Formato RFC3339
            status = "private"  # YouTube requiere que esté en privado antes de programarlo

        # Enviar el video a YouTube
        request = youtube.videos().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "title": title,
                    "description": description,
                    "tags": tags,
                    "categoryId": "22",  # Categoría "People & Blogs"
                },
                "status": {
                    "privacyStatus": status,
                    "publishAt": publish_at if schedule_time else None,
                },
            },
            media_body=googleapiclient.http.MediaFileUpload(video_path),
        )

        response = request.execute()
        print(f"YouTube: Video subido en https://www.youtube.com/watch?v={response['id']}")
        return True
    except Exception as e:
        print(f"YouTube: Error {e}")
        return False

def upload_videos_from_folder(folder_path, tags=None, description="", status="public", schedule_time=None, custom_title=None,
                              schedule_every_several_hours=None):
    """Itera sobre una carpeta y sube todos los videos .mp4 a YouTube."""
    timestamp = int(time.time())
    old_folder = f"old.{timestamp}"
    os.mkdir(os.path.join(folder_path, old_folder))
    for filename in os.listdir(folder_path):
        schedule_time = schedule_time + datetime.timedelta(hours=schedule_every_several_hours) if schedule_every_several_hours\
        else schedule_time
        if filename.endswith(".mp4"):
            video_path = os.path.join(folder_path, filename)
            print(f"Subiendo: {video_path}")
            assert upload_to_youtube(video_path, tags, description, status, schedule_time,
                                     custom_title=custom_title)

# Ejemplo de uso
# folder_path = "./videos"  # Ruta de la carpeta con videos
# upload_videos_from_folder(folder_path, tags=["educación", "datos curiosos"], description="Videos educativos", schedule_time=datetime.datetime(2025, 3, 1, 12, 0))
