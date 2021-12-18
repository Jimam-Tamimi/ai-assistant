from helpers.listener import takeCommand
from helpers.speaker import speak
from helpers.matchQuery import matchQuery
import os
from tkinter import filedialog

from tkinter import *
NAME = "us"


if __name__ == '__main__':





    
    
    
    pause = False
    while True:
        query = takeCommand()
        # query = input()
        print(query)
        if(query == None):
            continue


        
        if(pause!=True and type(query) == list and query[0] == False):
            speak(query[1])
            
            
        
            
        if(matchQuery(query, ["pause", "stop", "ok stop"])):
            speak(['Ok', 'Ok, sir', 'yes sir', "sure sir", "ok master", "ok master"])
            pause = True
            continue
              
             
        elif(matchQuery(query, [f"{NAME}", f"{NAME} up", "are you there"])):
            speak(['Yes', 'Yes, I am here', 'yes sir', 'yes master', 'yes master, I am here', 'yes master, I am here, what can I do for you', '' ]) 
            pause = False
            
        
             
        elif(matchQuery(query, ["open folder visual studio code", f"i want to open a folder in vs code", f"please open a file in vs code", "open a folder in vs code", "open a folder in visual studio code"])):
            print('in')
            folder_selected  = filedialog.askdirectory()
            os.system(f"code -r {folder_selected }")
            speak(['Yes', 'Yes, I am here', 'yes sir', 'yes master', 'yes master, I am here', 'yes master, I am here, what can I do for you', '' ]) 
            
        



        
        
        if(query == "exit"):
            break