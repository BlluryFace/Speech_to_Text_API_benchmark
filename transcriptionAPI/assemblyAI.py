import requests
import time
import os

from dotenv import load_dotenv
load_dotenv()

class AssemblyAITranscriber:
    def __init__(self):
        self.api_key = os.getenv("ASSEMBLYAI_KEY")
        self.upload_url = "https://api.assemblyai.com/v2/upload"
        self.transcript_url = "https://api.assemblyai.com/v2/transcript"

    def _upload(self, audio_path: str) -> str:
        try:
            with open(audio_path, "rb") as f:
                response = requests.post(
                    self.upload_url,
                    headers={"authorization": self.api_key},
                    files={"file": f}
                )
            response.raise_for_status()
            return response.json()["upload_url"]
        except Exception as e:
            print(f"[AssemblyAI Upload Error] {e}")
            raise RuntimeError("Upload failed")

    def transcribe(self, audio_path: str) -> str:
        try:
            audio_url = self._upload(audio_path)
            response = requests.post(
                self.transcript_url,
                json={"audio_url": audio_url},
                headers={"authorization": self.api_key}
            )
            response.raise_for_status()
            transcript_id = response.json()["id"]

            while True:
                poll = requests.get(f"{self.transcript_url}/{transcript_id}", headers={"authorization": self.api_key})
                poll.raise_for_status()
                status = poll.json()["status"]
                if status == "completed":
                    return poll.json()["text"]
                elif status == "error":
                    print(f"[AssemblyAI Poll Error] {poll.json()}")
                    return "[AssemblyAI transcription failed]"
                time.sleep(2)
        except Exception as e:
            print(f"[AssemblyAI Error] {e}")
            return f"[AssemblyAI transcription failed]: {e}"