import socket
from tkinter import *
from threading import Thread
import random
from PIL import ImageTk, Image

def setup():
    global SERVER
    global IP_ADDRESS
    global PORT 

    PORT = 5000
    IP_ADDRESS = "127.0.0.1"
    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    SERVER.connect((IP_ADDRESS,PORT))

    thread = Thread(target=recivedMsg)
    thread.start()
    askPlayerName()

def askPlayerName():
    global playerName
    global nameEntry
    global nameWindow
    global canvas1
    
    nameWindow = Tk()
    nameWindow.title("tumbola game!")
    nameWindow.geometry("500x500")

    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file = "C:/Users/iliea/OneDrive/Desktop/Code/Python/Hw\Hw204/assets/background.png")

    canvas1 = Canvas(nameWindow,width = 500,height = 500)
    canvas1.create_image(0,0,bg=bg,anchor = "nw")

    canvas1.create_text(screen_width/4.5,screen_height/8,text="Enter your name!")
    
    nameEntry = Entry(nameWindow,width=5,justify="center")
    nameEntry.place(screen_width/7,screen_height/5.5)

    saveButton = Button(nameWindow,text="save",width=10,height=10,command=saveName())
    saveButton.place(x=screen_width/6,y=screen_height/4)

    nameWindow.resizable(True,True)
    nameWindow.mainloop()

def saveName():
    global nameEntry
    global SERVER
    global nameWindow
    global playerName

    playerName = nameEntry.get()
    nameEntry.delete(0,END)
    nameWindow.destroy()

    SERVER.send(playerName.encode())
setup()


    