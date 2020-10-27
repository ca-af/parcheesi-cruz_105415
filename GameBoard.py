import graphics
from graphics import *

class Board:
    def board(self):
        flowerImage = Image(Point(280, 279), "parcheesi_board.png")
        flowerImage.draw(self.win)

    def player(self):
        self.playerA1 = Circle(Point(443, 452), 10)
        self.playerA1.setFill("red")
        self.playerA1.draw(self.win)

        self.playerA2 = self.playerA1.clone()
        self.playerA2.move(37, 0)
        self.playerA2.draw(self.win)

        self.playerA3 = self.playerA1.clone()
        self.playerA3.move(0, 37)
        self.playerA3.draw(self.win)

        self.playerA4 = self.playerA1.clone()
        self.playerA4.move(37, 37)
        self.playerA4.draw(self.win)

        self.playerB1 = Circle(Point(79, 446), 10)
        self.playerB1.setFill("blue")
        self.playerB1.draw(self.win)

        self.playerB2 = self.playerB1.clone()
        self.playerB2.move(37, 0)
        self.playerB2.draw(self.win)

        self.playerB3 = self.playerB1.clone()
        self.playerB3.move(0, 37)
        self.playerB3.draw(self.win)

        self.playerB4 = self.playerB1.clone()
        self.playerB4.move(37, 37)
        self.playerB4.draw(self.win)

        self.playerC1 = Circle(Point(77, 79), 10)
        self.playerC1.setFill("yellow")
        self.playerC1.draw(self.win)

        self.playerC2 = self.playerC1.clone()
        self.playerC2.move(37, 0)
        self.playerC2.draw(self.win)

        self.playerC3 = self.playerC1.clone()
        self.playerC3.move(0, 37)
        self.playerC3.draw(self.win)

        self.playerC4 = self.playerC1.clone()
        self.playerC4.move(37, 37)
        self.playerC4.draw(self.win)

        self.playerD1 = Circle(Point(444, 80), 10)
        self.playerD1.setFill("green")
        self.playerD1.draw(self.win)

        self.playerD2 = self.playerD1.clone()
        self.playerD2.move(37, 0)
        self.playerD2.draw(self.win)

        self.playerD3 = self.playerD1.clone()
        self.playerD3.move(0, 37)
        self.playerD3.draw(self.win)

        self.playerD4 = self.playerD1.clone()
        self.playerD4.move(37, 37)
        self.playerD4.draw(self.win)

    def dice(self):


        self.x = self.win.getMouse()
        print(self.x)

    def __init__(self):
        self.win = GraphWin("Parcheesi", 560, 562)
        self.board()
        self.player()
        self.win.getMouse()
        self.win.close()

def main():
    board = Board()

if __name__ == "__main__":
    main()