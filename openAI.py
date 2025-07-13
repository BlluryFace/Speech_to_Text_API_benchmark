import openai
import os

class OpenAITranscriber:
    def __init__(self):
        self.client = openai.OpenAI()

    def transcribe(self, audio_path: str) -> str:
        try:
            with open(audio_path, "rb") as audio_file:
                response = self.client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a transcription assistant. Transcribe the following audio to plain text."
                        },
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text",
                                    "text": "Here is the audio I want you to transcribe."
                                },
                                {
                                    "type": "audio",
                                    "audio": audio_file
                                }
                            ]
                        }
                    ]
                )
            return response.choices[0].message.content
        except Exception as e:
            print(f"[OpenAI GPT-4o Error] {e}")
            return "[OpenAI GPT-4o transcription failed]"