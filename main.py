from helpers.listener import takeCommand
from helpers.speaker import speak
from helpers.matchQuery import matchQuery
import os
from tkinter import filedialog

from tkinter import *
# NAME = "us"
NAME = "ruckyia"


if __name__ == '__main__':


    # speak("hello sir")



    
    
    
    pause = False
    while True:
        query = takeCommand()


        # query = input()
        print(query) 
        
        if(pause!=True and type(query) == list and query[0] == False):
            speak(query[1])
            
            
        
            
        if(matchQuery(query, ["pause", "stop", "ok stop"])):
            speak(['Ok', 'Ok, sir', 'yes sir', "sure sir", "ok master", "ok master"])
            pause = True
              
             
        elif(matchQuery(query, [f"{NAME}", f"{NAME} up", "are you there"])):
            speak(['Yes', 'Yes, I am here', 'yes sir', 'yes master', 'yes master, I am here', 'yes master, I am here, what can I do for you', '' ]) 
            pause = False
            
        
             
        elif(matchQuery(query, ["open folder visual studio code", f"i want to open a folder in vs code", f"please open a file in vs code", "open a folder in vs code", "open a folder in visual studio code"])):
            speak(['Yes', 'Ok sir', 'yes sir', 'yes master', 'yes master, doing' ]) 
            root = Tk()
            folder_selected  = filedialog.askdirectory()
            root.withdraw()
            print(folder_selected)
            os.system(f"code -n {folder_selected }")
            
        
        



        
        
        if(query == "exit"):
            break