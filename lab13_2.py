from tkinter import *

result = ""


def onpress(i):
    global result

    if i == 0:
        result += "taken Chemistry\n"
    elif i == 1:
        result += "taken Physics\n"
    elif i == 2:
        result += "taken Biology\n"
    elif i == 3:
        result += "taken Math\n"
    elif i == 4:
        result += "taken English\n"
    elif i == 5:
        result += "blood type A\n"
    elif i == 6:
        result += "blood type B\n"
    elif i == 7:
        result += "blood type O\n"
    elif i == 8:
        result += "blood type AB\n"


def getreport():
    root2 = Tk()
    Message(root2, text = entry1.get() + "\n" + result).pack()

root = Tk()

label1 = Label(root, text="Enter your full name:")
label1.grid(row=0, column=0, sticky="w")

entry1 = Entry(root)
entry1.grid(row=0, column=1)

label2 = Label(root, text="Select subject(s) you had taken:")
label2.grid(row=1, column=0)

for i in range(5):
    if i == 0:
        chk = Checkbutton(root, text='Chemistry', command=(lambda i=i: onpress(i)) )
    if i == 1:
        chk = Checkbutton(root, text='Physics', command=(lambda i=i: onpress(i)) )
    if i == 2:
        chk = Checkbutton(root, text='Biology', command=(lambda i=i: onpress(i)) )
    if i == 3:
        chk = Checkbutton(root, text='Math', command=(lambda i=i: onpress(i)) )
    if i == 4:
        chk = Checkbutton(root, text='English', command=(lambda i=i: onpress(i)) )

    chk.grid(row=1, column=(i+1))

label3 = Label(root, text="What is your blood type?")
label3.grid(row=2, column=0, sticky="w")

bt = ["A", "B", "O", "AB"]

var = StringVar()
var.set(None)

for i in range(4):
    rad = Radiobutton(root, text=bt[i], variable=var, value=str(i), command=(lambda
                      i=(i+5): onpress(i)))
    rad.grid(row=2, column=(i+1))

button1 = Button(root, text="Report", command=getreport)
button1.grid(row=3, columnspan=5, sticky="e")

root.mainloop()
