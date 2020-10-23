#scoreboard.py
from graphics import *
from button import *

class Scoreboard:
    def __init__(self, win):
        self.win=win

    def add_score(self,time):
        inputUser=Entry(Point(0,-50),10)
        inputUser.draw(self.win)
        
        t=Text(Point(0,0),'Enter a 3 character username')
        t.setTextColor('red')
        t.draw(self.win)

        cancel=Button(self.win,Point(-50,-100),80,20,'Cancel')
        cancel.activate()

        enter=Button(self.win,Point(50,-100),80,20,'Enter')
        enter.activate()

        while True:
            p=self.win.getMouse()
            if enter.clicked(p):
                username=inputUser.getText()               
                if len(username)<3:                        #asegurar que el username tenga 3 chars
                    username=username+'   '
                user_info= username[:3]+f' {time:.4}\n'         #asegurar que no pase de 3
                f=open('user_board.txt','a')
                f.write(user_info)
                f.close()
                return True
            elif cancel.clicked(p):
                return False

    def show(self):
        self.sort()
        f = open('user_board.txt','r')
        t=Text(Point(0,150),'User board')
        t.setSize(18)
        t.setStyle('bold')
        t.setTextColor('red')
        t.draw(self.win)

        lines=Text(Point(0,0),f.read(100))
        lines.draw(self.win)
        
        back=Button(self.win, Point(0,-180),80,20,"Go Back")
        back.activate()
        p=self.win.getMouse()
        while True:
            if back.clicked(p):
                back.undraw()
                lines.undraw()
                t.undraw()
                f.close()
                break
    
    def sort(self):
        f=open('user_board.txt','r')
        lines=f.readlines()

        dic={}
        for user_info in lines:
            user=user_info.split()[0]
            time=user_info.split()[1]
            dic[float(time)]=user
            
        sortedDic= sorted(dic.items())

        f=open('user_board.txt','w')
        sortedContent=''
        for i in sortedDic:
            if len(i[1])<3:
                sortedContent=SortedContent + f'{i[1]}   {i[0]:.4}\n'
            else:
                sortedContent= sortedContent + f'{i[1]} {i[0]:.4}\n'
        f.write(sortedContent)
        f.close()