import speech_recognition as sr
import pyttsx3
import time
import webbrowser
from commands import *
import keyboard
import pyjokes
import requests
import pywhatkit
from chat import *

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)
ai_name = 'Computer'

def sayOpen():
    say('Opening')

def say(text, bool=True):
    if bool != False:
      print(ai_name+': '+text) 
    engine.say(text)
    engine.runAndWait()

def listen_to_command_with_name(name):
    name = name.lower()
    try:
        with sr.Microphone() as source:
            print('speak...')
            command = ''
            #print("loading... Complete!")
            voice = listener.listen(source, timeout=99999999999999999999999999999999999999999,phrase_time_limit=5)
            temp_com = listener.recognize_google(voice)
            command = temp_com.lower()

            if name in command:
                command = command[(len(name)+1):]
                print('You: '+command)
            else:
                command = ''
        
    except:
        #print("Didn't get that. Please repeat.")
        command = ''
    finally:
        return command

def convertKtoF(variable):
    variable = int(variable)
    variable = ((((variable)-273.15)*1.8)+32)
    variable = round(variable, 1)
    return str(variable)

if int(time.strftime("%H",time.localtime())) < 11:
    say('Good morning, Sapien!')
elif 11>= int(time.strftime("%H",time.localtime())) <= 13:
    say('Good noon, Saviour!')
else:
    say('Good evening, Sapien!')

say('What can I do for you?')

while keyboard.is_pressed('esc')!=True:
    command = listen_to_command_with_name(ai_name)
    if command != '':
        if 'who is' in command:
            if command.startswith("who is"):
                person = command[7:]
                if 'your creator' not in person and 'your inventor' not in person:
                    if ' ' in person:
                        person = person.replace(' ', '+')
                    say('Redirecting you to what I found...')
                    chrome_browser = webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
                    chrome_browser.open_new_tab(("https://www.google.com.tr/search?q={}".format(person)))
        elif 'time' in command:
            t = time.localtime()
            currentH = str(int(time.strftime("%I", t)))
            currentM = str(int(time.strftime("%M", t)))
            amPM = time.strftime('%p',t)
            print("It's currently "+currentH+":"+currentM+" "+amPM)
            say('It is currently ' + currentH + ' ' + currentM+' '+amPM, False)
        elif 'shut down and close' in command:
            shutdownandclose()        
        elif 'open' in command:
            if 'chrome' in command or 'google chrome' in command:
                openChrome()
            elif 'microsoft edge' in command or 'edge' in command:
                openEdge()
            elif 'file explorer' in command or 'files explorer' in command or 'explorer' in command:
                openExplorer()
            elif 'calculator' in command or 'calc' in command:
                openCalc()
            elif 'cmd' in command or 'command prompt' in command:
                openCmd()
            elif 'control panel' in command:
                opencontrolPanel()
            elif 'new note' in command or 'notes' in command or 'notepad' in command or 'notepad++' in command or 'notepad+' in command or 'note'in command:
                openNote()
            elif 'microsoft word' in command or 'word' in command:
                openWord()
            elif 'powerpoint' in command or 'microsoft power point' in command:
                openPowerP()
            elif 'paint' in command or 'draw' in command:
                openPaint()
            elif 'youtube' in command:
                openYt()
            elif 'docs' in command or 'google docs' in command:
                openDocs()
            elif 'amazon' in command:
                openAmazon()
            
            sayOpen()
        elif 'stop' in command or 'exit' in command or 'sleep' in command or 'quit' in command:
            say('Bye Bye!')
            break
        elif 'tell me' in command:
            if 'joke' in command or 'jokes' in command:
                joke = pyjokes.get_joke('en')
                say(joke)
                time.sleep(0.2)
                say('HeHeHeHeHe')
        elif 'weather' in command:
            say('Where?')
            location = input('where? ')
            location = location.replace(' ','+')
            response = requests.get("https://api.openweathermap.org/data/2.5/weather?appid=2e00ef8ae954518a83ffeb22b393672c&q={}".format(location.lower()))
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_temperature = convertKtoF(current_temperature)
                tempMax = y["temp_max"]
                tempMax = convertKtoF(tempMax)
                tempMin = y["temp_min"]
                tempMin = convertKtoF(tempMin)
                z = x["weather"]
                weather_description = z[0]["description"]
               
                say('It is about '+current_temperature+' degrees Fahrenheit with a maximum of '+tempMax+' degrees and a minimum of '+tempMin+' degrees, with '+weather_description)
                time.sleep(0.2)
                say('Oof! That took a lot of breath.')
            else:
                say(" City Not Found ")
        elif 'play' in command:
            video = command[5:]
            pywhatkit.playonyt(video)
        elif command=='how are you?' or command=='how are you' or 'how are you feeling'in command or 'how are you doing' in command or 'how are you now' in command or 'who created you' in command or 'how were you created' in command or 'who is your creator' in command or 'who is your inventor' in command or 'who invented you' in command or 'alexa' in command or 'ok google' in command or 'hey google' in command or 'google assistant' in command or 'cortana' in command or 'bixby' in command or 'what should i do' in command or 'i am bored' in command or "i'm bored" in command or 'tell me what to do' in command or 'rap' in command or 'that was good' in command or 'good job' in command or 'that was bad' in command:
            chat(ai_name, command)
        else:
            say("I didn't quite get that. Would you like to repeat that?",False)
            Repeat = input("I didn't quite get that. Would you like to repeat that(y/n)? ")
            if Repeat.lower()=='y':
                pass
            else:
                exit()