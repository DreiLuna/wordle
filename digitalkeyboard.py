from tkinter import *
root = Tk()

root.geometry("1000x1000")

heightl = 5
widthl = 5

#!def for said buttons
def exa():
    print('a')
def exb():
    print('b')
def exc():
    print('c')
def exd():
    print('d')
def exe():
    print('e')
def exf():
    print('f')
def exg():
    print('g')
def exh():
    print('h')
def exi():
    print('i')
def exj():
    print('j')
def exk():
    print('k')
def exl():
    print('l')
def exm():
    print('m')
def exn():
    print('n')
def exo():
    print('o')
def exp():
    print('p')
def exq():
    print('q')
def exr():
    print('r')
def exs():
    print('s')
def ext():
    print('t')
def exu():
    print('u')
def exv():
    print('v')
def exw():
    print('w')
def exx():
    print('x')
def exy():
    print('y')
def exz():
    print('z')

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

xspacing = (widthl*10) + 10
yspacing = (widthl*10) + 50

xcol1 = 10
yrow1 = 10

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
#r2
leta.place(x=xcol1, y=yrow1)
letb.place(x=xcol2, y=yrow1)
letc.place(x=xcol3, y=yrow1)
letd.place(x=xcol4, y=yrow1)
lete.place(x=xcol5, y=yrow1)
letf.place(x=xcol6, y=yrow1)
letg.place(x=xcol7, y=yrow1)
leth.place(x=xcol8, y=yrow1)
leti.place(x=xcol9, y=yrow1)
letj.place(x=xcol10, y=yrow1)
#r2

letk.place(x=xcol1, y=yrow2)
letl.place(x=xcol2, y=yrow2)
letm.place(x=xcol3, y=yrow2)
letn.place(x=xcol4, y=yrow2)
leto.place(x=xcol5, y=yrow2)
letp.place(x=xcol6, y=yrow2)
letq.place(x=xcol7, y=yrow2)
letr.place(x=xcol8, y=yrow2)
leta.place(x=xcol9, y=yrow2)

lett.place(x=xcol1, y=yrow3)
letu.place(x=xcol2, y=yrow3)
letv.place(x=xcol3, y=yrow3)
letw.place(x=xcol4, y=yrow3)
letx.place(x=xcol5, y=yrow3)
lety.place(x=xcol6, y=yrow3)
letz.place(x=xcol7, y=yrow3)


root.mainloop()