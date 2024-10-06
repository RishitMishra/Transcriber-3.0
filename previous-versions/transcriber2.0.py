import speech_recognition as sr 
from pydub import AudioSegment
import pydub.utils as pdu
 
audio_path =  str(input("Enter path to a '.wav' file:"))

sound = AudioSegment.from_file(audio_path)

chunk_length_ms = 110000 #5min.inmilliseconds
chunks =  pdu.make_chunks(sound, chunk_length_ms)

for chunk in chunks:
    chunk = chunk.export(format = "wav")
    audio_file = sr.AudioFile(chunk)
    reco =  sr.Recognizer()
    try:
        with audio_file as source:
            reco.adjust_for_ambient_noise(source)
            data = reco.record(source)
            global transcript
            transcript = reco.recognize_google(data, language = "en-IN")
    except Exception as e:
        print(e)
        print("Couldn't understand!!!")

    print("transcript:\n",transcript)

    a = audio_path.split(".") 
    txt_file = a[0] + ".txt"
    file =  open(txt_file, 'a')
    file.write(transcript + " ")
    file.close()
