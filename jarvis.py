import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
rate=engine.setProperty("rate", 185)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        r.pause_threshold = 1
        audio=r.listen(source,timeout=10, phrase_time_limit=5)

    try:
        print('Recognizing...')
        query= r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        print(e)
        speak('Say again please')
        return 'none'
    return query    

def greet_user():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good Morning sir")
    elif hour>12 and hour<18:
        speak("Good Afternoon sir")
    else:
        speak("Good Evening sir")
    speak("I am Hydra. Please tell me how can I help you")    


if __name__ == '__main__':  
    greet_user()
    if 1:
        query=takeCommand().lower()

        #tasks
        if "open notepad" in query:  
            npath="C:\\Windows\\notepad.exe"
            os.startfile(npath)

        elif "open adobe reader" in query:
            apath="C:\\Program Files\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe"
            os.startfile(apath)  

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in  query or "show webcam" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret, img=cap.read()
                cv2.imshow('Webcam',img)
                k=cv2.waitKey(50)
                if k==27: 
                    break
            cap.release()
            cv2.destroyAllWindows()

        #elif "open music" in query:
        #   music_dir="C:\\Program Files (x86)\\K-Lite Codec Pack\\Media Player Classic\\mplayerc.exe"
        #   songs=os.listdir(music_dir)
        #   rd=random.choice(songs)
        #   os.startfile(os.path.join(music_dir, rd))
            
        elif "ip address" in query:
            ip=get("https://api.ipify.org").text
            speak(f"Your IP address is: {ip}")

        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            # print(results)

        elif "open youtube" in query:
            webbrowser.open("http://www.youtube.com")
            speak("Opening YouTube")
            
        elif "open facebook" in query:
            webbrowser.open("http://www.facebook.com")
            speak("Opening Facebook")

        elif "open google" in query:
            speak("What should I search for?")
            cm=takeCommand().lower
            webbrowser.open(f"{cm}")
            speak("Google Search opened, sir.")

        elif "open stackoverflow" in query:
            webbrowser.open("https://stackoverflow.com/")
            speak("StackOverFlow page opened, sir.")

        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")        
            speak(f"Sir, the current time is {strTime}")    

        elif "open code" in query:
            vpath= "C:\\Users\\deepd\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vpath)  
            speak("Visual Studio Code has been opened,sir")   

        elif "send message" in query:
            kit.sendwhatmsg("+918670742869", "testing", 8,35)

        elif "play song on youtube" in query:
           kit.playonyt("see you again sir")

        elif "write an email" in query:
            print("To whom do you want to send the email?")
            speak("To whom do you want to send the email?")
            
            recipient_name=takeCommand().lower()
            from sendemail import recipient_mapping
            recipient_email=recipient_mapping.get(recipient_name)

            if recipient_email:
                print("what is the subject of the email?")
                speak("What is the subject of the email?")
                subject= takeCommand().lower()
                from sendemail import send_email
                from sendemail import sender_email
                from sendemail import sender_password

                print("what is the message of the email?")
                speak("What is the message of the email?")
                content=takeCommand().lower()
                send_email(sender_email, sender_password, recipient_email, subject, content)
            else:
                print("Sorry not able to find details")
                speak("Sorry not able to find details")
                

