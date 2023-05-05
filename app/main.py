from fastapi import FastAPI, UploadFile, File
from fastapi.responses import PlainTextResponse
import os
import tempfile
import whisper

app = FastAPI()

model_name = os.getenv("W_MODEL", "base")
model = whisper.load_model(model_name)

@app.post("/speech-to-text")
async def speech2text(audio_file: UploadFile = File(...)):
  if not audio_file:
    error_message = "No audio sent"
    return PlainTextResponse(content=error_message, status_code=400)
  else:
    print({"filename": audio_file.filename})
  if not audio_file.filename.endswith(".m4a"):
    error_message = "Invalid file type. Expected .m4a"
    return PlainTextResponse(content=error_message, status_code=400)
  with tempfile.NamedTemporaryFile() as fp:
    fp.write(audio_file.file.read())
    try:
      ans = model.transcribe(fp.name, fp16=False)['text']
      return PlainTextResponse(ans)
    except:
      error_message  = "Transcription error"
      return PlainTextResponse(content=error_message, status_code=500)