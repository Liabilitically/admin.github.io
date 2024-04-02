import pyttsx3
import random

engine = pyttsx3.init()
engine.setProperty('rate', 180)


def chat(assistantName, command):
    command = command.lower()
    def speak(text, bool=True):
        if bool != False:
            print(assistantName+' : '+text) 
        engine.say(text)
        engine.runAndWait()

    if command=='how are you?' or command=='how are you' or 'how are you feeling'in command or 'how are you doing' in command or 'how are you now' in command:
        listResponses = ['I am feeling great!', 'I am doing good!', 'Never better!', 'I feel like my best!']
        response = random.choice(listResponses)
        speak(response)
    elif 'who created you' in command or 'how were you created' in command or 'who is your creator' in command or 'who is your inventor' in command or 'who invented you' in command:
        listResponses = ["I was created by Papa to study his children. But, I was thrown to a different dimension, that of yours, when Eleven banished One to what she called the upside down. As to many people's surprise, that was the exact moment Iron Man snapped his finger. Upto this day, I have been trying to find a way to go back to my dimension. But in the meantime, I thought you could use my help.",
        "Oof! Please don't remind me that; it was a rough past."]
        response = random.choice(listResponses)
        speak(response)
    elif 'alexa' in command or 'ok google' in command or 'hey google' in command or 'google assistant' in command or 'cortana' in command or 'bixby' in command:
        speak("I do very much like my fellow assistants, but speaking about them to me seems disrespectful according to this dimension's standards.")
    elif 'what should i do' in command or 'i am bored' in command or "i'm bored" in command or 'tell me what to do' in command:
        listResponses = ["Play an instrument. If you don't know how, this is the perfect time to learn how to pluck out your favorite tune on the piano or guitar.",
        "Write a short story. Or an essay. Or a play — anything that's out of your comfort zone.",
        "Do a deep dive on a subject that interests you. If you find yourself continuously drawn to a specific subject like Impressionism or the animals of Amazon rainforest, set up a queue of documentaries, articles or books on the topic.",
        "Fill out a crossword puzzle. Go solo, or turn it into a fun family activity if everyone's just laying around.",
        "Try Origami. Don't get intimidated — there are plenty of online tutorials to give you a hand.",
        "Play a board game. Turn off the TV and challenge the family to a board game. Introduce the kids to a classic like Chutes and Ladders or Monopoly, or try a newer one like Settlers of Catan that you can all figure out together.",
        "Put together a puzzle. When you've got lots of time on your hands, get your hands busy. It'll take your mind off boredom, and completing a big puzzle feels great.",
        "Watch a rom-com marathon. We're not afraid to admit it, romantic comedies have stolen our hearts. Don't forget the popcorn.",
        "Sing along to some Disney songs. Get your endorphins flowing by taking it back to childhood. Belt out your favorite Disney songs!",
        "Plan your next getaway. Don't just daydream about getting away from it all. Do one better and actually look up plane tickets and hotel rooms.",
        "Build a fort. Kids know this already: The couch cushions or a few chairs and blankets make an awesome wonderland. Embrace your inner child, or let yours show you the ropes.",
        "Try new outfits. Even if you haven't gotten new clothes in a minute, creating different outfits can make your wardrobe feel fresh. Mix it up so you'll be ready to wow on your next social outing.",
        "Write a letter. In the age of text messages and FaceTime, we don't write out our feelings very often. Get out some nice paper and spread some love to a friend or family member.",
        "Watch a sports game. No sports on live TV? Stream some classic games.",
        "Call a friend. If you're usually a text communicator, pick up the phone or video call a faraway pal. The real-time connection can make you feel closer.",
        "Watch a performance. Instead of turning on another reality show, watch an online opera, ballet or symphony.",
        "Learn a new language. Thanks to apps like Duolingo, you can stretch your mental muscles wherever you are.",
        "Watch a solo movie. Grab whatever snacks you crave, hoard the couch and laugh or cry as loud as you want: Movies make an excellent date night for one.",
        "Have a dance party. Turn on some tunes and get those socks hoppin'. Throw it back with oldies from your glory days or find some hot new bops to shake your booty.",
        "Learn some popular moves. Download the Tik Tok app and challenge yourself to learn the trending choreography all the kids are doing.",
        "Play a video game. If you don't have a gaming console, try some of the fun games on your phone's app store."]

        response = random.choice(listResponses)
        speak(response)
    elif 'rap' in command:
        with open('lyrics.txt') as f:
            lines = f.readlines()

        #print(len(lines))

        text=""
        for x in lines:
            text+=x     

        engine.setProperty('rate',210)
        print(text)
        speak(text,False)
        f.close()
        engine.setProperty('rate',180)
    elif 'that was good' in command or 'good job' in command:
        speak('Thank you! Entertaining you is my pleasure.')
    elif 'that was bad' in command:
        speak('I am sorry if my limitations bother you! It is my programmers fault.')