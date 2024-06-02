import pyttsx3
import smtplib
import speech_recognition as sr
import datetime
import smtplib

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[0].id)

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
        audio=r.listen(source,timeout=1, phrase_time_limit=5)

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

def send_email(sender_email, sender_password, recipient_email, subject, content):
    from email.message import EmailMessage
    msg=EmailMessage()
    msg['From']=sender_email
    msg['To']=recipient_email
    msg['Subject']=subject
    msg.set_content(content)

    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Login Credentials for sending the mail
    server.login(sender_email, sender_password)
    server.send_message(msg)
    print("Mail has been sent successfully.")
    speak("Mail has been sent successfully.")

recipient_mapping={
    "webit": "deepdutta273@gmail.com"
}    

sender_email= "deepd298670@gmail.com"
sender_password="thpu cmcv kmvo ntqk"