import google.generativeai as genai

class GeminiProTranscriber:
    def __init__(self, api_key=None):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

    def transcribe(self, audio_path: str) -> str:
        try:
            with open(audio_path, "rb") as audio_file:
                response = self.model.generate_content(audio_file)
            return response.text
        except Exception as e:
            print(f"[Gemini Pro Error] {e}")
            return "[Gemini Pro transcription failed]"