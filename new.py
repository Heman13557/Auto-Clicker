

import threading
import time
from tkinter import *
from tkinter import ttk, messagebox
import mouse as mouser
from pynput import mouse
from pynput.mouse import Controller as cr, Button as bt
import keyboard
import pyautogui as pg
import pyglet



pyglet.font.add_file("sfprodisplaybold.otf")
pg.FAILSAFE = False

root = Tk()
root.title("                                                       Auto Clicker")
root.geometry("605x475")
root.iconbitmap(default="icons/untitled.ico")
root.resizable(False, False)
img1 = PhotoImage(file="icons/img1.png")
img2 = PhotoImage(file="icons/img2.png")
img3 = PhotoImage(file="icons/img3.png")
img4 = PhotoImage(file="icons/img4.png")
img5 = PhotoImage(file="icons/img5.png")
img55 = PhotoImage(file="icons/img55.png")
img6 = PhotoImage(file="icons/img6.png")
img7 = PhotoImage(file="icons/img7.png")
img77 = PhotoImage(file="icons/img77.png")
img8 = PhotoImage(file="icons/img8.png")
img88 = PhotoImage(file="icons/img88.png")
img22 = PhotoImage(file="icons/img22.png")
img33 = PhotoImage(file="icons/img33.png")
imgback1 = PhotoImage(file="icons/img101.png")
imgback2 = PhotoImage(file="icons/img102.png")
imgback3 = PhotoImage(file="icons/img103.png")

root.config(background="white")




hkey = "F6"

style = ttk.Style(root)
style.theme_use("vista")
style.configure('TLabel',background="white",foreground="black",font=('SF-Pro-Display 10 bold'))
style.configure('TButton',font=('Poppins 10 bold'),foreground="#04005e")
style.configure('TRadiobutton',fg="blue",background="white",highlightcolor="black",borderwidth=0,relief=FLAT)


cou = 0

pp = 0
state = False

pg.PAUSE = 0.001

storage = []

staticstate=0
        

ll1 = Label(root,bg="grey",width=605,height=1)
ll1.place(x=0,y=0,height=1)
blob1 = PhotoImage(file="icons/blob1.png")
blob2 = PhotoImage(file="icons/blob2.png")
blob3 = PhotoImage(file="icons/blob3.png")


def start(rev=None):


    global state
    state = True
    B3 = Button(Bottom,
                image=img3,
                bg="white",activebackground="white",borderwidth=0,
                command=killswitch)
    B3.grid(row=3, column=2, padx=(175,20))
    

    B2 = Button(Bottom,
                image=img2,
                command=start,bg="white",activebackground="white",borderwidth=0,
                state=DISABLED)
    B2.grid(row=3, column=1, padx=25)

    root.update()
    

    ck1 = 0
    if (drop2.get() == "Single"):
        ck1 = 1
    else:
        ck1 = 2
    global var1
    if (var1.get() == 2):
        pg.moveTo(x1.get(), y1.get(), duration=0.05)

    if (var.get() == 2):

        while (True):

            root.update()
            if (state == False):
                global pk1m
                pk1 = threading.Thread(target=firsttime1)
                pk1.daemon = True
                pk1.start()
                
                break
            if (rooze()):
                pk1 = threading.Thread(target=firsttime1)
                pk1.daemon = True
                pk1.start()
                
                break
            pg.click(clicks=ck1,
                     button=drop1.get(),
                     interval=hr.get() * 3600 + minu.get() * 60 + secs.get() +
                     msecs.get() * 0.001)
    else:

        for i in range(int(var3.get())):
            root.update()
            if (state == False):
                pk1 = threading.Thread(target=firsttime1)
                pk1.daemon = True
                pk1.start()
                break
            if (rooze()):
                pk1 = threading.Thread(target=firsttime1)
                pk1.daemon = True
                pk1.start()
                break
            pg.click(clicks=ck1, button=drop1.get(), interval=0)

        if (i == int(var3.get()) - 1):
            remap()

def firsttime():
    print("Cool Till here")
    keyboard.wait('f6')
    print("Starting Start")
    start()

def firsttime1():
    keyboard.wait('f6')
    start()


try:
    pk = threading.Thread(target=firsttime)
    pk.daemon = True
    pk.start()
except:
    print("Failed I Guess")
    cou = cou+1



def rooze():

    if (keyboard.is_pressed("F7")):

        remap()
        global state
        state = False
        return 1
    else:
        return 0


def remap():
    B3 = Button(Bottom,
                image=img3,
                bg="white",activebackground="white",borderwidth=0,
                state=DISABLED)
    B3.grid(row=3, column=2, padx=(175,20))
    
    B2 = Button(Bottom,
                image=img2,
                bg="white",activebackground="white",borderwidth=0,
                command=start)
    B2.grid(row=3, column=1, padx=25)
    


def check_num(input="1"):
    if input.isdigit():
        if int(input) < 1000:
            return True
        else:
            return False
    elif input == "":
        input = 0
        return True
    else:
        return False


callback = root.register(check_num)

def changeico1(l=None):
    global B6
    B6.config(image=img77)

def changeico2(l=None):
    global B6
    B6.config(image=img7)

def changeico3(l=None):
    global B
    B.config(image=img88)

def changeico4(l=None):
    global B
    B.config(image=img8)


def record():
    global Win2
    Win2 = Toplevel(root, bg="white")
    Win2.iconbitmap(default=None)
    Win2.geometry("230x50")
    Win2.title("Record & Playback")
    Win2.resizable(False, False)
    set1 = ttk.Style(root)
    set1.configure("TButton",bg="#1a4d99",fg="black")
    root.withdraw()
    global B6
    B6 = Button(Win2,
                image=img7,borderwidth=0,bg="white",activebackground="white",command=startrec)
    B6.grid(row=1, column=1, padx=5, pady=5)
    B6.bind("<Enter>",changeico1)
    B6.bind("<Leave>",changeico2)
    global B
    B = Button(Win2,
    image=img8,borderwidth=0,bg="white",activebackground="white",
                command=playrec)
    B.grid(row=1, column=2, padx=5, pady=5)
    
    B.bind("<Enter>",changeico3)
    B.bind("<Leave>",changeico4)

    root.update()
    Win2.bind("<Destroy>", on_destroy)


def on_destroy(event=None):
    root.deiconify()


def new_check():
    keyboard.wait("ctrl+1")

    global pp
    pp = 1
    global Win2
    Win2.deiconify()


def on_move(x, y):
    if (pp == 1):
        return False
    json_object = {'action': 'moved', 'x': x, 'y': y, '_time': time.time()}

    storage.append(json_object)


#Behaviour on Click Function
def on_click(x, y, button, pressed):
    if (pp == 1):
        return False
    try:
        json_object = {
            'action': 'pressed' if pressed else 'released',
            'button': str(button),
            'x': x,
            'y': y,
            '_time': time.time()
        }

        storage.append(json_object)
    except:
        messagebox.showerror("Error Occublack","Unknown Error")


#Behaviour on scroll Function
def on_scroll(x, y, dx, dy):
    if (pp == 1):
        global Win2
        Win2.deiconify()
        return False
    json_object = {
        'action': 'scroll',
        'vertical_direction': int(dy),
        'horizontal_direction': int(dx),
        'x': x,
        'y': y,
        '_time': time.time()
    }
    storage.append(json_object)


#Start Recording Button Function
def startrec():
    storage.clear()
    global pp
    pp = 0

    Win2.withdraw()
    messagebox.showinfo("Information", "Press CTRL+1 to stop Recording")
    kk = threading.Thread(target=new_check)

    kk.start()
    try:
        mouse_listener = mouse.Listener(on_click=on_click,
                                        on_scroll=on_scroll,
                                        on_move=on_move)
        mouse_listener.start()
        mouse_listener.join()
    except:
        messagebox.showerror("Error", "Looks like an loose Wire")
    finally:
        Win2.update()
    kk.join()





def playrec():
    messagebox.showinfo("Info","Press Ctrl+3 to stop Playback")
    mic = cr()

    data = storage
    for index, obj in enumerate(data):
        if (keyboard.is_pressed("ctrl+3")):
            return False
        action, _time = obj['action'], obj['_time']
        try:
            next_movement = data[index + 1]['_time']
            pause_time = next_movement - _time
        except IndexError as e:
            pause_time = 1

        if (1 == 2):
            messagebox.showerror("Error","Error Occurblack")
        else:
            move_for_scroll = True
            x, y = obj['x'], obj['y']
            if action == "scroll" and index > 0:
                if x == data[index - 1]['x'] and y == data[index - 1]['y']:
                    move_for_scroll = False

            mic.position = (x, y)
            if action == "pressed" or action == "released" or action == "scroll" and move_for_scroll == True:
                time.sleep(0.1)
            if action == "pressed":
                mic.press(bt.left if obj['button'] ==
                          "Button.left" else bt.right)
            elif action == "released":
                mic.release(bt.left if obj['button'] ==
                            "Button.left" else bt.right)
            elif action == "scroll":
                horizontal_direction, vertical_direction = obj[
                    'horizontal_direction'], obj['vertical_direction']
                mic.scroll(horizontal_direction, vertical_direction)
            time.sleep(pause_time)


def killswitch():
    
    global state
    state = False
    root.update()
    B3 = Button(Bottom,
                image=img3,
                bg="white",activebackground="white",borderwidth=0,
                state=DISABLED)
    B3.grid(row=3, column=2, padx=(175,20))
    
    B2 = Button(Bottom,
                image=img2,
                bg="white",activebackground="white",borderwidth=0,
                command=start)
    B2.grid(row=3, column=1, padx=25)
    


#Pick Location Funtion


def picklocation():
    root.iconify()
    mouser.wait()
    [x, y] = pg.position()

    x1.set(x)
    y1.set(y)
    root.deiconify()


def changeback(l=None):
    B1.config(image=img1)

def changeback1(l=None):
    B1.config(image=img6)

def changeico5(l=None):
    B5.config(image=img55)
def changeico6(l=None):
    B5.config(image=img5)

def changeico7(l=None):
    B2.config(image=img22)


def changeico8(l=None):
    B2.config(image=img2)

def changeico9(l=None):
    B3.config(image=img33)


def changeico10(l=None):
    B3.config(image=img3)
#Frames
vamp = Label(root,image=imgback1,bg="white")
vamp.place(x=8,y=40)
img1011 = PhotoImage(file="icons/img1011.png")

F1 = LabelFrame(root,
                borderwidth=0,
                padx=20,
                bg="white",
                highlightcolor="yellow",
                highlightbackground="yellow",
                font=('SF-Pro-Display-Bold 11'),
                text="Time Interval",
                fg="black")
F1.place(x=12, y=24, anchor="nw", width=580, height=80)
vamp11 = Label(root,image=img1011,bg="white")
vamp11.place(x=8,y=45)

hr = IntVar()
hr.set(0)
E1 = Entry(F1,
           width=5,font=("SF-Pro-Display-Bold 11"),
           textvariable=hr,
           validate="key",
           relief=GROOVE,
           validatecommand=(callback, "%P"))
E1.grid(row=1, column=1, padx=10, pady=20)
L1 = ttk.Label(F1, text=":Hours").grid(row=1, column=2)
minu = IntVar()
minu.set(0)
E2 = Entry(F1,
           width=5,font=("SF-Pro-Display-Bold 11"),
           textvariable=minu,
           validate="key",
           validatecommand=(callback, "%P")).grid(row=1, column=3, padx=7)
L2 = ttk.Label(F1,
           text=":Minutes").grid(row=1, column=4)
secs = IntVar()
secs.set(0)
E3 = Entry(F1,
           width=5,font=("SF-Pro-Display-Bold 11"),
           textvariable=secs,
           validate="key",
           validatecommand=(callback, "%P")).grid(row=1, column=5, padx=7)
L3 = ttk.Label(F1,
           text=':Seconds').grid(row=1, column=6)
msecs = IntVar()
msecs.set(100)
Ex = Entry(F1,
           width=5,font=("SF-Pro-Display-Bold 11"),
           textvariable=msecs,
           validate="key",
           validatecommand=(callback, "%P")).grid(row=1, column=7, padx=7)
Lx = ttk.Label(F1,
           text=':MiliSec').grid(row=1, column=8)



#Frame 2nd
#<----
vamp1 = Label(root,image=imgback2,bg="white")
vamp1.place(x=7,y=143)
F2 = LabelFrame(root,
                text="Mouse Options",
                bg="white",
                borderwidth=0,
                width=280,
                height=200,
                font=('SF-Pro-Display-Bold 11'),
                fg="black")
F2.place(x=11, y=121, anchor="nw", width=280, height=140)
img1022 = PhotoImage(file="icons/img1022.png")
vamp12 = Label(root,image=img1022,bg="white")
vamp12.place(x=7,y=145)
L4 = ttk.Label(F2,
           text="Mouse Button:").grid(row=0, column=1, pady=15, padx=5, sticky="ew")
clicked = StringVar()
clicked.set("Left")
llist = ["Left", "Right"]
drop1 = ttk.Combobox(F2, values=llist, width=8, state='readonly')

drop1.grid(row=0, column=2, sticky="ew")
drop1.config(font="SF-Pro-Display-Bold 11")
drop1.current(0)

L5 = ttk.Label(F2,
           text="Click Type:").grid(row=1, column=1, pady=10, padx=5)

llist1 = ["Single", "Double"]
drop2 = ttk.Combobox(F2, values=llist1, width=8,state='readonly')
drop2.grid(row=1, column=2, sticky="ew")
drop2.current(0)
drop2.config(font="SF-Pro-Display-Bold 11")
#Frame 2nd End
#----->
#Frame 3rd
#<----
vamp2 = Label(root,bg="white",image=imgback2)
vamp2.place(x=307,y=143)
F3 = LabelFrame(root,
                text="Click Repeat",
                bg="white",
                borderwidth=0,
                fg="black",
                font=('SF-Pro-Display-Bold 11'),
                width=280,
                height=140)
F3.place(x=311, y=121, width=280, height=140)
vamp13 = Label(root,image=img1022,bg="white")
vamp13.place(x=307,y=145)
var = IntVar()
var.set(2)
RB1 = ttk.Radiobutton(F3,
                  variable=var,style='BW.TRadiobutton').grid(row=1, column=1, padx=8, pady=12, sticky="w")
L4R = ttk.Label(F3,
            text="Repeat :").grid(row=1, column=2, sticky="w")
var3 = IntVar()
var3.set(1)
E5 = ttk.Spinbox(F3,
             textvariable=var3,
             from_=1,
             to=999,
             validate="key",
             validatecommand=(callback,"%P"),width=5)
E5.grid(row=1, column=3, padx=1)
E5.config(font="SF-Pro-Display-Bold 10")

RB2 =ttk.Radiobutton(F3,
                  variable=var,
                  value=2).grid(row=2,column=1,padx=8,pady=4, sticky="w")
L5R = ttk.Label(F3,
            text="Repeat Until Stopped").grid(row=2, column=2, sticky="w")

#Frame 3rd Ending
#--->
#Frame 4th
var1 = IntVar()
var1.set(1)
vamp3 = Label(root,image=imgback3,bg="white")
vamp3.place(x=10,y=297)
Frame4 = LabelFrame(root,
                    bg="white",
                    borderwidth=0,
                    text="Mouse Position",
                    font=('SF-Pro-Display-Bold 11'),
                    fg="black",
                    height=100,
                    width=400)
Frame4.place(x=14, y=275, anchor="nw", width=580, height=70)
vamp14 = Label(root,image=img1011,bg="white")
vamp14.place(x=10,y=296)
RB3 =ttk.Radiobutton(Frame4,
                  variable=var1,
                  value=1).grid(row=1, column=1, padx=8, pady=3)
Lex = ttk.Label(Frame4,
            text="Current Location").grid(row=1,pady=18, column=2,sticky="w")

#inner frame
Fin = Frame(Frame4, bg="white", height=90, width=300)
Fin.grid(row=1, column=3, padx=60)
RB4 =ttk.Radiobutton(Fin,
                  variable=var1,
                  value=2).grid(row=1, column=1)
B1 = Button(Fin,
            image=img6,
            height=38,
            width=125,
            bg="white",
            borderwidth=0,
            activebackground="white",
            command=picklocation)
B1.grid(row=1, column=2, padx=4)
B1.bind("<Enter>",changeback)
B1.bind("<Leave>",changeback1)
L6 = ttk.Label(Fin,
           text="X:").grid(row=1, column=3, padx=4)
x1 = IntVar()
y1 = IntVar()
y1.set(0)
x1.set(0)
E6 = Entry(Fin, textvariable=x1,width=3,font=("SF-Pro-Display-Bold 11")).grid(row=1, column=4,padx=3)
L7 = ttk.Label(Fin,
           text="Y:").grid(row=1, column=5, padx=4)
E7 = Entry(Fin, textvariable=y1,width=3,font=("SF-Pro-Display-Bold 11")).grid(row=1, column=6,padx=3)
# Frame 4th Ending
#Middle Frame Ending
#---->
#Bottom Frame

Bottom = Frame(root, bd=0, height=120, width=540,bg="white")
Bottom.place(x=10, y=365)
B2 = Button(Bottom,
            image=img2,bg="white",activebackground="white",borderwidth=0,height=36,
            command=start)
B2.grid(row=3, column=1, padx=25,pady=4)

B2.bind("<Enter>",changeico7)
B2.bind("<Leave>",changeico8)


B3 = Button(Bottom,
            image=img3,
            bg="white",activebackground="white",borderwidth=0,
            state=DISABLED,
            command=killswitch)
B3.grid(row=3, column=2, padx=(175,20))
B3.bind("<Enter>",changeico9)
B3.bind("<Leave>",changeico10)
B4 = Button(Bottom,
            image=img4,bg="white",activebackground="white",borderwidth=0,state="disabled")
B4.grid(row=4, column=1, padx=20, pady=1)

B5 = Button(Bottom,
            image=img5,bg="white",
            activebackground="white",
            borderwidth=0,
            command=record)
B5.grid(row=4, column=2, padx=(175,20))
B5.bind("<Enter>",changeico5)
B5.bind("<Leave>",changeico6)
# Ending Bottom Frame


root.mainloop()
