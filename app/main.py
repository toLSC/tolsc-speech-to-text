from fastapi import FastAPI, UploadFile
from fastapi.responses import PlainTextResponse
import os
import tempfile
import whisper

app = FastAPI()

model_name = os.getenv("W_MODEL", "base")
model = whisper.load_model(model_name)

@app.post("/speech-to-text")
def speech2text(audio_file: UploadFile):
  if not audio_file.filename.endswith(".m4a"):
    error_message = "Invalid file type. Expected .m4a"
    return PlainTextResponse(content=error_message, status_code=500)
  with tempfile.NamedTemporaryFile() as fp:
    fp.write(audio_file.file.read())
    try:
      ans = model.transcribe(fp.name, fp16=False)['text']
      return PlainTextResponse(ans)
    except:
      error_message  = "Transcription error"
      return PlainTextResponse(content=error_message, status_code=500)