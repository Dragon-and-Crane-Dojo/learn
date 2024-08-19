import os
import time
import requests
import playsound


# UnrealSpeech: https://docs.unrealspeech.com/reference/stream
API_KEY = os.environ['UNREALSPEECH_API_KEY']
filename = 'horse.mp3'

url = "https://api.v7.unrealspeech.com/stream"
voice = 'Scarlett'
say = 'right hand up'

payload = {
    "Text": say,
    "VoiceId": voice,
    "Bitrate": "192k",
    "Speed": "0",
    "Pitch": "1",
    "Codec": "libmp3lame",
    "Temperature": 0.25
}

headers = {
    "accept": "text/plain",
    "content-type": "application/json",
    "Authorization": "Bearer {}".format(API_KEY)
}


content = requests.post(url, json=payload, headers=headers).content

with open(filename, 'wb') as f:
    f.write(content)

playsound.playsound(filename)

# audio playback: https://clouddevs.com/python/libraries-for-audio-processing/
print('raise your left hand and say...')
print('right hand up')
print('put your right hand to your side and say...')
print('left hand to your side')
print('step your left leg out into horse stance and say...')
print('right leg out horse stance')
print('punch and say...')
print('punch kiai!')
