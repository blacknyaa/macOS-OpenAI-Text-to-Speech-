# OpenAI Text-to-Speech for macOS
A fun project that uses the OpenAI TTS (text-to-speech) model to read selected text on your Mac with a keyboard shortcut. This is instead of using the default macOS accessibility text reader, since OpenAI's text-to-speech sounds much better.

As of June 2024, the OpenAI TTS model is [priced](https://openai.com/api/pricing/) at $15 per 1 million characters processed.

## How It Works
Select some text on a webpage or in the Apple Notes app, for example, and press the keyboard shortcut you defined. A window will appear letting you know how much the request will cost. 

<img width="470" alt="cost" src="https://github.com/ryan-d-gordon/mac-openai-text-to-speech/assets/50992194/76ea01cf-fed3-4ee9-a766-5f5c2308aff6">

If you press continue, after a few seconds, the OpenAI-generated audio will start playing out of your system's default audio output.
<br>
<br> 

### Behind the Curtain
I'm using a combination of Python and Apple Scripts, plus an Automator Workflow to tie it all together and turn it into a macOS "Quick Action". Here's the Automator Workflow: 
<br><br>
<img width="500" alt="automator" src="https://github.com/ryan-d-gordon/mac-openai-text-to-speech/assets/50992194/cf66f006-183d-4444-8914-dd7b2335a8a0">




## Setup and Install
1. If you don't already have one, sign up for an OpenAI account and generate an API key. See their [quickstart guide](https://platform.openai.com/docs/quickstart) for more info.
2. Install the OpenAI Python library `pip install openai`
3. Download both Python scripts `openai-text-to-speech.py` and `openai-tts-cost-estimator.py` and the `OpenAI Text to Speech.zip` file containing the Automator Workflow from this repo.
4. Open `openai-text-to-speech.py` and replace `YOUR_OPENAI_API_KEY_GOES_HERE` with your OpenAI API key.
5. Place both Python scripts in `/usr/local/bin`.
6. Unzip the `OpenAI Text to Speech.zip` file and double click the `OpenAI Text to Speech.workflow` file to install it as a System Quick Action, or right click and open it with Automator to modify it to your liking first.

   <img width="602" alt="install-service" src="https://github.com/ryan-d-gordon/mac-openai-text-to-speech/assets/50992194/6d585aab-32c6-4e39-b40b-f13264c8d3ae">

7. Finally, set up a keyboard shortcut on your Mac by visiting System Settings > Keyboard > Keyboard Shortcuts... > Services. Expand the `Text` list and find the `OpenAI Text to Speech` we just installed. Define your desired shortcut.

<br> You can also run the Quick Action/Service by right clicking on any selected text, and selecting the action from the `Services` menu option:

<img width="532" alt="Screenshot 2024-06-10 at 1 02 47 AM" src="https://github.com/ryan-d-gordon/mac-openai-text-to-speech/assets/50992194/d018055e-e8c8-417c-8eca-836e2028a80f">
