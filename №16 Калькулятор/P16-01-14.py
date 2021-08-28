from tkinter import *
from math import sqrt
X=0
operation="" #хранит вид операции
def onClick(n): #ввод чисел
    if label1['text']=="0": label1['text']=str(n)
    elif type(label1['text'])==int or type(label1['text'])==float or label1["text"]=="Деление на ноль невозможно": label1['text']=str(n)
    else: label1['text']+=str(n)
    CheckLabel()

def onClickOperation(n): #передает в operation вид операции и очищает label для ввода второго числа
    global X,operation
    X=float(label1["text"])
    label1["text"]="0"
    operation=n

def onClickEq(): #при нажатии "равно" в зависимости от вида операции, переданной в переменную operation
    global X,operation
    if operation=="+" or operation=="plus": label1['text']=X+float(label1['text'])
    if operation == "-" or operation=="minus": label1['text'] = X - float(label1['text'])
    if operation == "*" or operation=="asterisk": label1['text'] = X * float(label1['text'])
    if operation == "/" or operation=="slash":
        if label1["text"]!="0":
            label1['text'] = X / float(label1['text'])
        else: label1["text"]="Деление на ноль невозможно"
    operation=""
    CheckLabel() #описана ниже

def onClickX(n): #для операций с введенным числом (возведение в квадрат, квадратный корень и пр.)
    if n=="sqrt": label1["text"]=sqrt(float(label1["text"]))
    if n=="sqr": label1["text"]=(float(label1["text"]))**2
    if n=="1/x":
        if label1["text"]!="0":
            label1["text"]=1/(float(label1["text"]))
        else: label1["text"]="Деление на ноль невозможно"
    if n=="+-": label1["text"] = str(0-float(label1["text"]))
    if n=="del":
        S=str(label1["text"])
        L=int(len(S))
        if L!=1:
            label1["text"]=S[0:L-1]
        else: label1["text"]="0"
        CheckLabel()
    if n=="C": label1["text"]="0"
    if n=="CE":
        global X, operation
        label1["text"] = "0"
        X=0
        operation=""
    if n=="%":
        if X!=0:
            percent=float(label1["text"])/100
            label1["text"]=str(percent*X)
        else: label1["text"]="0"
    CheckLabel()

def CheckLabel(): #изменяет размер шрифта в label при увеличивающимся количестве знаков
    if type(label1['text'])!=str: L = len(str(label1['text']))
    else: L = len(label1['text'])
    if 12<=L<=13: label1['font'] = "Arial 32"
    if 14<=L<=15: label1['font'] = "Arial 30"
    if L>=16: label1['font'] = "Arial 28"
    if L<12: label1['font'] = "Arial 36"

def KeyButton(e): #ввод с клавиатуры
    k=e.keysym
    if k.isdigit()==True: onClick(e.keysym) #если вводится число, то вызывается соот-щая ф-ция
    if k=="slash" or k=="asterisk" or k=="minus" or k=="plus": onClickOperation(e.keysym) #также с операциями
    if k=="Return": onClickEq()
    if k=="BackSpace": onClickX("del")
    if k=="period": onClick(".")

form1=Tk()
form1.geometry("330x460+250+300")
form1.title("Калькулятор")
form1.minsize(width=330,height=460)
form1.maxsize(width=490,height=620)

options={"fill": BOTH,"expand": True,"side": LEFT,"padx": 2,"pady": 2} #параметры pack для кнопок

frame1=Frame(form1,bg="#505050") #в каждом frame по 4 кнопки (всего 6 frame-ов)
frame1.pack(fill=BOTH)
label1=Label(frame1,text="0",font="Arial 36",bg="#505050",fg="white")
label1.pack(fill=BOTH,side=RIGHT,pady=20)

frame2=Frame(form1,bg="#505050")
frame2.pack(fill=BOTH,expand=True)
button1=Button(frame2,text=chr(37),font="Arial 14",fg="white",bg="#40424e",command=lambda: onClickX("%")).pack(**options)
button2=Button(frame2,text=chr(8730),font="Arial 16",fg="white",bg="#40424e",command=lambda: onClickX("sqrt")).pack(**options)
button3=Button(frame2,text="x"+chr(178),font="Arial 14",fg="white",bg="#40424e",command=lambda: onClickX("sqr")).pack(**options)
button4=Button(frame2,text="1/x",font="Arial 12 bold",fg="white",bg="#40424e",command=lambda: onClickX("1/x")).pack(**options)

frame3=Frame(form1,bg="#505050")
frame3.pack(fill=BOTH,expand=True)
button5=Button(frame3,text="CE",font="Arial 10 bold",fg="white",bg="#40424e",command=lambda: onClickX("CE")).pack(**options)
button6=Button(frame3,text="C",font="Arial 12",fg="white",bg="#40424e",command=lambda: onClickX("C")).pack(**options)
button7=Button(frame3,text=chr(8592),font="Arial 12 bold",fg="white",bg="#40424e",command=lambda: onClickX("del")).pack(**options)
button8=Button(frame3,text=chr(247),font="Arial 16 bold",fg="white",bg="#40424e",command=lambda: onClickOperation("/")).pack(**options)

frame4=Frame(form1,bg="#505050")
frame4.pack(fill=BOTH,expand=True)
button9=Button(frame4,text="7",font="Arial 14",bg="#0f0f0f",fg="white",command=lambda: onClick(7)).pack(**options)
button10=Button(frame4,text="8",font="Arial 14",bg="#0f0f0f",fg="white",command=lambda: onClick(8)).pack(**options)
button11=Button(frame4,text="9",font="Arial 14",bg="#0f0f0f",fg="white",command=lambda: onClick(9)).pack(**options)
button12=Button(frame4,text=chr(215),font="Arial 16 bold",fg="white",bg="#40424e",command=lambda: onClickOperation("*")).pack(**options)

frame5=Frame(form1,bg="#505050")
frame5.pack(fill=BOTH,expand=True)
button13=Button(frame5,text="4",font="Arial 14",bg="#0f0f0f",fg="white",command=lambda: onClick(4)).pack(**options)
button14=Button(frame5,text="5",font="Arial 14",bg="#0f0f0f",fg="white",command=lambda: onClick(5)).pack(**options)
button15=Button(frame5,text="6",font="Arial 14",bg="#0f0f0f",fg="white",command=lambda: onClick(6)).pack(**options)
button16=Button(frame5,text=chr(8722),font="Arial 16 bold",fg="white",bg="#40424e",command=lambda: onClickOperation("-")).pack(**options)

frame6=Frame(form1,bg="#505050")
frame6.pack(fill=BOTH,expand=True)
button17=Button(frame6,text="1",font="Arial 14",bg="#0f0f0f",fg="white",command=lambda: onClick(1)).pack(**options)
button18=Button(frame6,text="2",font="Arial 14",bg="#0f0f0f",fg="white",command=lambda: onClick(2)).pack(**options)
button19=Button(frame6,text="3",font="Arial 14",bg="#0f0f0f",fg="white",command=lambda: onClick(3)).pack(**options)
button20=Button(frame6,text="+",font="Arial 16 bold",fg="white",bg="#40424e",command=lambda: onClickOperation("+")).pack(**options)

frame7=Frame(form1,bg="#505050")
frame7.pack(fill=BOTH,expand=True)
button21=Button(frame7,text=chr(177),font="Arial 14",fg="white",bg="#40424e",command=lambda: onClickX("+-")).pack(**options)
button22=Button(frame7,text="0",font="Arial 14",bg="#0f0f0f",fg="white",command=lambda: onClick(0)).pack(**options)
button23=Button(frame7,text=".",font="Arial 16 bold",fg="white",bg="#40424e",command=lambda: onClick(".")).pack(**options)
button24=Button(frame7,text="=",font="Arial 16 bold",fg="white",bg="#40424e",command=onClickEq).pack(**options)

form1.bind("<Key>",KeyButton)

form1.mainloop()