import os
from google import genai
from dotenv import load_dotenv
load_dotenv()

class GeminiFlashTranscriber:
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GEMINI_KEY"))

    def transcribe(self, audio_path: str) -> str:
        try:
            with open(audio_path, "rb") as audio_file:
                myfile = self.client.files.upload(file=audio_path)

                response = self.client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=["Transcribe this audio clip, do not include any"
                              "thing else except the content of the audio",
                              myfile]
                )
            return response.text
        except Exception as e:
            print(f"[Gemini Flash Error] {e}")
            return "[Gemini Flash transcription failed]"