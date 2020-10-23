#target.py
from graphics import *
from button import *
from scoreboard import *
from random import seed
from random import randint
from time import perf_counter
from button import *
from math import sqrt

class Clilck_the_dots:

    def __init__(self):
        self.win=GraphWin("Click the dots", 1001, 501)
        self.win.setCoords(-500,-250,500,250)


    # muestra circulos en pantalla
    def Targets(self,better,size):
        if better:
            size =size - 10

        start = perf_counter()

        seed(1)
        trgt=Circle(Point(randint(-450,450),randint(-200,200)),size)
        trgt.setFill('red')
        trgt.draw(self.win)

        i=0
        while i<9:
            seed(i+2)
            if self.Compare(trgt.getCenter(),self.win.getMouse(),size):
                trgt.undraw()
                trgt.move(randint(-450,450),randint(-200,200))
                trgt.draw(self.win)
                i=i+1

        trgt.undraw()
                        
        stop = perf_counter()

        return (stop-start)

    #Chequea si el usuario le dio click al circulo
    def Compare(self,c,pM,size):
        r = sqrt((c.getX()-pM.getX())**2+(c.getY()-pM.getY())**2)

        if r<=size:
            return True
        else:
            return False

    #Cambia el tamano de los circulos cuando el jugador supere su tiempo
    #retorna el tiempo del jugador
    def gameplay(self):
        better = False
        size = 50
        tref=0.0
        agn=True
        while agn:
            time = self.Targets(better,size)
            if (tref > time):
                size = size-5
                better = True
                tref = time

            if self.display_text(time):
                break
            elif size<=0:
                break
        return time
    
    #hace el display entre cada juego
    def display_text(self, time):
        t=Text(Point(0,0),f'Your time was {time:.4}')
        t.setTextColor('red')
        t.setSize(15)
        t.draw(self.win)

        scoreboard=Button(self.win,Point(0,-150),80,20,'Scoreboard')
        scoreboard.activate()

        play_again=Button(self.win,Point(-45,-180),80,20,'Continue')
        play_again.activate()

        exit_game=Button(self.win,Point(45,-180),80,20,'Exit')
        exit_game.activate()

        sb=Scoreboard(self.win)
        while True:
            p=self.win.getMouse()
            if scoreboard.clicked(p):          #muestra scoreboard
                t.undraw()                     #cuando sale del scoreboard vuelve al menu
                scoreboard.undraw()
                play_again.undraw()
                exit_game.undraw()
                sb.show()
                t.draw(self.win)
                scoreboard.draw(self.win)
                play_again.draw(self.win)
                exit_game.draw(self.win)

            elif play_again.clicked(p):
                t.undraw()
                scoreboard.undraw()
                play_again.undraw()
                exit_game.undraw()
                return False

            elif exit_game.clicked(p):
                t.undraw()
                scoreboard.undraw()
                play_again.undraw()
                exit_game.undraw()
                return True

    #hace el display del intro screen
    def intro(self):
        title=Text(Point(0,180),'Click the dots')
        title.setTextColor('red')
        title.setSize(18)
        title.setStyle('bold')
        title.draw(self.win)

        objectives=''' -Objective is to click each target as fast as possible.
        -By the end of each round your time will be demostrated.
             -If you are able to beat your time, the targets will get smaller.'''
        instructions=Text(Point(0,0),objectives)
        instructions.setTextColor('red')
        instructions.setSize(15)
        instructions.draw(self.win)

        start_game=Button(self.win,Point(0,-180),80,20,'Start')
        start_game.activate()
        
        scoreboard=Button(self.win,Point(0,-150),80,20,'Scoreboard')
        scoreboard.activate()

        sb=Scoreboard(self.win)
        while True:
            p=self.win.getMouse()
            if start_game.clicked(p):
                start_game.undraw()
                scoreboard.undraw()
                title.undraw()
                instructions.undraw()
                break
            elif scoreboard.clicked(p):
                title.undraw()
                start_game.undraw()
                scoreboard.undraw()
                instructions.undraw()
                sb.show()
                title.draw(self.win)
                scoreboard.draw(self.win)
                start_game.draw(self.win)
                instructions.draw(self.win)

    #hace el display del outro screen
    def outro(self,time):
        t=Text(Point(0,0),'Thank you for playing')
        t.setTextColor('red')
        t.setSize(15)
        t.draw(self.win)

        close_game=Button(self.win,Point(0,-180),80,20,'Close')
        close_game.activate()

        scoreboard=Button(self.win,Point(-45,-150),80,20,'Scoreboard')
        scoreboard.activate()

        add_score=Button(self.win,Point(45,-150),80,20,'Add Score')
        add_score.activate()

        sb=Scoreboard(self.win)
        p=self.win.getMouse()
        while True:
            if close_game.clicked(p):
                close_game.undraw()
                scoreboard.undraw()
                add_score.undraw()
                t.undraw()
                break
            elif scoreboard.clicked(p):
                close_game.undraw()
                scoreboard.undraw()
                add_score.undraw()
                t.undraw()
                sb.show()
                close_game.draw(self.win)
                scoreboard.draw(self.win)
                add_score.draw(self.win)
                t.draw(self.win)
            elif add_score.clicked(p):
                close_game.undraw()
                scoreboard.undraw()
                add_score.undraw()
                t.undraw()
                sb.add_score(time)
                close_game.draw(self.win)
                scoreboard.draw(self.win)
                add_score.draw(self.win)
                t.draw(self.win)
                break