#!/usr/bin/env python
# coding: utf-8

# Audio Pen

from fastapi import FastAPI, Request
from openai import OpenAI
from pydantic import BaseModel
import json
from fastapi.middleware.cors import CORSMiddleware

class AudioTranscriptRequest(BaseModel):
    transcript: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/")
async def generate_refined_transcription(Audiotranscript: AudioTranscriptRequest):
    transcriptValue = Audiotranscript.transcript
   
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
    {"role": "system", "content": f"You are AI assistant to clean the following text and do not include the data cutoff.:\n{transcriptValue}"}]
    )
    
    summary = completion.choices[0].message.content
    #summary = "Success"
    return {"summary": summary}
    
#@app.get("/")
#async def generate_refined():
    #transcriptValue = Transcript
    #return {transcriptValue}
#    return("You are in the GET method")



