import os
import sys
import subprocess

def install_dependencies():
    print("Installing dependencies (yt-dlp, youtube-transcript-api)...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", "--break-system-packages", "--upgrade", "yt-dlp[default]", "youtube-transcript-api"])

def download_mp3_and_transcript(video_url):
    install_dependencies()
    
    from youtube_transcript_api import YouTubeTranscriptApi
    import yt_dlp

    # Extract Video ID for the transcript
    video_id = None
    if "v=" in video_url:
        video_id = video_url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in video_url:
        video_id = video_url.split("youtu.be/")[1].split("?")[0]
        
    if not video_id:
        print("Error: Could not extract video ID from URL.")
        return

    print(f"Video ID: {video_id}")
    
    # 1. Download Transcript
    print("Fetching transcript...")
    try:
        api = YouTubeTranscriptApi()
        transcript_data = api.fetch(video_id)
        transcript_path = f"{video_id}_transcript.txt"
        with open(transcript_path, "w", encoding="utf-8") as f:
            for entry in transcript_data:
                f.write(f"[{entry.start:.2f}] {entry.text}\n")
        print(f"Transcript saved to: {transcript_path}")
    except Exception as e:
        print(f"Could not retrieve transcript: {e}")

    # 2. Download MP3
    print("Downloading audio as MP3...")
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{video_id}.%(ext)s',
        'js_runtime': 'node',
        'extractor_args': {
            'youtube': {
                'player_client': ['web'],
            }
        },
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"Audio downloaded and converted to {video_id}.mp3 successfully.")
    except Exception as e:
        print(f"Error downloading audio: {e}")
        print("Note: If FFmpeg is missing, MP3 conversion might fail, but the audio file will still be downloaded.")

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=7sdocMe5DV4"
    download_mp3_and_transcript(url)
