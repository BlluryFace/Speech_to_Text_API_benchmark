import requests
import os
from elevenlabs import ElevenLabs

from dotenv import load_dotenv
load_dotenv()
class ElevenLabsTranscriber:
    def __init__(self):
        self.client = ElevenLabs(api_key=os.getenv("ELEVEN_KEY"))

    def transcribe(self, audio_path: str) -> str:
        try:
            with open(audio_path, "rb") as f:
                response = self.client.speech_to_text.convert(
                    model_id="scribe_v1",
                    file=f)
            return response.text
        except Exception as e:
            print(f"[ElevenLabs Error] {e}")
            return f"[ElevenLabs transcription failed] {e}"