import os
import random

def getaudio():
    audio_file_name = random.choice(os.listdir(r"C:\Users\birdl\Desktop\Year_2\Programming\Python\Praise_God\music_samples"))
    return audio_file_name

getaudio()
