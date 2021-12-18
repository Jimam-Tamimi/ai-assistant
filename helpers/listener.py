import speech_recognition as sr
from .speaker import speak      
        
        
r = sr.Recognizer()
    
def takeCommand():
    with sr.Microphone() as source:
        r.energy_threshold = 25000
        audio = r.listen(source)
    try: 
        query = r.recognize_google(audio)
        print("user said: " + query)
        return query.lower()
    except sr.WaitTimeoutError as e:
        return None
    except sr.UnknownValueError:
        return [False, "Sorry, I didn't get that"]
    except sr.RequestError as e:
        return [False, "Sorry, I am having some problem processing your request"]
    except Exception as e:
        return None