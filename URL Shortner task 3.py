#Importing Necessary Libraries
import pyshorteners
from tkinter import *

window=Tk()
window.title("URL Shortner")
window.config(bg="lavender")

#Defining the Main window dimensions
rw=650
rh=530
sw=window.winfo_screenwidth()
sh=window.winfo_screenheight()
wpos=(sw/2)-(rw/2)
hpos=(sh/2)-(rh/2)
window.geometry("%dx%d+%d+%d"%(rw,rh,wpos,hpos))
window.maxsize(2560,1600)
window.minsize(650,450)

def short():
    global s_url
    url = e1.get()
    short = pyshorteners.Shortener()
    s_url = short.tinyurl.short(url)
    L2.config(text=s_url)

def copy_select():
    global data 
    data=s_url.selection_get()

 #head label
h=Label(window,text="URL SHORTNER",width=0,height=0,font=("timesnewroman",25,"bold"))
h.config(bg="black",fg="white")
h.place(x=200,y=20)

#Label for Enter your URL link
l1=Label(window,text="Enter Your URl Link:",width=0,height=0,font=("timesnewroman",20,"bold"))
l1.configure(bg="white",fg="black")
l1.place(x=190,y=100)

#Entry for Url
e1=Entry(window,font=(6))
e1.configure(bg="white",fg="Black")
e1.place(x=220,y=170)

#Button for URL
b1=Button(window,text="Ok",width=10,height=0,font=("timesnewroman",17,"bold"),command=short)
b1.config(bg="red",fg="White")
b1.place(x=250,y=230)


#Label for Shortned Link
l1=Label(window,text="Shortned Link is:",width=0,height=0,font=("timesnewroman",20,"bold"))
l1.configure(bg="white",fg="black")
l1.place(x=220,y=300)

#Label for the output link
L2=Label(window,text="",width=30,height=0,font=("timesnewroman",15,"bold"))
L2.configure(bg="white",fg="Black")
L2.place(x=155,y=350)

#BVutton for Copy link
b2=Button(window,text="Copy Link",width=10,height=0,font=("timesnewroman",12,"bold"))
b2.config(bg="Green",fg="white")
b2.place(x=270,y=400)

window.mainloop()
