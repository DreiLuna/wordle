from tkinter import *
from enchant.checker import SpellChecker

root= Tk()

root.geometry('1000x1000')

root.configure(bg="#535559")
#?vars
my_word = "not the word"

correct_word = "those"



#!one file pogint

def wguesse(letterpressed):
    if changerow == 0:
        #!row 1 
        if collumcheck == 1:
            print("i got here")
            global let1_1
            let1_1 = letterpressed
            print("igot past there")
            l1_1.configure(text=let1_1)
            print("i dont think so")
        elif collumcheck == 2:
            global let1_2
            let1_2 = letterpressed
            l1_2.configure(text=let1_2)
        elif collumcheck == 3:
            global let1_3
            let1_3 = letterpressed
            l1_3.configure(text=let1_3)
        elif collumcheck == 4:
            global let1_4
            let1_4 = letterpressed
            l1_4.configure(text=let1_4)
        elif collumcheck == 5:
            global let1_5
            let1_5 = letterpressed
            l1_5.configure(text=let1_5)
        elif collumcheck == 6:
            global my_word
            my_word = str(let1_1) + str(let1_2) + str(let1_3) + str(let1_4) + str(let1_5)
'''
    #!row 2 
    let2_1
    let2_2
    let2_3
    let2_4
    let2_5
    #!row 3 
    let3_1
    let3_2
    let3_3
    let3_4
    let3_5
    #!row 4
    let4_1
    let4_2
    let4_3
    let4_4
    let4_5
    #!row 5
    let5_1
    let5_2
    let5_3
    let5_4
    let5_5
    #!row 6
    let6_1
    let6_2
    let6_3
    let6_4
    let6_5
'''
#!-------------
heightl = 5
widthl = 5

#!def for said buttons
global collumcheck
collumcheck = 0
global changerow
changerow = 0
def exa():
    global collumcheck
    collumcheck = int(collumcheck) + 1
    print(collumcheck)
    letterpressed = "a"
    wguesse(letterpressed)
    print("work")
def exb():
    global collumcheck
    collumcheck = int(collumcheck) + 1
    letterpressed = "b"
    wguesse(letterpressed)
def exc():
    global collumcheck
    collumcheck = int(collumcheck) + 1
    letterpressed = "c"
    wguesse(letterpressed)
def exd():
    global collumcheck
    collumcheck = int(collumcheck) + 1
    letterpressed = "d"
    wguesse(letterpressed)
def exe():
    global collumcheck
    collumcheck = int(collumcheck) + 1
    letterpressed = "e"
    wguesse(letterpressed)
def exf():
    global collumcheck
    collumcheck = int(collumcheck) + 1
    letterpressed = "f"
    wguesse(letterpressed)
def exg():
    global collumcheck
    collumcheck = int(collumcheck) + 1
    letterpressed = "g"
    wguesse(letterpressed)
def exh():
    global collumcheck
    collumcheck = int(collumcheck) + 1
    letterpressed = "h"
    wguesse(letterpressed)
def exi():
    global collumcheck
    collumcheck = int(collumcheck) + 1
    letterpressed = "i"
    wguesse(letterpressed)
def exj():
    global collumcheck
    collumcheck = int(collumcheck) + 1
    letterpressed = "j"
    wguesse(letterpressed)
def exk():
    global collumcheck
    collumcheck = int(collumcheck) + 1
    letterpressed = "k"
    wguesse(letterpressed)
def exl():
    global collumcheck
    collumcheck = int(collumcheck) + 1
    letterpressed = "l"
    wguesse(letterpressed)
def exm():
    global collumcheck
    collumcheck = int(collumcheck) + 1
    letterpressed = "m"
    wguesse(letterpressed)
def exn():
    global collumcheck
    collumcheck = int(collumcheck) + 1
    letterpressed = "n"
    wguesse(letterpressed)
def exo():
    global collumcheck
    collumcheck = int(collumcheck) + 1
    letterpressed = "o"
    wguesse(letterpressed)
def exp():
    global collumcheck
    collumcheck = int(collumcheck) + 1
    letterpressed = "p"
    wguesse(letterpressed)
def exq():
    global collumcheck
    collumcheck = int(collumcheck) + 1
    letterpressed = "q"
    wguesse(letterpressed)
def exr():
    global collumcheck
    collumcheck = int(collumcheck) + 1
    letterpressed = "r"
    wguesse(letterpressed)
def exs():
    global collumcheck
    collumcheck = int(collumcheck) + 1
    letterpressed = "s"
    wguesse(letterpressed)
def ext():
    global collumcheck
    collumcheck = int(collumcheck) + 1
    letterpressed = "t"
    wguesse(letterpressed)
def exu():
    global collumcheck
    collumcheck = int(collumcheck) + 1
    letterpressed = "u"
    wguesse(letterpressed)
def exv():
    global collumcheck
    collumcheck = int(collumcheck) + 1
    letterpressed = "v"
    wguesse(letterpressed)
def exw():
    global collumcheck
    collumcheck = int(collumcheck) + 1
    letterpressed = "w"
    wguesse(letterpressed)
def exx():
    global collumcheck
    collumcheck = int(collumcheck) + 1
    letterpressed = "x"
    wguesse(letterpressed)
def exy():
    global collumcheck
    collumcheck = int(collumcheck) + 1
    letterpressed = "y"
    wguesse(letterpressed)
def exz():
    global collumcheck
    collumcheck = int(collumcheck) + 1
    letterpressed = "z"
    wguesse(letterpressed)
def ent():

    #? Finish checking if word is correct - still need to make the word - mabey make a new function for that(most likely)
    global checkword
    checkword = 1
    global collumcheck
    collumcheck = 6
    error_checker = 0
    filler = " filler"
    wguesse(filler)
    global changerow
    chkr = SpellChecker("en_US")
    chkr.set_text(my_word)
    for err in chkr:
        print("ERROR, not a proper word:", err.word)
        error_checker = 1
        errorlable = Label(root, text=err.word + " is not a word. Please clear and try again.", )
        errorlable.place(x= 500, y=10)


    if error_checker == 0:
        changerow = changerow + 1
        print("your word is " + str(my_word))
        errorlable = Label(root, text=my_word + " is your word", )
        errorlable.place(x= 500, y=10)



#!buttons
leta = Button(root, text="a", height=heightl, width=widthl, command = exa)
letb = Button(root, text="b", height=heightl, width=widthl, command = exb)
letc = Button(root, text="c", height=heightl, width=widthl, command = exc)
letd = Button(root, text="d", height=heightl, width=widthl, command = exd)
lete = Button(root, text="e", height=heightl, width=widthl, command = exe)
letf = Button(root, text="f", height=heightl, width=widthl, command = exf)
letg = Button(root, text="g", height=heightl, width=widthl, command = exg)
leth = Button(root, text="h", height=heightl, width=widthl, command = exh)
leti = Button(root, text="i", height=heightl, width=widthl, command = exi)
letj = Button(root, text="j", height=heightl, width=widthl, command = exj)
letk = Button(root, text="k", height=heightl, width=widthl, command = exk)
letl = Button(root, text="l", height=heightl, width=widthl, command = exl)
letm = Button(root, text="m", height=heightl, width=widthl, command = exm)
letn = Button(root, text="n", height=heightl, width=widthl, command = exn)
leto = Button(root, text="o", height=heightl, width=widthl, command = exo)
letp = Button(root, text="p", height=heightl, width=widthl, command = exp)
letq = Button(root, text="q", height=heightl, width=widthl, command = exq)
letr = Button(root, text="r", height=heightl, width=widthl, command = exr)
lets = Button(root, text="s", height=heightl, width=widthl, command = exs)
lett = Button(root, text="t", height=heightl, width=widthl, command = ext)
letu = Button(root, text="u", height=heightl, width=widthl, command = exu)
letv = Button(root, text="v", height=heightl, width=widthl, command = exv)
letw = Button(root, text="w", height=heightl, width=widthl, command = exw)
letx = Button(root, text="x", height=heightl, width=widthl, command = exx)
lety = Button(root, text="y", height=heightl, width=widthl, command = exy)
letz = Button(root, text="z", height=heightl, width=widthl, command = exz)

ent = Button(root, text="enter", height=heightl, width=12, command = ent)


xspacing = (widthl*10) + 10
yspacing = (widthl*10) + 50

xcol1 = 10
yrow1 = 500

xcol2 = xcol1 +xspacing
xcol3 = xcol2 +xspacing
xcol4 = xcol3 +xspacing
xcol5 = xcol4 +xspacing
xcol6 = xcol5 +xspacing
xcol7 = xcol6 +xspacing
xcol8 = xcol7 +xspacing
xcol9 = xcol8 +xspacing
xcol10 = xcol9 +xspacing

yrow2 = yrow1 + yspacing
yrow3 = yrow2 + yspacing

offset1 = 25
offset2 = 50
#r1
letq.place(x=xcol1, y=yrow1)
letw.place(x=xcol2, y=yrow1)
lete.place(x=xcol3, y=yrow1)
letr.place(x=xcol4, y=yrow1)
lett.place(x=xcol5, y=yrow1)
lety.place(x=xcol6, y=yrow1)
letu.place(x=xcol7, y=yrow1)
leti.place(x=xcol8, y=yrow1)
leto.place(x=xcol9, y=yrow1)
letp.place(x=xcol10, y=yrow1)
#r2

leta.place(x=xcol1+offset1, y=yrow2)
lets.place(x=xcol2+offset1, y=yrow2)
letd.place(x=xcol3+offset1, y=yrow2)
letf.place(x=xcol4+offset1, y=yrow2)
letg.place(x=xcol5+offset1, y=yrow2)
leth.place(x=xcol6+offset1, y=yrow2)
letj.place(x=xcol7+offset1, y=yrow2)
letk.place(x=xcol8+offset1, y=yrow2)
letl.place(x=xcol9+offset1, y=yrow2)

#r3
letz.place(x=xcol1+offset2, y=yrow3)
letx.place(x=xcol2+offset2, y=yrow3)
letc.place(x=xcol3+offset2, y=yrow3)
letv.place(x=xcol4+offset2, y=yrow3)
letb.place(x=xcol5+offset2, y=yrow3)
letn.place(x=xcol6+offset2, y=yrow3)
letm.place(x=xcol7+offset2, y=yrow3)
ent.place(x=xcol8+offset2, y=yrow3)


#?vars for squares
let1_1 = " "
let1_2 = " "
let1_3 = " "
let1_4 = " "
let1_5 = " "

let2_1 = " "
let2_2 = " "
let2_3 = " "
let2_4 = " "
let2_5 = " "

let3_1 = " "
let3_2 = " "
let3_3 = " "
let3_4 = " "
let3_5 = " "

let4_1 = " "
let4_2 = " "
let4_3 = " "
let4_4 = " "
let4_5 = " "

let5_1 = " "
let5_2 = " "
let5_3 = " "
let5_4 = " "
let5_5 = " "

let6_1 = " "
let6_2 = " "
let6_3 = " "
let6_4 = " "
let6_5 = " "

height = 70
width = 70

leth =4
letw =8
spacing =width +10

col1 = 10
col2 = col1 + spacing
col3 = col2 + spacing
col4 = col3 + spacing
col5 = col4 + spacing

row1 = 10
row2 = row1 + height + 10
row3 = row2 + height + 10
row4 = row3 + height + 10
row5 = row4 + height + 10
row6 = row5 + height + 10
#?spam of squares
#!r1
r1_1 = Canvas(root, height = height, width = width)
r1_1.place(x=col1, y=10)
#letter
l1_1 = Label(r1_1, text=let1_1, height = leth, width =  letw, fg="black")
l1_1.pack()

r1_2 = Canvas(root, height = height, width = width)
r1_2.place(x=col2, y=10)
#letter
l1_2 = Label(r1_2, text=let1_2, height = leth, width =  letw, fg="black")
l1_2.pack()

r1_3 = Canvas(root, height = height, width = width)
r1_3.place(x=col3, y=10)
#letter
l1_3 = Label(r1_3, text=let1_3, height = leth, width =  letw, fg="black")
l1_3.pack()

r1_4 = Canvas(root, height = height, width = width)
r1_4.place(x=col4, y=10)
#letter
l1_4 = Label(r1_4, text=let1_4, height = leth, width =  letw, fg="black")
l1_4.pack()

r1_5 = Canvas(root, height = height, width = width)
r1_5.place(x=col5, y=10)
#letter
l1_5 = Label(r1_5, text=let1_5, height = leth, width =  letw, fg="black")
l1_5.pack()

#!r2
r2_1 = Canvas(root, height = height, width = width)
r2_1.place(x=col1, y=row2)
#letter
l2_1 = Label(r2_1, text=let2_1, height = leth, width =  letw, fg="black")
l2_1.pack()

r2_2 = Canvas(root, height = height, width = width)
r2_2.place(x=col2, y=row2)
#letter
l2_2 = Label(r2_2, text=let2_2, height = leth, width =  letw, fg="black")
l2_2.pack()

r2_3 = Canvas(root, height = height, width = width)
r2_3.place(x=col3, y=row2)
#letter
l2_3 = Label(r2_3, text=let2_3, height = leth, width =  letw, fg="black")
l2_3.pack()

r2_4 = Canvas(root, height = height, width = width)
r2_4.place(x=col4, y=row2)
#letter
l2_4 = Label(r2_4, text=let2_4, height = leth, width =  letw, fg="black")
l2_4.pack()

r2_5 = Canvas(root, height = height, width = width)
r2_5.place(x=col5, y=row2)
#letter
l2_5 = Label(r2_5, text=let2_5, height = leth, width =  letw, fg="black")
l2_5.pack()
#!r3
r3_1 = Canvas(root, height = height, width = width)
r3_1.place(x=col1, y=row3)
#letter
l3_1 = Label(r3_1, text=let3_1, height = leth, width =  letw, fg="black")
l3_1.pack()

r3_2 = Canvas(root, height = height, width = width)
r3_2.place(x=col2, y=row3)
#letter
l3_2 = Label(r3_2, text=let3_2, height = leth, width =  letw, fg="black")
l3_2.pack()

r3_3 = Canvas(root, height = height, width = width)
r3_3.place(x=col3, y=row3)
#letter
l3_3 = Label(r3_3, text=let3_3, height = leth, width =  letw, fg="black")
l3_3.pack()

r3_4 = Canvas(root, height = height, width = width)
r3_4.place(x=col4, y=row3)
#letter
l3_4 = Label(r3_4, text=let3_4, height = leth, width =  letw, fg="black")
l3_4.pack()

r3_5 = Canvas(root, height = height, width = width)
r3_5.place(x=col5, y=row3)
#letter
l3_5 = Label(r3_5, text=let3_5, height = leth, width =  letw, fg="black")
l3_5.pack()
#!r4
r4_1 = Canvas(root, height = height, width = width)
r4_1.place(x=col1, y=row4)
#letter
l4_1 = Label(r4_1, text=let4_1, height = leth, width =  letw, fg="black")
l4_1.pack()

r4_2 = Canvas(root, height = height, width = width)
r4_2.place(x=col2, y=row4)
#letter
l4_2 = Label(r4_2, text=let4_2, height = leth, width =  letw, fg="black")
l4_2.pack()

r4_3 = Canvas(root, height = height, width = width)
r4_3.place(x=col3, y=row4)
#letter
l4_3 = Label(r4_3, text=let4_3, height = leth, width =  letw, fg="black")
l4_3.pack()

r4_4 = Canvas(root, height = height, width = width)
r4_4.place(x=col4, y=row4)
#letter
l4_4 = Label(r4_4, text=let4_4, height = leth, width =  letw, fg="black")
l4_4.pack()

r4_5 = Canvas(root, height = height, width = width)
r4_5.place(x=col5, y=row4)
#letter
l4_5 = Label(r4_5, text=let4_5, height = leth, width =  letw, fg="black")
l4_5.pack()
#!5
r5_1 = Canvas(root, height = height, width = width)
r5_1.place(x=col1, y=row5)
#letter
l5_1 = Label(r5_1, text=let5_1, height = leth, width =  letw, fg="black")
l5_1.pack()

r5_2 = Canvas(root, height = height, width = width)
r5_2.place(x=col2, y=row5)
#letter
l5_2 = Label(r5_2, text=let5_2, height = leth, width =  letw, fg="black")
l5_2.pack()

r5_3 = Canvas(root, height = height, width = width)
r5_3.place(x=col3, y=row5)
#letter
l5_3 = Label(r5_3, text=let5_3, height = leth, width =  letw, fg="black")
l5_3.pack()

r5_4 = Canvas(root, height = height, width = width)
r5_4.place(x=col4, y=row5)
#letter
l5_4 = Label(r5_4, text=let5_4, height = leth, width =  letw, fg="black")
l5_4.pack()

r5_5 = Canvas(root, height = height, width = width)
r5_5.place(x=col5, y=row5)
#letter
l5_5 = Label(r5_5, text=let5_5, height = leth, width =  letw, fg="black")
l5_5.pack()
#!r6
r6_1 = Canvas(root, height = height, width = width)
r6_1.place(x=col1, y=row6)
#letter
l6_1 = Label(r6_1, text=let6_1, height = leth, width =  letw, fg="black")
l6_1.pack()

r6_2 = Canvas(root, height = height, width = width)
r6_2.place(x=col2, y=row6)
#letter
l6_2 = Label(r6_2, text=let6_2, height = leth, width =  letw, fg="black")
l6_2.pack()

r6_3 = Canvas(root, height = height, width = width)
r6_3.place(x=col3, y=row6)
#letter
l6_3 = Label(r6_3, text=let6_3, height = leth, width =  letw, fg="black")
l6_3.pack()

r6_4 = Canvas(root, height = height, width = width)
r6_4.place(x=col4, y=row6)
#letter
l6_4 = Label(r6_4, text=let6_4, height = leth, width =  letw, fg="black")
l6_4.pack()

r6_5 = Canvas(root, height = height, width = width)
r6_5.place(x=col5, y=row6)
#letter
l6_5 = Label(r6_5, text=let6_5, height = leth, width =  letw, fg="black")
l6_5.pack()

root.mainloop()