import whisper

# Load the 'base' model from Whisper
model = whisper.load_model("base")

# Transcribe an empty input (you may want to provide actual input here)
transcription_result = model.transcribe("")

# Open the file in append mode and write the transcription result to it
with open("transcription.txt", "a") as output_file:
    output_file.write(transcription_result['text'])
