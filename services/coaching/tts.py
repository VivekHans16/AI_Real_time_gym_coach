from io import BytesIO
from gtts import gTTS


class TextToSpeech:

    def speak(self, text, lang="en"):
        cleaned = (text or "").strip()

        if not cleaned:
            print("TTS: Empty text")
            return None

        try:
            print("TTS INPUT:", cleaned)

            buffer = BytesIO()

            gTTS(
                text=cleaned,
                lang=lang
            ).write_to_fp(buffer)

            buffer.seek(0)

            audio = buffer.read()

            print("TTS AUDIO BYTES:", len(audio))

            return audio

        except Exception as e:
            print("TTS ERROR:", repr(e))
            return None