import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import array
import calendar
import os
import time
import random
# import random
import pyautogui
from PIL import Image, ImageGrab

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speek(audio):
    engine.say(audio)
    engine.runAndWait()


def take_scr():
    image = ImageGrab.grab()
    image.show()


def volume_up():
    pyautogui.press('volumeup')


def volume_down():
    pyautogui.press('volumedown')


def mute():
    pyautogui.press('volumemute')


def high_volume():
    pyautogui.keyDown('volumeup')


def home_menu():
    pyautogui.press('win')


def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        print("sir, Good morning.")
        speek("sir, Good morning")

    elif hour >= 12 and hour < 18:
        print("sir, Good aftternoon.")
        speek("sir, Good afternoon")

    else:
        print("sir, Good evening.")
        speek("sir, Good evening")


intro = str(" I am optimus 2.0, How can I help you.")


# intro = str(" I am Optimus 2.0, I am a programmable artificial intiligence.  \n"
#             "Devloped by sadat. under the project of O-ONAI. I wanna give thanks to sadat for devlop me.\n"
#             "Currently now I am  a beta virsion of the acctual program. but I can do manything like conversation with you,\n"
#             " search informations in web, and send emails.\n "
#            "I have also some hardware capability like apps controll, I can also play music for you.\n"
#             "I Think you should have a try...\n"
#            "Pleas tell me how may I help you...")
def date_data():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    month = now.month
    dayNum = now.day
    weekday = calendar.day_name[my_date.weekday()]
    month_names = ['January', 'February', 'March', 'April', 'May', 'Jun', 'July', 'August', 'september', 'October',
                   'November', 'december']
    ordinal_number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
                      '15', '16', '17', '18', '19', '20', '21', '22', '23th', '24', '25', '26', '27', '28', '29', '30',
                      '31']

    return 'Today is ' + weekday + ' the ' + month_names[month - 1] + ',' + ordinal_number[dayNum - 1]


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        audio = r.listen(source)

        # voice controll

        r.energy_threshold = 200
        r.dynamic_energy_adjustment_damping = 0.15
        r.dynamic_energy_ratio = 1
        r.pause_threshold = 0.5
        r.phrase_threshold = 0.7
        r.non_speaking_duration = 1

    try:
        print('Recognizing....')
        query = r.recognize_google(audio, language='en-us')
        print(f"You said:{query}\n")

    except:
        print("Say that again pleas....")
        return "None"
    return query



if __name__ == '__main__':

    wishme()
    print(intro)
    # speek(intro)
    while True:
        query = takecommand().lower()

        if 'tell me about' in query:
            speek('searching wikipedia')
            query = query.replace("tell me about", "")
            results = wikipedia.summary(query, sentences=4)
            speek("According to wikipedia")
            print(results)
            speek(results)

        if "what's the date" in query:
            date_data()
            print(date_data())
            speek(date_data())


        #     ansd = calendar.weekday(year, month, day)
        #
        #     print(calendar.day_name.str[ansd])
        #     speek(ansd)
        # elif "what's the current day " in query or "what is the current day" in query:
        #     month, day, year = 7, 14, 2020

        elif "what's the time" in query or "what is the time" in query:
            t = time.localtime()
            current_time: str = time.strftime("%H  %M %S O clock %p", t)

            print(current_time)
            speek(current_time)

        # for quitting
        elif 'quite' in query:
            print('Your plasure sir, I am quiting .  Thank you sir for using me.')
            speek('Your plasure sir, I am quiting . Thank you sir for using me.')
            exit()
        # for hardware controll
        elif 'screenshot' in query:
            take_scr()

        elif 'volume down' in query:
            volume_down()
        elif 'volume up' in query:
            volume_up()
        elif 'mute' in query:
            mute()

        elif 'volume maximize' in query:
            high_volume()

        elif 'open home menu' in query:
            home_menu()

        # serching tecnique:
        elif 'search' in query:
            os.startfile('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
            time.sleep(1)
            query = query.replace("search", "")
            pyautogui.write(f"{query}", interval=0.25)
            pyautogui.press('enter')
            time.sleep(1)
            speek(f'Here is what I found for {query} on google')
        # opening website

        elif 'open google' in query:
            os.startfile('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')

            time.sleep(2)

            pyautogui.write('https://www.google.com/')
            pyautogui.press('enter')

        elif 'python web' in query:
            os.startfile('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')

            time.sleep(2)

            pyautogui.write('https://www.pypi.org/')
            pyautogui.press('enter')

        # opening application

        elif 'open code' in query:
            os.startfile("C:\\Program Files\\Microsoft VS Code\\Code.exe")


        elif 'open youtube' in query:

            os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

            time.sleep(2)

            pyautogui.write('https://www.youtube.com/')
            pyautogui.press('enter')

        elif 'open facebook' in query:

            os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
            time.sleep(2)

            pyautogui.write('https://web.facebook.com/?_rdc=1&_rdr')

            pyautogui.press('enter')

        elif 'stackoverflow' in query:

            os.startfile('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
            time.sleep(1)

            pyautogui.write('https://www.stackoverflow.com/?_rdc=1&_rdr')

            pyautogui.press('enter')


        # playing music

        elif 'play music' in query or 'play song' in query:
            music_dr = "G:\\SD SONGS\\songs"
            songs = os.listdir(music_dr)
            os.startfile(os.path.join(music_dr.songs[0]))
            exit()

        # convercetion
        # convercetion commands for optimus
        elif 'how are you' in query:
            print("I am fine. whats yours sir, you should stay home,its quraintain time")
            speek("I am fine. whats yours sir, you should stay home,its quraintain time")

        elif 'optimus' in query:
            print("Yes sir. pleas command me")
            speek("Yes sir. pleas command me")
        elif 'who are you' in query:
            print("sir,I am optimus your personal assistant")
            speek("sir,I am optimus your personal assistant")
        elif 'whats your age' in query:
            print("I have naver born so that I have no age,sir")
            speek("I have naver born so that I have no age,sir")
        elif 'what are you doing' in query:
            print("I am just wait for your command sir, I just only heare to help you,sir")
            speek("I am just wait for your command sir, I just only heare to help you,sir")
        elif 'you are grate' in query:
            print("Thanks for your compliment, sir.")
            speek("Thanks for your compliment, sir.")
        elif 'do you have any girlfriend' in query:
            print("sorry sir but  I am not a human. only human have any girl friend. I hope you understand.")
            speek("sorry sir but  I am not a human. only human have any girl friend. I hope you understand.")
        elif 'how old are you' in query:
            print(
                "actually I dont know. master sadat knows that. master had been  so long on me. but I can tell you, I am younger like master.")
            speek(
                "actually I dont know. master sadat knows that. master had been workin  so long on me. but I can tell you, I am younger like master.")



        # conveicetion commands humans:

        # convercetion with friends:

        elif 'Aurup' in query:
            print("I think he is a nice person,and your good friend also.")
            speek("I think he is a nice person,and your good friend also")


