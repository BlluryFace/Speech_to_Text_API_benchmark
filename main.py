import sys
import os

from openAI import OpenAITranscriber
from geminiPro import GeminiProTranscriber
from geminiFlash import GeminiFlashTranscriber
from elevenLabs import ElevenLabsTranscriber
from assemblyAI import AssemblyAITranscriber

def run_all_transcribers(audio_path: str):
    print("\n--- Transcribing Audio: {} ---\n".format(audio_path))

    transcribers = [
        ("OpenAI GPT-4o", OpenAITranscriber()),
        ("Gemini 2.5 Pro", GeminiProTranscriber()),
        ("Gemini 2.5 Flash", GeminiFlashTranscriber()),
        ("ElevenLabs", ElevenLabsTranscriber()),
        ("AssemblyAI", AssemblyAITranscriber())
    ]

    base_filename = os.path.splitext(os.path.basename(audio_path))[0]

    for name, transcriber in transcribers:
        print(f"{name}:")
        try:
            result = transcriber.transcribe(audio_path)
        except Exception as e:
            result = f"[ERROR] {e}"

        # Save to file
        folder_path = os.path.join("transcriptions", name.replace(" ", "_"))
        os.makedirs(folder_path, exist_ok=True)

        output_path = os.path.join(folder_path, f"{base_filename}_transcription.txt")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(result)

        print(f"Saved transcription to: {output_path}")
        print("-" * 50)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <audio_file_path>")
        sys.exit(1)

    audio_file_path = sys.argv[1]
    run_all_transcribers(audio_file_path)