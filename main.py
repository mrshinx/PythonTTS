import speech_recognition as sr
import pyttsx3
from datetime import date, datetime
import re

# Define user, bot and dict of responses
You = ""
Assistant = "Hello, please say something"
Responses = {
    "hello": "Hi",
    "how are you": "I'm fine, thank you",
    "what day is it today": date.today().strftime("%B %d, %Y"),
    "what time is it": datetime.now().strftime("%H:%M")
}

# Define exit pattern
pattern = re.compile(r"bye")

# obtain audio from the microphone and initialize bot audio
r = sr.Recognizer()
engine = pyttsx3.init()

# Begin
print(f'Assistant: {Assistant}')
engine.say(Assistant)
engine.runAndWait()

# Loop
while not (pattern.search(You)):
    with sr.Microphone() as source:
        audio = r.listen(source)

    # Recognize speech using Google Speech Recognition
    try:
        You = r.recognize_google(audio)
        print(f"You: {You}")
    except sr.UnknownValueError:
        print("I cannot understand what you said, please say it again.")
        continue
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        break

    if You in Responses:
        Assistant = Responses[You]
        print(f"Assistant: {Assistant}")
        engine.say(Assistant)
        engine.runAndWait()
        continue
    elif pattern.fullmatch(You):
        Assistant = "Goodbye"
        print(f"Assistant: {Assistant}")
        engine.say(Assistant)
        engine.runAndWait()
        break
    else:
        Assistant = "I'm not smart enough to answer that"
        print(f"Assistant: {Assistant}")
        engine.say(Assistant)
        engine.runAndWait()
        continue
