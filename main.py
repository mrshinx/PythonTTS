import speech_recognition as sr
import pyttsx3
from datetime import date, datetime

# Define user, bot and dict of responses
You = ""
Assistant = "Hello, please say something"

# obtain audio from the microphone and initialize bot audio
r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change default voice to female

# Begin
print(f'Assistant: {Assistant}')
engine.say(Assistant)
engine.runAndWait()

# Loop
while True:
    with sr.Microphone() as source:
        audio = r.listen(source)

    # Recognize speech using Google Speech Recognition
    try:
        You = r.recognize_google(audio)
        print(f"You: {You}")
    except sr.UnknownValueError:
        Assistant = "I cannot understand what you said, please say it again."
        print(f"Assistant: {Assistant}")
        engine.say(Assistant)
        engine.runAndWait()
        continue
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        break

    # Response cases
    if "hello" in You:
        Assistant = "Hi"
    elif "hi" in You:
        Assistant = "Hey there"
    elif "time" in You:
        Assistant = datetime.now().strftime("%H:%M")
    elif ("date" in You) or ("day" in You):
        Assistant = date.today().strftime("%B %d, %Y")
    elif You == "how are you":
        Assistant = "I'm fine, thank you"
    elif "bye" in You:
        Assistant = "Goodbye"
    else:
        Assistant = "I'm not smart enough to answer that"

    print(f"Assistant: {Assistant}")
    engine.say(Assistant)
    engine.runAndWait()
    if Assistant == "Goodbye":
        break
