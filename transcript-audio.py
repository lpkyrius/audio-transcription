import speech_recognition as sr
from pydub import AudioSegment
import tempfile
import os

service = "Google Speech Recognition"
audio_dir = "audios/"
original_file = os.path.join(audio_dir, "original.m4a")
audio = AudioSegment.from_file(original_file, format="m4a")

# Create a temporary file in the same directory
temp_fd, temp_wav_path = tempfile.mkstemp(suffix=".wav", dir=audio_dir)
os.close(temp_fd)
# Export audio to the temporary file
audio.export(temp_wav_path, format="wav")

recognizer = sr.Recognizer()

with sr.AudioFile(temp_wav_path) as source:
    # process in 60-second chunks, since the audio may be long
    audio_data = recognizer.record(source, duration=60)

try:
    transcription = recognizer.recognize_google(audio_data)
    print('Here is the audio file transcription:')
    print('📝 Starting...')
    print()
    print(transcription)
    print()
    print('📝 Finished!')
except sr.UnknownValueError:
    print(f"{service} could not understand the audio")
except sr.RequestError as e:
    print(f"Could not request results from {service} service; {e}")

# Delete the temporary file
os.remove(temp_wav_path)
