import sys
import os

from transcriptionAPI.openAI import OpenAITranscriber
from transcriptionAPI.geminiPro import GeminiProTranscriber
from transcriptionAPI.geminiFlash import GeminiFlashTranscriber
from transcriptionAPI.elevenLabs import ElevenLabsTranscriber
from transcriptionAPI.assemblyAI import AssemblyAITranscriber

def run(folder_path: str = "./recordings"):
    print("\n--- Transcribing All Audio Files in: {} ---\n".format(folder_path))

    transcribers = [
        ("openAI", OpenAITranscriber()),
        ("geminiPro", GeminiProTranscriber()),
        ("geminiFlash", GeminiFlashTranscriber()),
        ("elevenLabs", ElevenLabsTranscriber()),
        ("assemblyAI", AssemblyAITranscriber())
    ]

    for audio_file in os.listdir(folder_path):
        audio_path = os.path.join(folder_path, audio_file)

        if not os.path.isfile(audio_path):
            continue  # Skip subdirectories or non-files

        base_filename = os.path.splitext(os.path.basename(audio_path))[0]
        print(f"\n=== Processing: {audio_file} ===\n")

        for name, transcriber in transcribers:
            print(f"{name}:")

            try:
                result = transcriber.transcribe(audio_path)
            except Exception as e:
                result = f"[ERROR] {e}"

            # Save to corresponding folder
            transcription_folder = os.path.join("transcriptions", name.replace(" ", "_"))
            os.makedirs(transcription_folder, exist_ok=True)

            output_path = os.path.join(transcription_folder, f"{base_filename}_transcription.txt")
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(result)

            print(f"✅ Saved to: {output_path}")
            print("-" * 50)

if __name__ == "__main__":
    run()