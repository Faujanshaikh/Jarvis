import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialize
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        # Adjust for ambient noise
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening... Please speak now.")
        try:
            audio = r.listen(source, timeout=5)  # Timeout increased to 5 seconds
            text = r.recognize_google(audio)
            print("You said:", text)
            
            # Commands
            if "open YouTube" in text:
                speak("Opening YouTube")
                webbrowser.open("https://www.youtube.com")
            elif "open Google" in text:
                speak("Opening Google")
                webbrowser.open("https://www.google.com")
            else:
                speak("Command not recognized")
                
        except sr.WaitTimeoutError:
            speak("No speech detected. Please try again.")
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
