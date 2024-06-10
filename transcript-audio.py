import speech_recognition as sr
from pydub import AudioSegment

# Convert the m4a file to wav using pydub
service = "Google Speech Recognition"
audios_folder = "audios/"
audio = AudioSegment.from_file(f"{audios_folder}original.m4a", format="m4a")
audio.export(f"{audios_folder}to-transcript.wav", format="wav")

recognizer = sr.Recognizer()

with sr.AudioFile(f"{audios_folder}to-transcript.wav") as source:
    # process in 60-second chunks
    audio_data = recognizer.record(source, duration=60)
try:
    # Perform transcription
    transcription = recognizer.recognize_google(audio_data)
    print('Here is the audio file transcription:')
    print('📝')
    print(transcription)
    print('📝')
except sr.UnknownValueError:
    print(f"{service} could not understand the audio")
except sr.RequestError as e:
    print(f"Could not request results from {service} service; {e}")
