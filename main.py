import sys

from openAI import OpenAITranscriber
from geminiPro import GeminiProTranscriber
from geminiFlash import GeminiFlashTranscriber
from elevenLabs import ElevenLabsTranscriber
from assemblyAI import AssemblyAITranscriber

def run_all_transcribers(audio_path: str):
    print("\n--- Transcribing Audio: {} ---\n".format(audio_path))

    transcribers = [
        ("OpenAI GPT-4o", OpenAITranscriber()),
        ("Gemini 2.5 Pro", GeminiProTranscriber(api_key="your-gemini-api-key")),
        ("Gemini 2.5 Flash", GeminiFlashTranscriber(api_key="your-gemini-api-key")),
        ("ElevenLabs", ElevenLabsTranscriber()),
        ("AssemblyAI", AssemblyAITranscriber())
    ]

    for name, transcriber in transcribers:
        print(f"{name}:")
        try:
            result = transcriber.transcribe(audio_path)
        except Exception as e:
            result = f"[ERROR] {e}"
        print(result)
        print("-" * 50)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <audio_file_path>")
        sys.exit(1)

    audio_file_path = sys.argv[1]
    run_all_transcribers(audio_file_path)