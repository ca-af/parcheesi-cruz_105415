import graphics
import random
from graphics import *

class Dice:
    def roll(self, which):
        for pos in which:
            self.dice[pos] = random.randrange(1, 7)

    def rollAll(self):
        self.roll(range(2))

    def values(self):
        return self.dice[:]

    def score(self):
        counts = [0] * 7
        for value in self.dice:
            counts[value] = counts[value] + 1

        if counts.count(2) == 1:
            return "One Pair"

    def __init__(self):
        self.dice = [0]*2
        self.rollAll()

class Button:

    def __init__(self, win, center, width, height, label):

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        return self.active and \
               self.xmin <= p.getX() <= self.xmax and \
               self.ymin <= p.getY() <= self.ymax

    def getLabel(self):
        return self.label.getText()

    def activate(self):
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = 1

    def deactivate(self):
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = 0

class Gameplay:
    def board(self):
        flowerImage = Image(Point(280, 279), "parcheesi_board.png")
        flowerImage.draw(self.win)

    def player(self):
        self.playerA1 = Circle(Point(443, 452), 10)
        self.playerA1.setFill("red")
        self.playerA1.draw(self.win)
        self.A1 = 0

        self.playerA2 = self.playerA1.clone()
        self.playerA2.move(37, 0)
        self.playerA2.draw(self.win)
        self.A2 = 0

        self.playerA3 = self.playerA1.clone()
        self.playerA3.move(0, 37)
        self.playerA3.draw(self.win)
        self.A3 = 0

        self.playerA4 = self.playerA1.clone()
        self.playerA4.move(37, 37)
        self.playerA4.draw(self.win)
        self.A4 = 0

        self.playerB1 = Circle(Point(79, 446), 10)
        self.playerB1.setFill("blue")
        self.playerB1.draw(self.win)
        self.B1 = 0

        self.playerB2 = self.playerB1.clone()
        self.playerB2.move(37, 0)
        self.playerB2.draw(self.win)
        self.B2 = 0

        self.playerB3 = self.playerB1.clone()
        self.playerB3.move(0, 37)
        self.playerB3.draw(self.win)
        self.B3 = 0

        self.playerB4 = self.playerB1.clone()
        self.playerB4.move(37, 37)
        self.playerB4.draw(self.win)
        self.B4 = 0

        self.playerC1 = Circle(Point(77, 79), 10)
        self.playerC1.setFill("yellow")
        self.playerC1.draw(self.win)
        self.C1 = 0

        self.playerC2 = self.playerC1.clone()
        self.playerC2.move(37, 0)
        self.playerC2.draw(self.win)
        self.C2 = 0

        self.playerC3 = self.playerC1.clone()
        self.playerC3.move(0, 37)
        self.playerC3.draw(self.win)
        self.C3 = 0

        self.playerC4 = self.playerC1.clone()
        self.playerC4.move(37, 37)
        self.playerC4.draw(self.win)
        self.C4 = 0

        self.playerD1 = Circle(Point(444, 80), 10)
        self.playerD1.setFill("green")
        self.playerD1.draw(self.win)
        self.D1 = 0

        self.playerD2 = self.playerD1.clone()
        self.playerD2.move(37, 0)
        self.playerD2.draw(self.win)
        self.D2 = 0

        self.playerD3 = self.playerD1.clone()
        self.playerD3.move(0, 37)
        self.playerD3.draw(self.win)
        self.D3 = 0

        self.playerD4 = self.playerD1.clone()
        self.playerD4.move(37, 37)
        self.playerD4.draw(self.win)
        self.D4 = 0

    def buttons(self):
        self.rollDice = Button(self.win, Point(117, 622), 100, 100, "Roll Dice")
        self.rollDice.activate()

        self.exitButton = Button(self.win, Point(430, 620), 100, 100, "EXIT")
        self.exitButton.activate()

        while(True):
            mouseClick = self.win.getMouse()

            if (self.rollDice.clicked(mouseClick)):
                self.dice.roll([0])
                self.dice.roll([1])
                print(self.dice.values())
                return self.dice.values()
            elif (self.exitButton.clicked(mouseClick)):
                return 0
            else:
                continue

    def game(self):
        self.dice1 = Rectangle(Point(212, 596), Point(260, 640))
        self.dice1.setFill("red")
        self.dice1.draw(self.win)

        self.dice2 = self.dice1.clone()
        self.dice2.move(70, 0)
        self.dice2.draw(self.win)

        while (True):
            if (self.buttons() == 0):
                break
            else:
                self.x = self.buttons()

    def __init__(self):
        self.win = GraphWin("Parcheesi", 560, 700)
        self.dice = Dice()
        self.board()
        self.player()
        self.buttons()
        self.game()

def main():
    board = Gameplay()

if __name__ == "__main__":
    main()