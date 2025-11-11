from django.shortcuts import render, redirect
from gtts import gTTS
import playsound


# def home(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         if name:
#             text = f"{name} teri maa ki chut"
#             sound = gTTS(text, lang = "en")
#             sound.save("my_aound.mp3")
#             playsound.playsound("my_aound.mp3")

#     return render(request, 'app/home.html')


from django.shortcuts import render
from gtts import gTTS
import os, random

def home(request):
    audio_file = None
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            file_path = os.path.join(os.path.dirname(__file__), 'messages.txt')
            with open(file_path, 'r') as f:
                messages = [line.strip() for line in f if line.strip()]
            random_message = random.choice(messages)

            tts = gTTS(text=f"{name}, {random_message}", lang='en')
            path = f"media/audio/{name}.mp3"
            os.makedirs(os.path.dirname(path), exist_ok=True)
            tts.save(path)
            audio_file = '/' + path  # static/media file URL


    return render(request, 'app/home.html', {'audio_file': audio_file})
