import whisper
import os

model = whisper.load_model("base")
with open("metadata.csv", "w") as f:
    for filename in os.listdir("wavs"):
        if filename.endswith(".wav"):
            path = os.path.join("wavs", filename)
            result = model.transcribe(path, fp16=False)
            f.write(f"{path}|{result['text'].strip()}\n")
            print(f"Processed: {filename}")
