from graphics import *
from random import seed
from random import randint
from time import perf_counter
from button import *
from math import sqrt

#compara la distancia del click al radio del circulo
def Compare(c,size,pM):
    r = sqrt((c.getX()-pM.getX())**2+(c.getY()-pM.getY())**2)

    if r<=size:
        return True
    else:
        return False

#muestra circulos en pantalla
def Targets(better, size, win):
    if better:
        size = size - 10

    start = perf_counter()

    seed(1)
    trgt=Circle(Point(randint(-450,450),randint(-200,200)),size)
    trgt.setFill('red')
    trgt.draw(win)

    i=0
    while i<9:
        seed(i+2)
        if Compare(trgt.getCenter(),size,win.getMouse()):
            trgt.undraw()
            trgt.move(randint(-450,450),randint(-200,200))
            trgt.draw(win)
            i=i+1

    trgt.undraw()
                      
    stop = perf_counter()

    return (stop-start)

#verifica si el jugador quiere seguir jugando
def again(win):
    play=Button(win,Point(-45,0),80,20,'Continue')
    play.activate()
    stop=Button(win,Point(45,0),80,20,'Exit')
    stop.activate()

    p=win.getMouse()
    while True:
        if play.clicked(p):
            play.undraw()
            stop.undraw()
            return True
        elif stop.clicked(p):
            play.undraw()
            stop.undraw()
            return False

#muestra texto en pantalla
def info(win,style,text,size):
    t=Text(Point(0,0),text)
    t.setTextColor('red')
    t.setSize(size)
    t.setStyle(style)
    t.draw(win)
        
    ub=Button(win,Point(0,-150),80,20,'Userboard')
    ub.activate()

    b=Button(win,Point(0,-180),80,20,'Continue')
    b.activate()

    p=win.getMouse()
    while True:
        if b.clicked(p):
            t.undraw()
            b.undraw()
            ub.undraw()
            break
        elif ub.clicked(p):
            t.undraw()
            b.undraw()
            ub.undraw()
            user_board(win,style,text,size)
            break

#cambia el tamano de los circulos siempre que el jugador supere el tiempo
def Clilck_the_dots(win):
    better = False
    size = 50
    time=0.0
    tref=0.0
    agn=True
    while agn:
            time = Targets(better, size, win)
            if (tref > time) or (tref==0):
                size = size-5
                better = True
                tref = time
            else:
                better = False

            text=f'Your time was {time:.4}'
            info(win,'normal',text,15)
            
            agn=again(win)
            if size<=0:
                break
    return time

#muestra base de datos de jugadores con sus tiempos
def user_board(win,style,text,size):
    sort()
    f = open('user_board.txt','r')
    t=Text(Point(0,150),'User board')
    t.setSize(18)
    t.setStyle('bold')
    t.setTextColor('red')
    t.draw(win)

    lines=Text(Point(0,0),f.read(100))
    lines.draw(win)
    
    b=Button(win, Point(0,-180),80,20,"Go Back")
    b.activate()
    while True:
        if b.clicked(win.getMouse()):
            b.undraw()
            lines.undraw()
            t.undraw()
            f.close()
            info(win,style,text,size)
            break

#le pide al usuario un numbre para ingresar su tiempo
def add_score(win,time):
    inputUser=Entry(Point(0,-50),10)
    inputUser.draw(win)
    
    t=Text(Point(0,0),'Enter a 3 character username')
    t.setTextColor('red')
    t.draw(win)

    c=Button(win,Point(-50,-100),80,20,'Cancel')
    c.activate()

    e=Button(win,Point(50,-100),80,20,'Enter')
    e.activate()

    p=win.getMouse()
    while True:
        if e.clicked(p):
            u=inputUser.getText()               
            if len(u)<3:                        #asegurar que el username tenga 3 chars
                u=u+'   '
            user= u[:3]+f' {time:.4}\n'         #asegurar que no pase de 3
            f=open('user_board.txt','a')
            f.write(user)
            f.close()
            break
        elif c.clicked(p):
            break

    c.undraw()
    inputUser.undraw()
    t.undraw()
    e.undraw()
    sort()

#acomoda los usuarios desde el timepo mas corto al mayor
def sort():
    f=open('user_board.txt','r')
    lines=f.readlines()
    f.close()

    times=[]
    users=[]
    for i in lines:
        users.append(i[0:3])
        times.append(float(i[4:10]))
    dic={}
    for i in range(len(users)):
        dic[times[i]]=users[i]

    sortedDic= sorted(dic.items())

    f=open('user_board.txt','w')
    sortedContent=''
    for i in sortedDic:
        sortedContent= sortedContent + f'{i[1]} {i[0]:.4}\n'
    f.write(sortedContent)
    f.close()

def main():
    win=GraphWin("Click the dots", 1001, 501)
    win.setCoords(-500,-250,500,250)
    

    info(win,'bold',"Click the dots",18)


    instructions=''' -Objective is to click each target as fast as possible.
        -By the end of each round your time will be demostrated.
             -If you are able to beat your time, the targets will get smaller.'''
    info(win, 'normal',instructions,15)
    
    time= Clilck_the_dots(win)

    add_score(win,time)

    info(win,'normal','Thank you for playing',15)   
    win.close()

main()