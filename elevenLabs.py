import requests
import os

class ElevenLabsTranscriber:
    def __init__(self):
        self.api_key = os.getenv("ELEVEN_API_KEY")
        self.endpoint = "https://api.elevenlabs.io/v1/speech-to-text"

    def transcribe(self, audio_path: str) -> str:
        try:
            with open(audio_path, "rb") as f:
                response = requests.post(
                    self.endpoint,
                    headers={"xi-api-key": self.api_key},
                    files={"audio": f}
                )
            response.raise_for_status()
            return response.json().get("text", "[No transcription]")
        except Exception as e:
            print(f"[ElevenLabs Error] {e}")
            return "[ElevenLabs transcription failed]"