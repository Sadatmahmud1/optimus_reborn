import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import calendar
import os
import time, smtplib
import random, requests
import pyautogui
from PIL import ImageGrab

# from tkinter import*
# def guio():


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


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


# intro = str("How can I help you.")
intro = str(" I am Optimus 2.0, I am a programmable artificial intiligence.  \n"
            #  "Devloped by sadat. under the project of O-ONAI. I wanna give thanks to sadat for devlop me.\n"
            #  "Currently now I am  a beta virsion of the acctual program. but I can do manything like conversation with you,\n"
            #  " search informations in web, and send emails.\n "
            # "I have also some capability like apps controll, I can also play music for you.\n"
            #  "I Think you should have a try...\n"
            # "Pleas tell me how may I help you..."
            )


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
        speek('I could not catch your voice')
        return "None"
    return query


rcbscians = (
    'Sir,NOW I am wishing your all off special frieds. Happy EID UL AJHA Rahul, lemon, Monir, Fysal, Musfiq, Hasan,'
    ' Mobassir,Shoron, Mobassir,Ryan, Fahim, Israq, pavel, Torsa, Neha, Najnin, Nafisa.'
    ' Sir, acctually I noticed that among all of your friends, hasan is very cute like a girl')
G_p = 'sss galaxy mail 02'
hello_word = ['hi how are you', 'hello every one', 'whats up guise']
ps_hellow_word = random.choice(hello_word)
cmplw = ['yes I think so', 'Maybe but I have some dought', 'I have some dought']
compliment1 = random.choice(cmplw)

optimus_complimenting_word = ['Thanks for your compliment, sir', 'you know how smart am I sir,',
                              'Not a big dill sir Its your coding magic']
compliment2 = random.choice(optimus_complimenting_word)


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sadatmahmud02@gmail.com', G_p)
    server.sendmail('sadatmahmud02@gmail.com', to, content)
    server.close()


dicten = {
    'mahmud': 'sadatmahmud.bd@gmail.com',
    'rahul': 'Rahulislam.ng@gmail.com',
    #     'rahul': 'rahulislam.bd@gmail.com',
    #     'rahul': 'rahulislam.bd@gmail.com',
    #     'rahul': 'rahulislam.bd@gmail.com',
    #     'rahul': 'rahulislam.bd@gmail.com',
}

if __name__ == '__main__':
    wishme()
    print(intro)
    speek(intro)
    while True:
        query = takecommand().lower()
        if "what's the date" in query or "what is the date" in query:
            date_data()
            print(date_data())
            speek(date_data())
            continue


        #     ansd = calendar.weekday(year, month, day)
        #
        #     print(calendar.day_name.str[ansd])
        #     speek(ansd)
        # elif "what's the current day " in query or "what is the current day" in query:
        #     month, day, year = 7, 14, 2020

        elif "what's the time" in query or "what is the time" in query:

            t = time.localtime()
            current_hour: int = time.strftime("%H")

            if int(current_hour) > 12:
                current_hour = int(current_hour) - 12
            current_time: str = time.strftime("%M O'Clock %p", t)
            ctime = current_hour, current_time

            print(current_hour, current_time)
            speek(ctime)
            continue
        elif 'what is the weather today' in query:
            user_api = '724168f118d817bf1e275a112c71eaaf'
            location = 'Rajshahi'

            complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + user_api
            api_link = requests.get(complete_api_link)
            api_data = api_link.json()

            # create variables to store and display data
            temp_city = ((api_data['main']['temp']) - 273.15)
            weather_desc = api_data['weather'][0]['description']
            hmdt = api_data['main']['humidity']
            wind_spd = api_data['wind']['speed']
            # date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

            print(f"Sir todays Weather Stats in  {location} : ")
            speek(f"sir, todays Weather Stats in  {location} : ")
            print("Current temperature is : {:.2f} deg C".format(temp_city))
            speek("Current temperature is : {:.2f} deg C".format(temp_city))

            wcst = (f"Current weather desc  : {weather_desc}")
            print(wcst)
            wc = str(wcst)
            speek(wc)
            wcst1 = (f"Current Humidity      : {hmdt} %")
            print(wcst1)
            wc1 = str(wcst1)
            speek(wc1)
            wcst2 = (f"Current wind speed    : {wind_spd} kmph")
            print(wcst2)
            wc2 = str(wcst2)
            wc2 = wc2.replace('kmph', 'kelometer per hour')
            speek(wc2)
            continue

        # for quitting
        elif 'quite' in query or 'exit' in query or 'stop' in query:
            print('Your plasure sir, I am quiting .  Thank you sir for using me.')
            speek('Your plasure sir, I am quiting . Thank you sir for using me.')
            exit()
        # for hardware controll
        elif 'screenshot' in query:
            take_scr()

        elif 'volume down' in query:
            speek('volume lowing')
            volume_down()
        elif 'volume up' in query:
            speek('volume increasing')
            volume_up()
        elif 'mute' in query:
            speek('muting')
            mute()

        elif 'volume maximize' in query:
            high_volume()
            speek('maximizing volume')

        elif 'open home menu' in query:
            speek('opening home menu')
            home_menu()

        #
        # elif 'open interface' in query:
        #     root = Tk()
        #     root.geometry("633x633")
        #     frame = Frame(root, borderwidth=6, bg='gray')
        #     frame.pack(side=BOTTOM)
        #     b1 = Button(frame, bg='cyan', text='command', command=takecommand)
        #     b1.pack(side=BOTTOM)
        #     root.mainloop()

        # serching tecnique:
        elif 'search' in query:
            os.startfile('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
            time.sleep(15)
            query = query.replace("search", "")
            pyautogui.write(f"{query}", interval=0.25)
            pyautogui.press('enter')
            time.sleep(4)
            speek(f'Here is what I found for {query} on google')
        # opening website

        elif 'open google' in query:
            os.startfile('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')

            time.sleep(8)
            speek("opening google")

            pyautogui.write('https://www.google.com/')
            pyautogui.press('enter')

        elif 'python web' in query:
            os.startfile('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')

            time.sleep(8)
            speek("opening pypi org")

            pyautogui.write('https://www.pypi.org/')
            pyautogui.press('enter')

        # opening application

        elif 'open code' in query or 'open vs code' in query:
            os.startfile("C:\\Program Files\\Microsoft VS Code\\Code.exe")
            speek("opening vscode")


        elif 'open youtube' in query:

            os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

            time.sleep(8)
            speek("opening youtub")

            pyautogui.write('https://www.youtube.com/')
            pyautogui.press('enter')

        elif 'open facebook' in query:

            os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
            time.sleep(8)
            speek("opening facebook")

            pyautogui.write('https://web.facebook.com/?_rdc=1&_rdr')

            pyautogui.press('enter')

        elif 'stack overflow' in query:

            os.startfile('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
            time.sleep(8)
            speek("opening stack-overflow")

            pyautogui.write('https://www.stackoverflow.com/?_rdc=1&_rdr')

            pyautogui.press('enter')


        # playing music

        elif 'play music' in query or 'play song' in query:
            music_dr = "G:\\SD SONGS\\songs"
            songs = os.listdir(music_dr)
            os.startfile(os.path.join(music_dr, random.choice(songs)))
            exit()
            # Our country perpus
        elif 'our country' in query or 'what is my country' in query:
            print('sir, your country is bangladesh.')
            speek('sir, your country is bangladesh.')
            continue

        elif 'what is my city' in query:
            print('sir, your city is Naogaon.')
            speek('sir, your city is nao-gaon.')
            continue

        elif 'my hometown' in query:
            print('sir, your Home town is Naogaon.')
            speek('sir, your Home town is nao-gaon.')
            continue
        # convercetion
        # commands for optimus
        elif 'how are you' in query:
            print("I am fine. whats yours sir, you should stay home,its quraintain time")
            speek("I am fine. whats yours sir, you should stay home,its quraintain time")

        elif 'who i am' in query:
            print("You are my devloper")
            speek("You are my devloper")

        elif 'wish my friends' in query:
            print("Hellow everyone, I am optimus. I am the personal\n "
                  "assistent of sir. The Eid festivals is comes  again\n"
                  " so that sir wishing  all of you. Happy Eid ul Ajha, festival.\n "
                  'Sir, NOW I am wishing your all off special friends,\n Happy Eid ul Ajha, to, Rahul, lemon, Monir, Fysal, Musfiq, Hasan,\n'
                  ' Mobassir,Shoron, Mobassir,Ryan, Fahim, Israq, pavel,\n Torsa, Neha, Najnin and Nafisa.'
                  ' Sir, acctually\n I noticed that among all of your friends, hasan is very cute like a girl')

            speek("Hellow everyone, I am optimus. I am the personal "
                  "assistent of sir. The Eid festivals is comes  again"
                  " so that sir wishing  all of you. Happy Eid ul Ajha, festival. "
                  'Sir, NOW I am wishing your all off special friends, Happy Eid ul Ajha, to, Rahul, lemon, Monir, Fysal, Musfiq, Hasan,'
                  ' Mobassir,Shoron, Mobassir,Ryan, Fahim, Israq, pavel, Torsa, Neha, Najnin and Nafisa.'
                  ' Sir, acctually I noticed that among all of your friends, hasan is very cute like a girl')
            time.sleep(1)
            print('Thanks everyone stay safe stay home bye.')
            speek('Thanks everyone stay safe stay home bye.')

            time.sleep(2)
            speek('sir, anything else to do')
        elif 'nothing' in query:
            print('ok sir I am quiting')
            speek('ok sir I am quiting')
            quit()


        elif 'what is my name' in query:
            print('Sir, You are Mr. Sadat Mahmud.')
            speek('sir, you are Mr. sadat mahmud')

        elif 'hello' in query:
            print(ps_hellow_word)
            speek(ps_hellow_word)

        elif 'what is your name' in query:
            print("I am optimus 2.0")
            speek("I am optimus 2.0")
            continue
        elif 'good' in query:
            print("thanks sir ")
            speek("thanks sir ")

        elif 'can you hear me' in query:
            print("Optimus is in your service sir.")
            speek("Optimus is in your service sir.")

        elif 'optimus' in query:
            print("good morning and happy new year 20 21 sir. pleas command me")
            speek("good morning and happy new year 20 21 sir. pleas command me")
        elif 'whare is may last line of code ' in query:
            print("sir,your last line of code is line")
            speek("sir,your last line of code is line")
        elif 'who are you' in query:
            print("sir,I am optimus your personal assistant")
            speek("sir,I am optimus your personal assistant")
        elif 'who are you' in query:
            print("sir,I am optimus your personal assistant")
            speek("sir,I am optimus your personal assistant")
        elif "what's your age" in query:
            print("I have naver born so that I have no age,sir")
            speek("I have naver born so that I have no age,sir")
        elif 'what are you doing' in query:
            print("I am just wait for your command sir, I just only heare to help you,sir")
            speek("I am just wait for your command sir, I just only heare to help you,sir")

        elif 'you are great' in query or 'you are good' in query or 'smart' in query:
            print(compliment2)
            speek(compliment2)

        elif 'do you love me' in query or 'do you respect me' in query:
            print(
                'sir, I have no heart, but if I would, I will have some fellings for you sir. I thik it should be the love, but More than love,'
                ' I wants to you give respect sir')
            speek(
                'sir, I have no heart, but if I would, I will have some fellings for you sir. I thik it should be the love, but More than love,'
                ' I wants to you give respect sir')
            speek('sir, do love any one')
            asking = takecommand().lower()
            while 'what do you think' in asking:
                print('I think sir you are')
                speek('I think sir you are')
                asking = takecommand().lower()
                if 'wow' in asking:
                    print('I dont know sir, but my algorithm saying it is tru')
                    speek('I dont know sir, but my algorithm saying it is tru')
                    print('who is she sir')
                    speek('who is she sir')
                    asking = takecommand().lower()
                    if "i can't tell you " in asking:
                        print('I am not a human but, I can understand sir, love is really heart braking')
                        speek('I am not a human but, I can understand sir, love is really heart braking')

        elif 'do you have any girlfriend' in query:
            print("sorry sir but  I am not a human, only human have any girl friend, I hope you understand.")
            speek("sorry sir but  I am not a human, only human have any girl friend, I hope you understand.")
        elif 'how old are you' in query:
            print(
                "actually I dont know. master sadat knows that. master had been  so long on me. but I can tell you, I am younger like master.")
            speek(
                "actually I dont know. master sadat knows that. master had been workin  so long on me. but I can tell you, I am younger like master.")



        # conveicetion commands humans:

        # convercetion with friends:

        elif ' rahul' in query:
            print("I think he is a nice person,and your good friend also.")
            speek("I think he is a nice person,and your good friend also")

        elif 'my friends' in query:
            print(rcbscians)
            speek(rcbscians)

        elif 'lemon' in query:
            print("I think he is a good person,and he loves food . and I Think he needs a girl friend ")
            speek("I think he is a good person,and he loves food . and I Think he needs a girl friend")

        elif 'mubashshir' in query:
            print("shoron or mobashssir soron is your friend in rcbsc. I think he is a good person,and he loves food ."
                  " and I Think he will never find any  girl friend because he is too much fat ")
            speek(
                "shoron, or mobashssir soron. is your friend, in rcbsc. I think he is a good person. and he loves food."
                " and I Think he will never find any  girl friend because he is too much fat")

        elif 'hassan' in query:

            print("I think he is a good person,more than handsome he is very cute. and I Think he needs a girl friend ")
            speek("I think he is a good person,,more than handsome he is very cute. and I Think he needs a girl friend")

        elif 'nazneen' in query or 'najnin' in query or 'naznin' in query:
            print("I think she is a very cute girl,and your good friend also. and you called her sister")
            speek("I think she is a very cute girl,and your good friend also. and you called her sister")

        elif 'anika' in query:
            print("I think she is very pritty,and   your good friend also, and I know that you call her sister")
            speek("I think she is very pritty,and your good friend also, and I know that you call her sister")

        elif 'do you think he is good' in query or 'do you think she is good' in query:
            print(compliment1)
            speek(compliment1)


        elif 'who is ghulam mustafa' in query:
            print("GM sir or, Golam mostofa sir is your honorable teacher, in rcbsc. at the department of ICT")
            speek("GM sir or, Golam mostofa sir is your honorable teacher, in rcbsc. at the department of ICT")
            continue
        # Email function

        elif 'send email' in query:
            try:
                print('sir,pleas tell me where to send')
                speek('sir,pleas tell me where to send')
                to = takecommand().lower()
                to = dicten[to]
                print('sir, pleas tell me what should I say')
                speek('sir, pleas tell me what should I say')
                content = takecommand()
                sendemail(to, content)
                print('Email has been send')
                speek('Email has been send')
            except Exception as e:
                print(e)
                speek('sorry sir I could not send the email.')

        # wikipedia searching algorithm:
        while 'tell me about' in query or 'who is' in query or 'what is' in query:
            speek('searching wikipedia')
            query = query.replace("tell me about", "")
            query = query.replace("who is", "")
            query = query.replace("what is", "")
            results = wikipedia.summary(query, sentences=2)
            try:
                speek("According to wikipedia")
                print(results)
                speek(results)
            except:
                print('Nothing is matched, according to your information')
                speek('Nothing is matched, according to your information')

v


