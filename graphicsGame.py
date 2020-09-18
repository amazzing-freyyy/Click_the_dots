from graphics import *
from random import seed
from random import randint
from time import perf_counter

#chequea si el click esta dentro del bounding box del circulo
def Compare(p1,p2,pM):
    if (p1.getX()<=pM.getX()<=p2.getX()) and (p1.getY()<=pM.getY()<=p2.getY()):
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
        p1=trgt.getP1()
        p2=trgt.getP2()
        if Compare(p1,p2,win.getMouse()):
            trgt.undraw()
            trgt.move(randint(-450,450),randint(-200,200))
            trgt.draw(win)
            i=i+1

    trgt.undraw()
                      
    stop = perf_counter()

    return (stop-start)

#verifica si el jugador quiere volver a jugar
def again(win):
    text=Text(Point(0,0),'Press enter to play again...')
    text.setTextColor('red')
    text.draw(win)

    if win.getKey()=='Return':
        text.undraw()
        return True
    else:
        text.undraw()
        return False

def main():
    win=GraphWin("Click the dots", 1001, 501)
    win.setCoords(-500,-250,500,250)
    win.setBackground('light gray')

    text=Text(Point(0,40),'Click the dots')
    text2=Text(Point(0,0),'Click to continue')
    text.setTextColor('red')
    text2.setTextColor('red')
    text.setSize(18)
    text.setStyle('bold')
    text.draw(win)
    text2.draw(win)

    win.getMouse()
    text.undraw()
    text2.undraw()
    
    better = False
    size = 100
    time=0.0
    tref=0.0
    agn=True
    while agn:
            #determina si el tiempo en el intento disminuyo
            #de ser asi disminuye el tamano de los circulos
            time = Targets(better, size, win)
            if (tref > time) or (tref==0):
                size = size-10
                better = True
                tref = time
            else:
                better = False

            text2.setText(f'Your time was {time}\nClick to continue')
            text2.draw(win)
            
            win.getMouse()
            text2.undraw()

            agn=again(win)
            if size<=0:
                agn=False

    text2.setText('Thank you for playing.\nClick to close')
    text2.draw(win)
    
    win.getMouse()
    text2.undraw()
        
    win.close()

main()
