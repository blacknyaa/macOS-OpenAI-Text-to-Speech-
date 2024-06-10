from openai import OpenAI
import subprocess
import sys

# Designed for macOS
# This script converts text to speech using OpenAI's TTS (text-to-speech) API and plays the resulting audio automatically.
# It accepts the text as a command line argument.

# Replace YOUR_OPENAI_API_KEY_GOES_HERE with your OpenAI API key
API_KEY = "YOUR_OPENAI_API_KEY_GOES_HERE"

def text_to_speech(text, api_key, output_file):
    # Convert text to speech using the OpenAI API.
    client = OpenAI(api_key=api_key)
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    response.stream_to_file(output_file)

if __name__ == "__main__":
    text = " ".join(sys.argv[1:])
    output_file = "/tmp/output.mp3"

    # Convert text to speech
    text_to_speech(text, API_KEY, output_file)
    print(f"Speech saved to {output_file}")

    # Play the audio file
    subprocess.run(["afplay", output_file])
