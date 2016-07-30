from tkinter import *

root = Tk()
root.geometry("500x650")


def updatevalue(event):
    f = scale1.get()
    label1['text'] = str(f) + "F = " + str((f-32) * 5/9) + "C"
    listbox1.see(f+200)
    listbox1.selection_set(first=f+200, last=None)
scale1 = Scale(root, label="Temperature (F)", from_=-200, to=200, length=600,
               tickinterval=10, resolution=1)
scale1.place(x=5, y=5)
scale1.bind("<ButtonRelease-1>", updatevalue)

label1=Label(root, text="")
label1.place(x=5, y=620)


def OnClick(e):
    f = listbox1.curselection()[0]-200
    scale1.set(f)
    label1['text'] = str(f) + "F = " + str((f-32) * 5/9) + "C"

scrollbar1 = Scrollbar(root, orient=VERTICAL)
scrollbar1.pack(side=RIGHT, fill=Y)

listbox1 = Listbox(root, width=30, height=35, selectbackground="red",
                   exportselection=False)
listbox1.bind('<<ListboxSelect>>', OnClick)

scrollbar1.configure(command=listbox1.yview)
listbox1.config(yscrollcommand=scrollbar1.set)

for f in range(-200, 200):
    listbox1.insert(END, str(f) + "F = " + str((f-32) * 5/9) + "C")

listbox1.place(x=250, y=5)

root.mainloop()

