from tkinter import *
root = Tk()
ms = 0
s = 0
m = 0
h = 0
d = 0


def tick():
    global ms, s, m, h, d
    ms += 1
    if ms > 9999:
        ms = 0
        s = s + 1
    if s > 59:
        s = 0
        m = m + 1

    if m > 59:
        m = 0
        h = h + 1

    if h > 23:
        h = 0
        d = d + 1

    label1['text'] = str(d) + " day " + str(h) + ":" + str(m) + ":" + str(s) + ":" + \
        str(ms)

    global task
    task = label1.after(1, tick)


def stopit():
    label1.after_cancel(task)

label1 = Label(root, width=15)
label1.grid(row=0, columnspan=2)

button1 = Button(root, text='Start', command=tick)
button1.grid(row=1, column=0)

button2 = Button(root, text='Stop', command=stopit)
button2.grid(row=1, column=1)

root.mainloop()
