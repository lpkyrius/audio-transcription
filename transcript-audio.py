import speech_recognition as sr
from pydub import AudioSegment
import tempfile
import os
import time
from datetime import datetime

service = "Google Speech Recognition"
audio_dir = "audios/"
original_file = os.path.join(audio_dir, "original.m4a")
audio = AudioSegment.from_file(original_file, format="m4a")

audio_duration_minutes = len(audio) / 1000 / 60
audio_duration_minutes_text = f"{audio_duration_minutes:.2f}"
print(f"\nThe original audio duration is approximately \
      {audio_duration_minutes_text.strip()} minutes.")
print('\nProcessing the audio file...\n')

temp_fd, temp_wav_path = tempfile.mkstemp(suffix=".wav", dir=audio_dir)
os.close(temp_fd)
audio.export(temp_wav_path, format="wav")

recognizer = sr.Recognizer()

start_time = time.time()

with sr.AudioFile(temp_wav_path) as source:
    offset = 0
    chunk_size = 5  # Process in 5-second chunks to reduce transcription loses
    transcription = []
    issue_count = 0

    while True:
        try:
            # Read a chunk
            audio_data = recognizer.record(source,
                                           duration=chunk_size,
                                           offset=offset)
            if len(audio_data.frame_data) == 0:
                break  # End of file reached

            # Recognize the chunk
            chunk_transcription = recognizer.recognize_google(audio_data)
            transcription.append(chunk_transcription)
        except sr.UnknownValueError:
            print(f"{service} could not understand the audio at offset \
                  {offset} seconds")
            transcription.append(f"[**{chunk_size} secs with audio issues**]")
            issue_count += 1
        except sr.RequestError as e:
            print(f"Could not request results from \
                  {service} service at offset \
                  {offset} seconds; {e}")
            transcription.append(f"[**{chunk_size} secs with audio issues**]")
            issue_count += 1
        finally:
            offset += chunk_size  # Move to the next chunk

end_time = time.time()  # Record the end time
processing_time = end_time - start_time

# Join all the chunks into a single transcription
full_transcription = " ".join(transcription)

# Get the current date and time in YYYYMMDDmmss format
current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
output_file = os.path.join(audio_dir, f"{current_datetime}.txt")

# Save the transcription to the file
with open(output_file, "w") as file:
    print("\n📝 Saving the audio file transcription...")
    file.write(full_transcription)
    print("📝 Finished!\n")

print(f"Total chunks with issues: {issue_count}")
print(f"Total processing time: {processing_time:.2f} seconds")
print(f"Transcription saved to {output_file}")

# Delete the temporary file
os.remove(temp_wav_path)
