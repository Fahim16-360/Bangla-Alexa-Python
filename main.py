import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import webbrowser
import requests, json

r = sr.Recognizer() # initialise a recogniser
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)

def talk(text):
    alexa.say(text)
    alexa.runAndWait()

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

# listen for audio and convert it to text:
def take_command():
    with sr.Microphone() as source: # microphone as source
        print('listening...')
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            # voice_data = r.recognize_google(audio, language ='bn-BD')  # convert audio to text
            voice_data = r.recognize_google(audio, language ='en-IN')  # convert audio to text
            # voice_data = voice_data.lower()
            print("You : ", voice_data)
        except sr.UnknownValueError: # error: recognizer does not understand
            pass
            # webbrowser.open('dukhito_bujhte_parchi_na.mp3', True)
        except sr.RequestError:
            pass
        return voice_data

def respond(voice_data):
    if there_exists(["Naam","Name"]):
        webbrowser.open('naam_alexa.mp3', True)
    if 'hello' in str(voice_data):
        webbrowser.open('ji_hello.mp3', True)
    if there_exists(["time","samay","shomoy","koyta"]):
        # time = datetime.datetime.now().strftime('%I:%M %p')
        # print(time)
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk(time)
    if 'gaan' in str(voice_data):
        song = voice_data.replace('gaan', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    if 'search' in str(voice_data):
        search_term = voice_data.split("search", "")
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        webbrowser.open('google_results.mp3', True)
    if 'weather' in str(voice_data):
        # base URL
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        CITY = "dhaka"
        API_KEY = "e00c2d23c1ffc3a62346935366b9109a"
        # upadting the URL
        URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
        # HTTP request
        response = requests.get(URL)
        # checking the status code of the request
        if response.status_code == 200:
            # getting data in the json format
            data = response.json()
            # getting the main dict block
            main = data['main']
            # getting temperature
            temperature = main['temp']
            # getting the humidity
            humidity = main['humidity']
            # getting the pressure
            pressure = main['pressure']
            # weather report
            report = data['weather']
            print(f"{CITY:-^30}")
            print(f"Temperature: {temperature}")
            print(f"Humidity: {humidity}")
            print(f"Pressure: {pressure}")
            print(f"Weather Report: {report[0]['description']}")
        else:
            # showing the error message
            print("Error in the HTTP request")
        talk(f"current temperature in{CITY:-^30} is {temperature}")
    
    if 'coding' in str(voice_data):
        webbrowser.open('coding_koreche.mp3', True)
    if 'thank you' in str(voice_data):
        webbrowser.open('welcome.mp3', True)
    if there_exists(["Bondho","Bandhu","Bandh","Bondhu"]):
        exit()

while True:
    voice_data = take_command() # get the voice input
    respond(voice_data) # respond




