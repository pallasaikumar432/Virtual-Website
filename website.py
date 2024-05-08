import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize the recognizer
r = sr.Recognizer()

# Initialize text to speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    # use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        command = r.recognize_google(audio)
        print("You said: " + command)
        return command
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

def open_website(command):
    print(f"Received command: {command}")  # Debug print
    if 'open' in command:
        domain = command.replace('open ', '').strip()
        url = f'http://{domain}.com'
        print(f"Trying to open: {url}")  # Debug print
        webbrowser.open(url)
        speak(f"Opening {domain}")
    else:
        speak("Command not recognized, please try again.")


# Main function to process voice commands
def main():
    speak("Hello, I can open websites for you. Please tell me which site to open by saying, for example, 'open cricbuzz'.")
    command = listen()
    if command:
        open_website(command.lower())

if __name__ == "__main__":
    main()
