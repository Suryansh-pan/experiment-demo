import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os 
import smtplib
#email ke liye dictionary bna kr yha pe user ke naam key se aur unka email value se print kra skte hai 
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voice[1].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
      hour=int(datetime.datetime.now().hour)
      if hour>=0 and hour<12:
            speak("Hello sir it your morning time please utilize it anyway ")

      elif hour>=12 and hour<18:
            speak("hello suryansh sir i am your jarvis it is your evening time lets fuck of the work shutup all the thoughts of your mind and completely go to sleep ")
        
      else:
            speak("Hello suryansh boss it is your night time please utilize it sir")

            speak("I am jarvis Sir.Please tell me how may i help you ")
def takecommand():
      
      r = sr.Recognizer()
      with sr.Microphone() as source:
          print("Listening...")
          r.pause_threshold = 1
          audio = r.listen(source)
          try:
              print("Recognizing...")
              query = r.recognize_google(audio, language='en-in')
              print(f"User said: {query}\n") 
          except Exception as e:
              print(" please say that again suryansh sir .......")
              return "None"
          return query


def sendEmail(to,content):
     server=smtplib.SMTP('smtp.gmail.com,587')
     server.ehlo()
     server.starttls()
     server.login('youremail@gmail.com','your-password-here')
     server.sendmail('youremail@gmail.com', to, content)
     server.close()
     
if _name=="main_" :
    wishme()
    #while :
    if 1:
         query=takecommand().lower()
    #takecommand()
    #logic for executing tasks based on query 
    if 'wikipedia' in query:
         speak('Searching wikipedia...')
         query=query.replace("wikipedia","")
         results=wikipedia.summary(query,sentences=2)
         speak("According to wikipedia")
         print(results)
         speak(results)
    elif 'open youtube' in query:
         webbrowser.open("youtube.com")

    elif 'open google' in query:
         webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
         webbrowser.open("stackoverflow.com")
    elif 'open github' in query:
         webbrowser.open("github.com")
    elif 'open whatsapp' in query:
         webbrowser.open("web.whatsapp.com")
    elif 'open instagram' in query:
         webbrowser.open("instagram.com")
    elif 'play music' in query:
         webbrowser.open("https://open.spotify.com")
    elif'the time' in query:
         strTime=datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Sir, the time is {strTime}")
    elif 'open code' in query:
         codePath="C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.starfile(codepath)
    elif 'email ' in query:
         try:
              speak("What should i say?")
              content=takecommand()
              to="suryanshpandey1001@gmail.com"
              sendEmail(to,content)
              speak("Email has been sent sucessfully sir")
         except Exception as e:
              print(e)
              speak("sorry my freind suryansh bhai. I am not able to send this email right now")