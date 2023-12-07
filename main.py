import os
import pyaudio
from gtts import gTTS
from playsound import playsound

def generate_audio_file(text):
    audio = gTTS(text=text, lang='ja', slow=False)
    audio.save("response.mp3")

def play_audio_file():
    os.system("mpg321 response.mp3")
    playsound("response.mp3", block=False)

if __name__ == "__main__":
    generate_audio_file("あいうえお")
    play_audio_file()

