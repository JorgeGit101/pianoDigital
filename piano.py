from tkinter import *
from playsound import playsound as play


play('D:/piano/musica/DO.mp3')

def nota_do():
    play('D:/piano/musica/DO.mp3')


def nota_re():
    play('D:/piano/musica/RE.mp3')


def nota_mi():
    play('D:/piano/musica/MI.mp3')


def nota_fa():
    play('D:/piano/musica/FA.mp3')


def nota_sol():
    play('D:/piano/musica/SOL.mp3')


def nota_la():
    play('D:/piano/musica/LA.mp3')


def nota_si():
    play('D:/piano/musica/SI.mp3')


ventana = Tk()

ventana.title('Piano')
ventana.geometry('700x340')

image = PhotoImage(file="imagenes/tec.png")

background = Label(ventana, image=image)
background.place(x=-2, y=-2)


etiqueta = Label(ventana, text='Piano con Python')
etiqueta.pack(side=TOP)
do = Button(ventana, command=nota_do, text='DO')
re = Button(ventana, command=nota_re, text='RE')
mi = Button(ventana, command=nota_mi, text='MI')
fa = Button(ventana, command=nota_fa, text='FA')
sol = Button(ventana, command=nota_sol, text='SOL')
la = Button(ventana, command=nota_la, text='LA')
si = Button(ventana, command=nota_si, text='SI')

e = Label(ventana, bg='black')
e.config(height=7, width=1)
e.pack()

e2 = Label(ventana, bg='black')
e2.config(height=1, width=1)
e2.pack(side=LEFT)

e3 = Label(ventana, bg='black')
e3.config(height=1, width=1)
e3.pack(side=TOP)

do.config(height=10, width=6)
re.config(height=10, width=6)
mi.config(height=10, width=6)
fa.config(height=10, width=6)
sol.config(height=10, width=6)
la.config(height=10, width=6)
si.config(height=10, width=6)

do.pack(side=LEFT)
re.pack(side=LEFT)
mi.pack(side=LEFT)
fa.pack(side=LEFT)
sol.pack(side=LEFT)
la.pack(side=LEFT)
si.pack(side=LEFT)

ventana.mainloop()
