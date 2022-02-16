from tkinter import *

root= Tk()

root.geometry('1000x1000')

root.configure(bg="#535559")
#?vars

height = 80
width = 80

spacing =width +10

col1 = 10
col2 = col1 + spacing
col3 = col2 + spacing
col4 = col3 + spacing
col5 = col4 + spacing

let1_1 = "a"
let1_2 = "b"
let1_3 = "b"
let1_4 = "b"
let1_5 = "b"


#?spam of squares

r1_1 = Canvas(root, height = height, width = width)
r1_1.place(x=col1, y=10)
#letter
l1_1 = Label(r1_1, text=let1_1, height = 5, width =  10, fg="black")
l1_1.pack()

r1_2 = Canvas(root, height = height, width = width)
r1_2.place(x=col2, y=10)
#letter
l1_2 = Label(r1_2, text=let1_2, height = 5, width =  10, fg="black")
l1_2.pack()

r1_3 = Canvas(root, height = height, width = width)
r1_3.place(x=col2, y=10)
#letter
l1_3 = Label(r1_2, text=let1_3, height = 5, width =  10, fg="black")
l1_3.pack()

r1_4 = Canvas(root, height = height, width = width)
r1_4.place(x=col2, y=10)
#letter
l1_4 = Label(r1_2, text=let1_4, height = 5, width =  10, fg="black")
l1_4.pack()

r1_5 = Canvas(root, height = height, width = width)
r1_5.place(x=col2, y=10)
#letter
l1_5 = Label(r1_2, text=let1_5, height = 5, width =  10, fg="black")
l1_5.pack()


root.mainloop()