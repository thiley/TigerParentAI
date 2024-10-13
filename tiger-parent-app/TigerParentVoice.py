
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
    text = "Go ou'? Why you always wan' go ou'? You no have be'er tings to do? Always wastin' time! Your cousin Timmy never go ou'. He always studyin', always winnin' awards. You wan' be lazy? Fine, go ahead! But you no do anytin' productive anyway. You prob'ly just sit around, talk nonsense, waste more time. But also, why you even have friends? You no need friends! Focus on studyin'!"
    text_to_speech_file(text)
