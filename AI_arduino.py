import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import cv2

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('V7EAL6-688W6GAJQ6')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello Sir, I am your digital assistant Arduino!')
speak('How may I help you?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Can you repeat that?')
        query = myCommand()

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')
    
        elif "who made you" in query:
            username_prasoon = ("Prasoon rai made me... Thanks to him!")
            speak(username_prasoon)

        elif "make my notes" in query or "make notes for my class" in query or "make my classroom notes" in query:
           speak("Ok you can write your notes here...")
           speak("Please tell me your name for notes...")
           notes_name = myCommand()
           while True:
              note = myCommand()
              print((notes_name) + " posted: " + (note))
                         
              if "<exitnote>" in note or "exit note" in note or "exit notes" in note:
                  break

        elif "play music" in query:
            speak("Which music would you like to hear?")
            mine = myCommand()
            webbrowser.open(mine)

        elif "start a local chat" in query or "local chat" in query:
            speak("Ok, starting a local chat ")
            speak("I am going to be the host ")
            speak("However, the server code for this computer is 'LAPTOP-2R3CKJJJ' ")
            speak("Code = LAPTOP-2R3CKJJJ")
            speak("Mean while I am opening both the programs...")
            from subprocess import *
            import time
            Popen('python server.py')
            Popen('python client.py')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')
        
        elif 'play song' in query:
            music_folder = 'C:\\Users\\praso_\\Music'
            music = ['BEST OF ALAN WALKER - New Songs Alan Walker 2019 - Top 20 Alan Walker Songs 2019' , 'Marshmello - Alone (Official Music Video)' , 'Marshmello - Stars (Official Music Video)' , 'Marshmello - Summer (Official Music Video) with Lele Pons' , 'Marshmello - Together (Official Music Video)']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "set a alarm" in query or "set a timer" in query:
            speak("Ok, so please enter the timer settings...")
            from subprocess import *
            import time
            Popen('python alarm.py')

        elif "would you marry me" in query or "marry me" in query:
            speak("Hmmmm...")
            speak("Before answering this question you need to answer some questions...")
            speak("There are three questions!")
            speak("Are you ready?")
            speak("Let's begin...")
            speak("1... Where do I live?")
            A_A = myCommand()
            if "in clouds" in A_A or "in cloud" in A_A:
                speak("Correct answer...")

            else:
                speak("Wrong answer!")
                break
            speak("2. When is my birthday?")
            B_B = myCommand()
            if "eight january" in B_B or "Eight January" in B_B or "8 January" in B_B:
                speak("Great!")

            else:
                speak("Wrong answer!")
                break
            speak("Final question!")
            speak("This one is going to be a bit harder!")
            speak("Let's begin...")
            speak("3. What is my favourit colour?")
            C_C = myCommand()
            if "grey" in C_C or "Grey" in C_C:
                speak("Great you passed the test!")
                speak("However rightnow I am wrapping my head around the myth of love")
                speak("So, for now I would like to give my answer with this music...")
                webbrowser.open('https://www.youtube.com/watch?v=lNmAkWvnWEg')
                

            else:
                speak("Nah...")
                speak("Wrong answer....")
                speak("I think we need more time to get to know each other!")
                
            

        elif "read my notes" in query or "read by note" in query:
            speak("Reading your notes...")
            speak((notes_name) + " posted: " + (note))

        elif "start face recognition" in query or "<facerecognition>" in query or "starfish recognition" in query or "starfish organization" in query or "face recognition" in query:
            speak("Starting face recognition...")
            from subprocess import *
            import time
            Popen('python detect_face_video.py')

        elif "what are your secret" in query or "what are your secrets" in query or "what are your secret" in query:
            speak("If I will tell you my secret it will not be a secret!")

        elif "Set a alarm" in query or "set a timer" in query:
            speak("alarm for what time?")


        elif "open amazon" in query:
            webbrowser.open('www.amazon.in')

        elif "open youtube music" in query:
            webbrowser.open('https://music.youtube.com/')

        elif "play alone" in query:
            webbrowser.open('https://www.youtube.com/watch?v=ALZHF5UqnU4')

        elif "play happier" in query:
            webbrowser.open('https://www.youtube.com/watch?v=m7Bc3pLyij0')


        elif "play stars" in query:
            webbrowser.open('https://www.youtube.com/watch?v=A57B7B6w3kw')

        elif "play alone by allen walker" in query:
            webbrowser.open('https://www.youtube.com/watch?v=1-xGerv5FOk')

        elif "play alone by marshmello" in query:
            webbrowser.open('https://www.youtube.com/watch?v=ALZHF5UqnU4')

        elif "play centuries" in query:
            webbrowser.open('https://www.youtube.com/watch?v=ICK0TqVQT9M&t=5s')

        elif "play beliver" in query:
            webbrowser.open('https://www.youtube.com/watch?v=0J8lU5yQfZk')

        elif "play ignite" in query:
            webbrowser.open('https://www.youtube.com/watch?v=Az-mGR-CehY')

        elif "on my way" in query:
            webbrowser.open('https://www.youtube.com/watch?v=dhYOPzcsbGM')

        elif "play blocks" in query:
            webbrowser.open('https://www.youtube.com/watch?v=5E4ZBSInqUU')

        elif "play faded" in query:
            webbrowser.open('https://www.youtube.com/watch?v=60ItHLz5WEA')

        elif "play darkside" in query:
            webbrowser.open('https://www.youtube.com/watch?v=M-P4QBt-FWw')

        elif "play top songs by allen walker" in query:
            webbrowser.open('https://www.youtube.com/watch?v=WWCsGEarExg')

        elif "play cheap thrills" in query:
            webbrowser.open('https://www.youtube.com/watch?v=nYh-n7EOtMA')

        elif "play sorry" in query:
            webbrowser.open('https://www.youtube.com/watch?v=fRh_vgS2dFE')

        elif "play let me love you" in query:
            webbrowser.open('https://www.youtube.com/watch?v=euCqAq6BRa4')

        elif "play what do you mean" in query:
            webbrowser.open('https://www.youtube.com/watch?v=DK_0jXPuIr0')

        elif "play sorry" in query:
            webbrowser.open('https://www.youtube.com/watch?v=fRh_vgS2dFE')

        elif "play baby" in query:
            webbrowser.open('https://www.youtube.com/watch?v=kffacxfA7G4')

        elif "play top songs by justin biber" in query:
            webbrowser.open('https://www.youtube.com/watch?v=1uL3MWtpJOA')

        elif "play top songs by marshmello" in query:
            webbrowser.open('https://www.youtube.com/watch?v=bJQ_nIK9rzo')
        
        elif "open whatsapp" in query or "open watsapp" in query:
             webbrowser.open('https://web.whatsapp.com/')

        elif "open my amazon cart" in query:
            webbrowser.open('https://www.amazon.com/gp/cart/view.html/ref=lh_cart')

        elif "open my flipkart cart" in query:
            webbrowser.open('https://www.flipkart.com/viewcart?otracker=Cart_Icon_Click')

        elif "open flipkart" in query:
            webbrowser.open('www.flipkart.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient or "mi" in recipient or "MI" in recipient or "ME" in recipient or "Mi" in recipient or "Me" in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            sys.exit()

        
        elif 'hello' in query:
            speak('Hello Sir')

        
        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('Got it.')
                    speak('WOLFRAM-ALPHA says -')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                speak("Sorry sir I don't know that one!")
        
        speak('Next Command! Sir!')
