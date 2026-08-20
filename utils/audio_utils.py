import ffmpeg
import os


def extract_audio(video_path):
    # If the uploaded file is already an audio file,
    # no audio extraction is required.
    if video_path.lower().endswith((".wav", ".mp3", ".m4a", ".flac", ".aac", ".ogg")):
        return video_path

    # For video files, extract the audio as WAV.
    audio_path = os.path.splitext(video_path)[0] + ".wav"

    (
        ffmpeg
        .input(video_path)
        .output(audio_path, ac=1, ar=16000)
        .run(overwrite_output=True)
    )

    return audio_path
