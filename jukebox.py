import tkinter
##import tkMessageBox
import speech_recognition as sr
import random
import os
from playsound import playsound


top = tkinter.Tk()

music_types=["pop","rock","edm"]
stop=0

def quitCallBack():
##   tkMessageBox.showinfo( "Hello Python", "Hello World")
    print("QUIT")
    quit()

def vol_upCallBack():
    print("Volume UP")

def vol_downCallBack():
    print("Volume DOWN")

def startCallBack():
    print("Start")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        recog_word = r.recognize_google(audio)
        print(recog_word)
        
        if recog_word in music_types:
            print("Found")
            while(1):
                rndmp3 ()
                if stop==1:
                    break
        
def stopCallBack():
    print("Stop")
    stop=1        
        
def rndmp3 ():
    randomfile = random.choice(os.listdir("C:\\Users\\hp1\\Downloads\\New Music\\"))
    print(randomfile)
    file = "C:\\Users\\hp1\\Downloads\\New Music\\" + randomfile
    playsound(file)

start = tkinter.Button(top, text ="Start", command = startCallBack)

stop = tkinter.Button(top, text ="Stop", command=stopCallBack)

quits = tkinter.Button(top, text ="Quit", command = quitCallBack)

vol_up = tkinter.Button(top, text ="Volume up", command = vol_upCallBack)

vol_down = tkinter.Button(top, text ="Volume down", command = vol_downCallBack)

start.pack()
stop.pack()
quits.pack()
vol_up.pack()
vol_down.pack()

top.mainloop()
