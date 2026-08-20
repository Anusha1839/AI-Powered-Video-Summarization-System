from utils.audio_utils import extract_audio
from utils.transcriber import transcribe_audio
from utils.cleaner import clean_text
from utils.gemini_utils import generate_structured_summary

import json
import os


def process_video(video_path):

    # Create outputs directory if it does not exist
    os.makedirs("outputs", exist_ok=True)

    # Step 1: Extract Audio
    print("Step 1: Extract Audio")
    audio_path = extract_audio(video_path)

    # Step 2: Generate Transcript
    print("Step 2: Transcribe")
    transcript = transcribe_audio(audio_path)

    with open(
        "outputs/transcript.txt",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(transcript)

    # Step 3: Clean Transcript
    print("Step 3: Clean")
    cleaned_text = clean_text(transcript)

    with open(
        "outputs/cleaned_transcript.txt",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(cleaned_text)

    # Step 4: Generate Structured Summary
    print("Step 4: Summary")
    result = generate_structured_summary(cleaned_text)

    # Validate with Pydantic
    from schemas.summary_schema import SummaryResponse

    validated_result = SummaryResponse(**result)

    with open(
        "outputs/structured_summary.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            validated_result.model_dump(),
            f,
            indent=4
        )

    print("Finished")

    return validated_result.model_dump()
