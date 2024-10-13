
import os
import uuid
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)


def text_to_speech_file(text: str) -> str:
    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id="mbL34QDB5FptPamlgvX5", # Adam pre-made voice
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_turbo_v2_5", # use the turbo model for low latency
        voice_settings=VoiceSettings(
            stability=0.7,
            similarity_boost=0.78,
            style=0.47,
            use_speaker_boost=True,
        ),
    )

    # uncomment the line below to play the audio back
    # play(response)

    # Generating a unique file name for the output MP3 file
    save_file_path = f"{uuid.uuid4()}.mp3"

    # Writing the audio to a file
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: A new audio file was saved successfully!")

    # Return the path of the saved audio file
    return save_file_path

if __name__ == "__main__":
    text = "Make me proud? Hah! You tink dat easy? You tink doin' one or two tings goin' impress me? Look at cousin Mei, she already doctor an' only 25! What you do? Nothin'. Always askin' for approval like child. You no need approval, you need success! You need to win awards, get straight A’s, be best at everytin'. Even den, maybe not enough.But honestly, you prob'ly never be like Mei or Timmy anyway. So why you bo'der try?"
    text_to_speech_file(text)
