import speech_recognition as sr
 
audio_path =  str(input("Enter path to a '.wav' file (not more than 10MB):"))
audio_file = sr.AudioFile(audio_path)
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
file =  open(txt_file, 'w')
file.write(transcript)
file.close()
