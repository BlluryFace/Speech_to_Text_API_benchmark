import os

import openai
from dotenv import load_dotenv
load_dotenv()
class OpenAITranscriber:
    def __init__(self):
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_KEY"))

    def transcribe(self, audio_path: str) -> str:
        try:
            with open(audio_path, "rb") as audio_file:
                transcription = self.client.audio.transcriptions.create(
                    model="gpt-4o-transcribe",
                    file=audio_file
                )
            return transcription.text
        except Exception as e:
            print(f"[OpenAI GPT-4o Error] {e}")
            return f"[OpenAI GPT-4o transcription failed] {e}"