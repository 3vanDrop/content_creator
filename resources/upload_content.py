import os
import yaml
import requests
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import googleapiclient.http

# Archivos YAML
INPUT_FILE = "input_videos.yaml"
UPLOADED_FILE = "uploaded_videos.yaml"

# Configuración de APIs
TIKTOK_CLIENT_KEY = "sbawi75cjg1d8p2aap"
TIKTOK_CLIENT_SECRET = "ts6hGpKkWRLFERXvizC9UfepjUksGr8t"
TIKTOK_ACCESS_TOKEN = "TU_ACCESS_TOKEN"
FB_ACCESS_TOKEN = "EAAHfsxS5gUMBOwd0amczByxH8qseFp4ZAGJHUMPc8ZCpZBQTV4VOZBb7BfG5IczFBo71skFg8ZCP5YVhfsZCrMZCtKezVG9ZAOXuxoyOozlpnDmiBBYJ0ja6rZBAByFDebn4V5j2DPqJBZASrbvZBAXXflnqnxQzOE0aVixGFpzVvBA1cDxWt3ha4ijbuie8siNOBQfSJfOtXhnbC5PZB7cQP9LfsDLurU4w2R8ZD"
FB_PAGE_ID = "296936583690967"

def load_videos():
    """Carga la lista de videos desde input_videos.yaml"""
    if not os.path.exists(INPUT_FILE):
        return {"videos": []}
    with open(INPUT_FILE, "r") as f:
        return yaml.safe_load(f) or {"videos": []}

def save_videos(videos):
    """Guarda la lista de videos en input_videos.yaml"""
    with open(INPUT_FILE, "w") as f:
        yaml.dump({"videos": videos}, f, default_flow_style=False)

def save_uploaded(video):
    """Guarda un video en uploaded_videos.yaml"""
    uploaded = load_videos_from_file(UPLOADED_FILE)
    uploaded["videos"].append(video)
    with open(UPLOADED_FILE, "w") as f:
        yaml.dump(uploaded, f, default_flow_style=False)

def load_videos_from_file(filename):
    """Carga videos desde un archivo YAML"""
    if not os.path.exists(filename):
        return {"videos": []}
    with open(filename, "r") as f:
        return yaml.safe_load(f) or {"videos": []}

def upload_to_youtube(video_path, tags: list):
    """Sube un video a YouTube solo con la ruta del archivo."""
    try:
        # Autenticación con OAuth 2.0
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            "client_secret_1076071101464-bm19qlcf7nj4o5ieav3jem0rai0bu4f7.apps.googleusercontent.com.json", ["https://www.googleapis.com/auth/youtube.upload"]
        )
        credentials = flow.run_local_server(port=0)
        youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

        # Configuración automática del título y descripción
        video_filename = os.path.basename(video_path).replace("VEED", "")
        title = os.path.splitext(video_filename)[0]  # Usa el nombre del archivo como título
        description = " #".join([""] + tags)[1:]

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
                "status": {"privacyStatus": "public"},  # Puede ser "private" o "unlisted"
            },
            media_body=googleapiclient.http.MediaFileUpload(video_path),
        )

        response = request.execute()
        print(f"YouTube: Video subido en https://www.youtube.com/watch?v={response['id']}")
        return True
    except Exception as e:
        print(f"YouTube: Error {e}")
        return False

def upload_to_tiktok(video):
    """Sube el video a TikTok"""
    try:
        url = "https://open-api.tiktok.com/share/video/upload/"
        headers = {"Authorization": f"Bearer {TIKTOK_ACCESS_TOKEN}"}
        files = {"video": open(video["file"], "rb")}
        response = requests.post(url, headers=headers, files=files)
        
        if response.status_code == 200:
            print("TikTok: Video subido correctamente")
            return True
        else:
            print(f"TikTok: Error {response.text}")
            return False
    except Exception as e:
        print(f"TikTok: Error {e}")
        return False

def upload_to_facebook(video_path):
    """Sube un video a Facebook solo con la ruta del archivo."""
    try:
        url = f"https://graph-video.facebook.com/{FB_PAGE_ID}/videos"
        files = {"source": open(video_path, "rb")}
        data = {
            "title": "Video Automático",  # Puedes cambiar esto o eliminarlo si no quieres título
            "description": "Subido con la API de Facebook",  # Puedes modificarlo
            "access_token": FB_ACCESS_TOKEN
        }
        
        response = requests.post(url, files=files, data=data)
        
        if response.status_code == 200:
            print("Facebook: Video subido correctamente")
            return True
        else:
            print(f"Facebook: Error {response.text}")
            return False
    except Exception as e:
        print(f"Facebook: Error {e}")
        return False
def main():
    """Carga videos, sube y actualiza los archivos YAML"""
    videos = load_videos()["videos"]
    if not videos:
        print("No hay videos pendientes para subir.")
        return

    updated_videos = []
    for video in videos:
        success = False

        # Intentar subir a cada plataforma
        if upload_to_youtube(video):
            success = True
        if upload_to_tiktok(video):
            success = True
        if upload_to_facebook(video):
            success = True

        # Si el video fue subido con éxito a al menos una plataforma, lo mueve a uploaded_videos.yaml
        if success:
            save_uploaded(video)
        else:
            updated_videos.append(video)  # Mantener en la lista de pendientes si falló

    # Guardar los videos pendientes en input_videos.yaml
    save_videos(updated_videos)

if __name__ == "__main__":
    main()
