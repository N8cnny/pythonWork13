from tkinter import *
import math

root = Tk()
root.title("Calc")
root.geometry('135x190')

v = StringVar("")


def OnClick(obj):
    if obj == "btn1":
        v.set(v.get() + "7")
    if obj == "btn2":
        v.set(v.get() + "8")
    if obj == "btn3":
        v.set(v.get() + "9")
    if obj == "btn4":
        v.set(v.get() + "+")

    if obj == "btn5":
        v.set(v.get() + "4")
    if obj == "btn6":
        v.set(v.get() + "5")
    if obj == "btn7":
        v.set(v.get() + "6")
    if obj == "btn8":
        v.set(v.get() + "-")

    if obj == "btn9":
        v.set(v.get() + "1")
    if obj == "btn10":
        v.set(v.get() + "2")
    if obj == "btn11":
        v.set(v.get() + "3")
    if obj == "btn12":
        v.set(v.get() + "*")

    if obj == "btn13":
        v.set(v.get() + ".")
    if obj == "btn14":
        v.set(v.get() + "0")
    if obj == "btn15":
        v.set("")
    if obj == "btn16":
        v.set(v.get() + "/")

    if obj == "btn17":
        v.set(eval("1.0/float(" +v.get() + ")"))
    if obj == "btn18":
        v.set(eval("math.sqrt(" +v.get() + ")"))
    if obj == "btn19":
        v.set(v.get() + "%")
    if obj == "btn20":
        v.set(eval(v.get()))

    if obj == "btn21":
        v.set(v.get() + "(")
    if obj == "btn22":
        v.set(v.get() + ")")
    if obj == "btn23":
        v.set(v.get() + "[")
    if obj == "btn24":
        v.set(v.get() + "]")

entry1 = Entry(root, textvariable=v, justify=RIGHT).grid(row=0, column=0,
                                                         columnspan=4, padx=5, pady=5)
button1 = Button(root, text="7", width=3,
                 command=lambda: OnClick('btn1')).grid(row=1, column=0)

button2 = Button(root, text="8", width=3,
                 command=lambda: OnClick('btn2')).grid(row=1, column=1)

button3 = Button(root, text="9", width=3,
                 command=lambda: OnClick('btn3')).grid(row=1, column=2)

button4 = Button(root, text="+", width=3,
                 command=lambda: OnClick('btn4')).grid(row=1, column=3)

button5 = Button(root, text="4", width=3,
                 command=lambda: OnClick('btn5')).grid(row=2, column=0)

button6 = Button(root, text="5", width=3,
                 command=lambda: OnClick('btn6')).grid(row=2, column=1)

button7 = Button(root, text="6", width=3,
                 command=lambda: OnClick('btn7')).grid(row=2, column=2)

button8 = Button(root, text="-", width=3,
                 command=lambda: OnClick('btn8')).grid(row=2, column=3)

button9 = Button(root, text="1", width=3,
                 command=lambda: OnClick('btn9')).grid(row=3, column=0)

button10 = Button(root, text="2", width=3,
                  command=lambda: OnClick('btn10')).grid(row=3, column=1)

button11 = Button(root, text="3", width=3,
                  command=lambda: OnClick('btn11')).grid(row=3, column=2)

button12 = Button(root, text="*", width=3,
                  command=lambda: OnClick('btn12')).grid(row=3, column=3)

button13 = Button(root, text=".", width=3,
                  command=lambda: OnClick('btn13')).grid(row=4, column=0)

button14 = Button(root, text="0", width=3,
                  command=lambda: OnClick('btn14')).grid(row=4, column=1)

button15 = Button(root, text="Cls", width=3,
                  command=lambda: OnClick('btn15')).grid(row=4, column=2)

button16 = Button(root, text="/", width=3,
                  command=lambda: OnClick('btn16')).grid(row=4, column=3)

button17 = Button(root, text="1/x", width=3,
                  command=lambda: OnClick('btn17')).grid(row=5, column=0)

button18 = Button(root, text="sqrt", width=3,
                  command=lambda: OnClick('btn18')).grid(row=5, column=1)

button19 = Button(root, text="Mod", width=3,
                  command=lambda: OnClick('btn19')).grid(row=5, column=2)

button20 = Button(root, text="=", width=3,
                  command=lambda: OnClick('btn20')).grid(row=5, column=3)

button21 = Button(root, text="(", width=3,
                  command=lambda: OnClick('btn21')).grid(row=6, column=0)

button22 = Button(root, text=")", width=3,
                  command=lambda: OnClick('btn22')).grid(row=6, column=1)

button23 = Button(root, text="[", width=3,
                  command=lambda: OnClick('btn23')).grid(row=6, column=2)

button24 = Button(root, text="]", width=3,
                  command=lambda: OnClick('btn24')).grid(row=6, column=3)

mainloop()

