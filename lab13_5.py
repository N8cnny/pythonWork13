from tkinter import *
import math

result = ""


def getmonthly():

    p = float(entry1.get())

    n = float(entry2.get())

    r = float(entry3.get()) / 100

    m = p * (math.pow((1+r), n) * r / (math.pow((1+r), n) - 1))

    result = "$" + str(round(m, 2))
    text1.insert(END, result)

root = Tk()
root.geometry("270x150")

label1 = Label(root, text="Principal:")
label1.grid(row=0, column=0, sticky="e")

entry1 = Entry(root)
entry1.grid(row=0, column=1)

label2 = Label(root, text="Number of payments:")
label2.grid(row=1, column=0, sticky="e")

entry2 = Entry(root)
entry2.grid(row=1, column=1)

label3 = Label(root, text="Monthly interest:")
label3.grid(row=2, column=0, sticky="e")

entry3 = Entry(root)
entry3.grid(row=2, column=1)

label4 = Label(root, text="Monthly payment:")
label4.grid(row=3, column=0, sticky="e")

text1 = Text(root,height=2, width=15)
text1.grid(row=3, column=1)

button1 = Button(root, text="Calculate", command=getmonthly)
button1.grid(row=4, columnspan=2, sticky="e")

root.mainloop()
