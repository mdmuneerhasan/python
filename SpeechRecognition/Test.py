import speech_recognition as sr

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print('[search edureka: search youtube]')
    print('speak now')
    audio = r3.listen(source)
    get = r2.recognize_google(audio)
    print(get)


