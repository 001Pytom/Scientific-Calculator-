from ast import Add
from cProfile import label
from calendar import SUNDAY
from email.mime import image, text
from time import strftime  # import time module
from tkinter import *
from turtle import width
import math
from pygame import mixer
import speech_recognition

mixer.init()

# first widget
root = Tk()
root.title("Smart calculator")
root.config(bg="white")
root.geometry("557x360")

# time function

 
def time():
    string = strftime("%H:%M:%S")  # store the time
    label_time.config(text=string)  # set time to label
    label_time.after(1000, time)  # call it on every second


# voice function


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def mod(a, b):
    return a % b


def lcm(a, b):
    lcm = math.lcm(a, b)
    return lcm


def hcf(a, b):
    hcf = math.gcd(a, b)
    return hcf


def sqr(a):
    sqr = math.sqrt(a)
    return sqr


# dictionary and keys
operatons = {"ADD": add, "ADDITION": add, "SUM": add, "PLUS": add,
             "SUBTRACTION": sub, "DIFFERENCE": sub, "MINUS": sub, "SUBTRACT": sub,
             "PRODUCT": mul, "MULTIPLICATION": mul, "MULTIPLY": mul, "TIMES": mul,
             "DIVISION": div, "DIVIDE": div, "DIV": div,
             "LCM": lcm, "HCF": hcf,
             "MOD": mod, "REMAINDER": mod, "MODULUS": mod, "SQUAREROOT": sqr}


# findnumb
def findnumbers(t):
    l = []
    for num in t:
        try:
            l.append(int(num))
        except ValueError:
            pass
    return l


# mic function
def audio():
    # object of the recognizer class sr, so that we can access the methods
    sr = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as n:  # with to create object of the class, to avoid exceptions 
        try:
            sr.adjust_for_ambient_noise(n, duration=0.2)
            voice = sr.listen(n)  # listen to the voice and store in a variable
            text = sr.recognize_google(voice)  # to convert the voice to text
            text_list = text.split(" ")
            print(text_list)
            for word in text_list:
                if word.upper() in operatons.keys():
                    l = findnumbers(text_list)
                    print(l)
                    result = operatons[word.upper()](l[0], l[1])
                    entry.delete(0, END)
                    entry.insert(END, result)
                else:
                    pass

        except:
            # if your voice isn't recognized
            pass


def onclick(value):
    num = entry.get()
    answer = ""

    try:

        if value == "C":
            num = num[0: len(num)-1]
            entry.delete(0, END)
            entry.insert(0, num)
            return

        elif value == "DEL":
            entry.delete(0, END)

        elif value == "√":
            answer = math.sqrt(eval(num))

        elif value == "π":
            answer = eval(num)*math.pi

        elif value == "Cos":
            answer = math.cos(math.radians(eval(num)))

        elif value == "Sin":
            answer = math.sin(math.radians(eval(num)))

        elif value == "tan":
            answer = math.tan(math.radians(eval(num)))

        elif value == "Cosh":
            answer = math.cosh(math.radians(eval(num)))

        elif value == "Sinh":
            answer = math.sinh(math.radians(eval(num)))

        elif value == "Tanh":
            answer = math.tanh(math.radians(eval(num)))

        elif value == "2π":
            answer = 2 * math.pi
            return

        elif value == chr(8731):
            answer = eval(num)**(1/3)

        elif value == "x\u02b8":  # x^y
            entry.insert(END, "**")
            return

        elif value == "x²":
            answer = eval(num)**2

        elif value == "ln":
            answer = math.log2(eval(num))

        elif value == "°":
            answer = math.degrees(eval(num)) 

        elif value == "Rad":
            answer = math.radians(eval(num))

        elif value == "e":
            answer = math.e

        elif value == "log":  # after looking for log, u can check degree and back to radian
            answer = math.log10(eval(num))

        elif value == "x!":
            answer = math.factorial(eval(num))

        elif value == chr(247):
            entry.insert(END, "/")
            return

        elif value == "=":
            answer = eval(num)

        elif value == "ANS":   
            answer = answer
            return
        elif value == "%":
            answer = eval(num)/100

        elif value == "x^3":
            answer = eval(num)**3

        elif value == "|x|":
            answer = math.fabs(eval(num))
            return
        else:
            entry.insert(END, value)
            return

        entry.delete(0, END)
        entry.insert(0, answer)

    except SyntaxError:
        pass


# entry field
entry = Entry(root, font=("Helvetica", 15, "bold"), bg="black",
              fg="white", bd=5, relief=SUNKEN, width=30)
entry.grid(row=0, column=0, columnspan=7)


# button declaration
Button_rad = Button(root, text="Rad", width=5, height=1, relief=RIDGE, bg="grey12",
                    fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="Rad": onclick(button))

Button1 = Button(root, text="√", width=5, height=1, relief=RIDGE, bg="grey12",
                 fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="√": onclick(button))

Button2 = Button(root, text="C", width=5, height=1, relief=RIDGE, bg="grey12",
                 fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="C": onclick(button))

Button3 = Button(root, text="(", width=5, height=1, relief=RIDGE, bg="springGreen4",
                 fg="white", font=("Helvetica", 15, "normal"), activebackground="springGreen4", padx=3, pady=3, command=lambda button="(": onclick(button))

Button4 = Button(root, text=")", width=5, height=1, relief=RIDGE, bg="springGreen4",
                 fg="white", font=("Helvetica", 15, "normal"), activebackground="springGreen4", padx=3, pady=3, command=lambda button=")": onclick(button))

Button5 = Button(root, text="%", width=5, height=1, relief=RIDGE, bg="springGreen4",
                 fg="white", font=("Helvetica", 15, "normal"), activebackground="springGreen4", padx=3, pady=3, command=lambda button="%": onclick(button))

Button6 = Button(root, text=chr(247), width=5, height=1, relief=RIDGE, bg="springGreen4",
                 fg="white", font=("Helvetica", 15, "normal"), activebackground="springGreen4", padx=3, pady=3, command=lambda button=chr(247): onclick(button))

# Button7 = Button(root, text="%", width=5, height=1, relief=RIDGE, bg="grey12",
#                    fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12")

Button8 = Button(root, text="Sin", width=5, height=1, relief=RIDGE, bg="grey12",
                 fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="Sin": onclick(button))

Button9 = Button(root, text="Cos", width=5, height=1, relief=RIDGE, bg="grey12",
                 fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="Cos": onclick(button))

Button_1 = Button(root, text="Tan", width=5, height=1, relief=RIDGE, bg="grey12",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="tan": onclick(button))

Button_2 = Button(root, text="7", width=5, height=1, relief=RIDGE, bg="grey12",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="7": onclick(button))

Button_3 = Button(root, text="8", width=5, height=1, relief=RIDGE, bg="grey12",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="8": onclick(button))

Button_4 = Button(root, text="9", width=5, height=1, relief=RIDGE, bg="grey12",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="9": onclick(button))

Button_5 = Button(root, text="*", width=5, height=1, relief=RIDGE, bg="springGreen4",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="springGreen4", padx=3, pady=3, command=lambda button="*": onclick(button))

Button_6 = Button(root, text="ln", width=5, height=1, relief=RIDGE, bg="grey12",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="ln": onclick(button))

Button_7 = Button(root, text="log", width=5, height=1, relief=RIDGE, bg="grey12",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="log": onclick(button))

Button_8 = Button(root, text="x!", width=5, height=1, relief=RIDGE, bg="grey12",
                  fg="white", font=("Helvetica", 15, "italic"), activebackground="grey12", padx=3, pady=3, command=lambda button="x!": onclick(button))

Button_9 = Button(root, text="4", width=5, height=1, relief=RIDGE, bg="grey12",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="4": onclick(button))

Button_10 = Button(root, text="5", width=5, height=1, relief=RIDGE, bg="grey12",
                   fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="5": onclick(button))

Button_11 = Button(root, text="6", width=5, height=1, relief=RIDGE, bg="grey12",
                   fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="6": onclick(button))

Button12 = Button(root, text="-", width=5, height=1, relief=RIDGE, bg="springGreen4",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="springGreen4", padx=3, pady=3, command=lambda button="-": onclick(button))

Button13 = Button(root, text="e", width=5, height=1, relief=RIDGE, bg="grey12",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="e": onclick(button))

Button14 = Button(root, text="x²", width=5, height=1, relief=RIDGE, bg="grey12",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="x²": onclick(button))

Button15 = Button(root, text="x\u02b8", width=5, height=1, relief=RIDGE, bg="grey12",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="x\u02b8": onclick(button))

Button16 = Button(root, text="1", width=5, height=1, relief=RIDGE, bg="grey12",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="1": onclick(button))

Button17 = Button(root, text="2", width=5, height=1, relief=RIDGE, bg="grey12",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="2": onclick(button))

Button18 = Button(root, text="3", width=5, height=1, relief=RIDGE, bg="grey12",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="3": onclick(button))

Button19 = Button(root, text="+", width=5, height=1, relief=RIDGE, bg="springGreen4",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="springGreen4", padx=3, pady=3, command=lambda button="+": onclick(button))

Button20 = Button(root, text="°", width=5, height=1, relief=RIDGE, bg="grey12",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="°": onclick(button))

Button21 = Button(root, text="π", width=5, height=1, relief=RIDGE, bg="grey12",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="π": onclick(button))

Button22 = Button(root, text=chr(8731), width=5, height=1, relief=RIDGE, bg="grey12",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button=chr(8731): onclick(button))

Button23 = Button(root, text="|x|", width=5, height=1, relief=RIDGE, bg="grey12",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="|x|": onclick(button))

Button24 = Button(root, text="0", width=5, height=1, relief=RIDGE, bg="grey12",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="0": onclick(button))

Button25 = Button(root, text=".", width=5, height=1, relief=RIDGE, bg="grey12",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button=".": onclick(button))

Button26 = Button(root, text="=", width=5, height=1, relief=RIDGE, bg="springGreen4",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="springGreen4", padx=3, pady=3, command=lambda button="=": onclick(button))

Button27 = Button(root, text="2π", width=5, height=1, relief=RIDGE, bg="grey12",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="2π": onclick(button))

Button28 = Button(root, text="Cosh", width=5, height=1, relief=RIDGE, bg="grey12",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="Cosh": onclick(button))

Button29 = Button(root, text="Sinh", width=5, height=1, relief=RIDGE, bg="grey12",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="Sinh": onclick(button))
Button30 = Button(root, text="Tanh", width=5, height=1, relief=RIDGE, bg="grey12",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="Tanh": onclick(button))

Button31 = Button(root, text="x^3", width=5, height=1, relief=RIDGE, bg="grey12",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="x^3": onclick(button))

Button32 = Button(root, text="DEL", width=5, height=1, relief=RIDGE, bg="grey12",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="grey12", padx=3, pady=3, command=lambda button="DEL": onclick(button))

Button33 = Button(root, text="ANS", width=5, height=1, relief=RIDGE, bg="springGreen4",
                  fg="white", font=("Helvetica", 15, "normal"), activebackground="springGreen4", padx=3, pady=3, command=lambda button="ANS": onclick(button))

# Buttton Time
label_time = Button(root, font=("Helvetica", 10, "italic"), background="black",
                    foreground="cyan", width=7, command=time, fg="white")

# buton Mic
Button_mic = Button(root, text="MIC", width=7, height=1, relief=RIDGE, bg="grey12",
                    fg="white", font=("Helvetica", 10, "italic"), activebackground="grey12", command=audio)


# display buttons
Button_rad.grid(row=1, column=0, padx=5, pady=5)
Button1.grid(row=1, column=1, padx=5, pady=5)
Button2.grid(row=1, column=2, padx=5, pady=5)
Button3.grid(row=1, column=3, padx=5, pady=5)
Button4.grid(row=1, column=4, padx=5, pady=5)
Button5.grid(row=1, column=5, padx=5, pady=5)
Button6.grid(row=1, column=6, padx=5, pady=5)
Button8.grid(row=2, column=0, padx=5, pady=5)
Button9.grid(row=2, column=1, padx=5, pady=5)
Button_1.grid(row=2, column=2, padx=5, pady=5)
Button_2.grid(row=2, column=3, padx=5, pady=5)
Button_3.grid(row=2, column=4, padx=5, pady=5)
Button_4.grid(row=2, column=5, padx=5, pady=5)
Button_5.grid(row=2, column=6, padx=5, pady=5)
Button_6.grid(row=3, column=0, padx=5, pady=5)
Button_7.grid(row=3, column=1, padx=5, pady=5)
Button_8.grid(row=3, column=2, padx=5, pady=5)
Button_9.grid(row=3, column=3, padx=5, pady=5)
Button_10.grid(row=3, column=4, padx=5, pady=5)
Button_11.grid(row=3, column=5, padx=5, pady=5)
Button12.grid(row=3, column=6, padx=5, pady=5)
Button13.grid(row=4, column=0, padx=5, pady=5)
Button13.grid(row=4, column=0, padx=5, pady=5)
Button14.grid(row=4, column=1, padx=5, pady=5)
Button15.grid(row=4, column=2, padx=5, pady=5)
Button16.grid(row=4, column=3, padx=5, pady=5)
Button17.grid(row=4, column=4, padx=5, pady=5)
Button18.grid(row=4, column=5, padx=5, pady=5)
Button19.grid(row=4, column=6, padx=5, pady=5)
Button20.grid(row=5, column=0, padx=5, pady=5)
Button21.grid(row=5, column=1, padx=5, pady=5)
Button22.grid(row=5, column=2, padx=5, pady=5)
Button23.grid(row=5, column=3, padx=5, pady=5)
Button24.grid(row=5, column=4, padx=5, pady=5)
Button25.grid(row=5, column=5, padx=5, pady=5)
Button26.grid(row=5, column=6, padx=5, pady=5)
Button27.grid(row=6, column=0, padx=5, pady=5)
Button28.grid(row=6, column=1, padx=5, pady=5)
Button29.grid(row=6, column=2, padx=5, pady=5)
Button30.grid(row=6, column=3, padx=5, pady=5)
Button31.grid(row=6, column=4, padx=5, pady=5)
Button32.grid(row=6, column=5, padx=5, pady=5)
Button33.grid(row=6, column=6, padx=5, pady=5)
# place time
label_time.grid(row=0, column=0)
# place mic
Button_mic.grid(row=0, column=6)

root.mainloop()
