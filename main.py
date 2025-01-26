import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")  
    elif "open linkedin" in c.lower():
        webbrowser.open("inkedin.com/in/vikas-rajliwal-42b668274/")  
    elif c.lower().startswith("play"):
        song =c.lower().split()
        link =music_library.music[song]
        webbrowser.open(link)
          
recogniser= sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
if __name__ == "__main__":
    speak("Initializing jarvis...")
    while True:
        # listen for the wake weywords 
        #take audio from microphone 
        r= sr.Recognizer()
        
            
        try:
            with sr.Microphone() as source:
                print("Litining...")
                audio=r.listen(source,timeout=2,phrase_time_limit=1)
            word=r.recognize_google(audio)
            print(f"{word}")
            if(word.lower()=="hello"):
                speak("ya")
                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis activate...")
                    audio=r.listen(source)
                command =r.recognize_google(audio)
                print(f"{command}")
                processCommand(command)
           
        except sr.UnknownValueError:
            print("could not understand the audio")
        except sr.RequestError as e :
            print("error ".format(e))
        except sr.WaitTimeoutError:
                print("Listening timed out. No speech detected.")            