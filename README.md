# Audio Transcription with Python

This project demonstrates how to transcribe an audio file (in `.m4a` format - usually created with Apple Voice Memos) to text using Python. It utilizes the `pydub` library for audio processing and the `speech_recognition` library for speech-to-text conversion.

## Requirements

- Python 3.6+
- `pydub` library
- `speech_recognition` library
- `ffmpeg` (for handling audio files)

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/your-username/audio-transcription.git
   cd audio-transcription
    ```

2.	Create and activate a virtual environment (optional but recommended):
    ```
    python -m venv venv
    # For Mac or Linux
    source venv/bin/activate  
    # On Windows, use 
    venv\Scripts\activate
     ```

3.	Install ffmpeg:
	•	macOS:
    `brew install ffmpeg`
    •	Windows:
	Download FFmpeg from FFmpeg’s official download page.
	Extract the downloaded zip file to a directory (e.g., C:\ffmpeg).
	Add C:\ffmpeg\bin to your system’s PATH environment variable.
	•	Linux:
    ```
    sudo apt update
    sudo apt install ffmpeg
    ```
4.	Install the required Python packages:
    `pip install -r ./requirements.txt`

## Usage

1.	Place your .m4a audio file inside audios folder
2.  Rename your file to original.m4a
3.  Run the transcription script:
`python transcript-audio.py`
4.	Check the console output for the transcribed text.

_There is an audio example inside audios folder._

## Troubleshooting

1. FileNotFoundError: [Errno 2] No such file or directory: ‘ffprobe’:
    Ensure that ffmpeg and ffprobe are installed and correctly added to your system’s PATH.
2. speech_recognition.exceptions.UnknownValueError:
    This error indicates that the API could not understand the audio. Ensure the audio is clear and free of significant background noise.

## Contributing

Feel free to open issues or submit pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.