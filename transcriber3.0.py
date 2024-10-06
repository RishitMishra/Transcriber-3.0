import speech_recognition as sr 
from pydub import AudioSegment
import pydub.utils as pdu
import docx 
from docx.shared import Pt
 
audio_path =  str(input("Enter path to a '.wav' file:"))
ambi =  str(input("Enable Ambient noise cancellation (Y/N):"))

sound = AudioSegment.from_file(audio_path)

chunk_length_ms = 30000 #30secondsinmilliseconds
chunks =  pdu.make_chunks(sound, chunk_length_ms)
full_transcript = ""

for chunk in chunks:
    chunk = chunk.export(format = "wav")
    audio_file = sr.AudioFile(chunk)
    reco =  sr.Recognizer()
        
    try:
        with audio_file as source:
            if ambi in ('Y', 'y'):
                reco.adjust_for_ambient_noise(source)
            else:
                pass
            data = reco.record(source)
            global transcript
            transcript = reco.recognize_google(data, language = "en-IN")
    except Exception as e:
        print(e)
        print("Couldn't understand!!!")
    
    full_transcript += transcript 

print("transcript:\n",full_transcript)

a = audio_path.split(".wav") 
doc_file = a[0] + ".docx"
doc = docx.Document()
doc.add_paragraph(full_transcript)
doc.save(doc_file)



