from tkinter import*
from tkinter.ttk import Combobox
import random

screen = Tk()
screen.title('Password Generator App')
screen.geometry('600x400')
screen.configure(background='maroon')

def gen():
    global sc1
    sc1.set("")
    passw=" "
    length=int(c1.get())
    lowercase='abcdefghijklmnopqrstuvwxyz'
    uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'+lowercase
    mixs='0123456789'+lowercase+uppercase+'@#$&*'

    if c2.get()=='Lower':
        for i in range(0,length):
            passw=passw+random.choice(lowercase)
        sc1.set(passw)

    elif c2.get()=='Lower & Upper':
        for i in range(0,length):
            passw=passw+random.choice(uppercase)
        sc1.set(passw)

    elif c2.get()=='Lower&Upper&symbol':
        for i in range(0,length):
            passw=passw+random.choice(mixs)
        sc1.set(passw)   
    

sc1=StringVar("")
t1=Label(screen,text='',font=('Arial,28'),fg='blue',bg='maroon')
t1.place(x=60,y=0)
t2=Label(screen,text='password :',font=('Arial',14))
t2.place(x=145,y=90)

i1=Entry(screen,font=('Arial',14),textvariable=sc1)
i1.place(x=255,y=90)
t3=Label(screen,text='length :',font=('Arial',14))
t3.place(x=145,y=120)

t4=Label(screen,text='strength :',font=('Arial',14))
t4.place(x=145,y=155)

c1=Entry(screen,font=('Arial',14),width=10)
c1.place(x=230,y=120)

c2=Combobox(screen,font=('Arial',14),width=15)
c2['values']=('Lower','Lower & Upper','Lower&Upper&symbol')
c2.current(1)
c2.place(x=237,y=155)

b=Button(screen,text='Generate Password',font=('Arial,14'),fg='blue',bg='white',command=gen)
b.place(x=230,y=195)

screen.mainloop()
