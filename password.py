from tkinter import *
from tkinter.ttk import *
import random
import win32clipboard
def generator():
    entry.delete(0,END)
    l=int(entry1.get())
    digits=["1","2","3","4","5","6","7","8","9","0"]
    lower=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
           "p","q","r","s","t","u","v","w","x","y","z"]
    upper=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O",
           "P","Q","R","S","T","U","V","W","X","Y","Z"]
    symbols=["!","@","#","$","%","^","&","*"]
    p=""
    p1=""
    v=val.get()
    if(v==0):
        for _ in range(l//2):
            p+=random.choice(lower)
            p+=random.choice(symbols)
        if(l%2!=0):
            p+=random.choice(lower)
    else:
        for _ in range(l//4):
            p+=random.choice(lower)
            p+=random.choice(symbols)
            p+=random.choice(digits)
            p+=random.choice(upper)
        for _ in range(l%4):
            p+=random.choice(digits)
    l1=list(p)
    random.shuffle(l1)
    p1=''.join(l1)
    return p1
def copy1():
    pp=entry.get()
    win32clipboard.OpenClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT,pp)
    win32clipboard.CloseClipboard()
def generate():
    pw=generator()
    entry.insert(0,pw)
root=Tk()
root.configure(bg="black")
val= IntVar()
root.title("Random Password Generator")
random_password=Label(root,text="password")
random_password.grid(row=0,column=0)
entry=Entry(root)
entry.grid(row=0,column=1)
label1=Label(root,text="Length")
label1.grid(row=1,pady=10)
entry1=Spinbox(root,from_=8,to=32)
entry1.grid(row=1,column=1,pady=10)
r1=Radiobutton(root,text="Medium",variable=val,value=0)
r1.grid(row=1,column=2)
r2=Radiobutton(root,text="Strong",variable=val,value=1)
r2.grid(row=1,column=3,pady=10)
c1=Button(root,text="Copy",command=copy1)
c1.grid(row=0,column=2,pady=10)
g1=Button(root,text="Generate",command=generate)
g1.grid(row=0,column=3)
root.mainloop()
