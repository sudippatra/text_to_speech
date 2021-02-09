from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
import pyttsx3
 
# root window
root = Tk()
 
root.resizable(0,0)
root.configure(background="white")
root.title("Text To Speak")
# functions
def speak():
    engine = pyttsx3.init()
    audio_string = text.get('0.0',END)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio_string)
    engine.runAndWait()
    engine.stop()
 
 
def save_audio():
    engine = pyttsx3.init()
    audio_string = text.get('0.0',END)
    engine.save_to_file(audio_string,'test.mp3')
    engine.runAndWait()
    engine.stop()
    showinfo("python says","audio is saved as text.mp3")
 
# root widgets
text = scrolledtext.ScrolledText(root,width=30,height=10,wrap=WORD,padx=10,pady=10,borderwidth=5,relief=RIDGE)
text.grid(row=0,columnspan=3)
#buttons
ttk.Button(root,text="Listen",width=7,command=speak).grid(row=2,column=0,ipadx=2)
ttk.Button(root,text="Clear",width=7,command=lambda:text.delete('0.0',END)).grid(row=2,column=1,ipadx=2)
ttk.Button(root,text="Save",width=7,command=save_audio).grid(row=2,column=2,ipadx=2)
 
root.mainloop()