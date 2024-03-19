from gtts import gTTS

class UserAudio:
    def __init__(self, text=None, language="en", slow=True, accent="com"):
        self.lang = language
        self.slow = slow
        self.accent = accent

        if text is None:
            self.user_input()
        else:
            self.text_to_audio = text

        self.gtts_object = gTTS(
            text=self.text_to_audio, lang=self.lang, slow=self.slow, tld=self.accent
        )

    def user_input(self):
        text = input("Enter the text you want to convert to audio: ")
        self.text_to_audio = text
        self.gtts_object = gTTS(
            text=self.text_to_audio, lang=self.lang, slow=self.slow, tld=self.accent
        )

    def save_audio(self, filename):
        """
        Save the audio to a file.

        Args:
            filename (str): The name of the output audio file (e.g., "output.mp3").
        """
        self.gtts_object.save(filename)
        print(f"Audio saved as {filename}")


audio = UserAudio("Hello, this is a test.")
audio.save_audio("output.mp3")
print("Audio saved as output.mp3")
        
# Example usage:
# audio = UserAudio("Hello, this is a test.")
# audio.save_audio("output.mp3")
# print("Audio saved as output.mp3")

