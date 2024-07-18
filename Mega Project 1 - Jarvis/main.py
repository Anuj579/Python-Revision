# import speech_recognition as sr
# import webbrowser
# import pyttsx3
# import musicLibrary
# import requests

# recognizer = sr.Recognizer()
# engine = pyttsx3.init()
# newsapi = "850b9c7654cb46fa928274adccb0e7d8"

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def processCommand(c):
#     if "open google" in c.lower():
#             webbrowser.open("https://google.com")
#     elif "open facebook" in c.lower():
#             webbrowser.open("https://facebook.com")
#     elif "open youtube" in c.lower():
#             webbrowser.open("https://youtube.com")
#     elif "open linkedin" in c.lower():
#             webbrowser.open("https://linkedin.com")
#     elif c.lower().startswith("play"):
#          song = c.lower().split(" ")[1]
#          link = musicLibrary.music[song]
#          webbrowser.open(link)
#     elif "news" in c.lower(): 
#          r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
#          if r.status_code == 200:
#               # Parse the JSON response
#               data = r.json()

#               # Extract the articles
#               articles = data.get('articles',[])

#               # Speak the headlines
#               for article in articles:
#                    speak(article['title'])
#     else:
#          # Let OpenAI handle the request
#          pass

# if __name__ == '__main__':
#     speak("Initializing Jarvis...")
#     while True:
#         # Wait for the wake word "Jarvis"
#         # obtain audio from the microphone
#         r = sr.Recognizer()
        
#         print("recognizing...")
#         try:
#             with sr.Microphone() as source:
#                 print("Listening...")
#                 audio = r.listen(source, timeout=4, phrase_time_limit=1)
#             word = r.recognize_google(audio)
#             if (word.lower() == 'jarvis'):
#                 speak('Yeah')
#                 #Listen for command 
#                 with sr.Microphone() as source:
#                     print("Jarvis Active...")
#                     audio = r.listen(source)
#                     command = r.recognize_google(audio)

#                     processCommand(command)

#         except Exception as e:
#             print("Error; {0}".format(e))