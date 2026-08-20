from faster_whisper import WhisperModel

def transcribe_audio(audio_path):

    print("Loading model...")

    model = WhisperModel(
        "tiny",
        device="cpu",
        compute_type="int8"
    )

    print("Model loaded...")

    print("Starting transcription...")

    segments, info = model.transcribe(audio_path)

    print("Transcription finished...")

    transcript = ""

    for segment in segments:
        transcript += segment.text + " "

    return transcript
