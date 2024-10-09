import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            speech = listener.listen(source)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "jarvis" in instruction:
                instruction = instruction.replace("jarvis", "")
                print(instruction)
    except sr.UnknownValueError:
        pass
    return instruction

def play_jarvis():
    instruction = input_instruction()
    print(instruction)
    if "play" in instruction:
        song = instruction.replace("play", "")
        talk("Playing " + song)
        pywhatkit.playonyt(song)
    elif "time" in instruction:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("Current time: " + time)
    elif "date" in instruction:
        date = datetime.datetime.now().strftime("%d/%m/%Y")
        talk("Today's date: " + date)
    elif "how are you" in instruction:
        talk("I am fine, how about you?")
    elif "what is your name" in instruction:
        talk("I am Jarvis. What can I do for you?")
    elif "who is" in instruction:
        human = instruction.replace("who is", "")
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)
    else:
        talk("Please repeat.")

play_jarvis()
