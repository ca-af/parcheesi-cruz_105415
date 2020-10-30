"""
Programado por: Andy Cruz - 105415
29 de octubre de 2020
CECS3210 – 39 - SPRING-20
Prof. Edwin Flórez Gómez"""
import graphics
import random
from graphics import *

"""
EL Dice class es utilizado para identificar el numero que cae el
dice cuando el jugador lo enrolla.
"""
class Dice:
    """
    El roll función se utiliza para enrollar los dices con los
    valores del 1 al 7.
    """
    def roll(self, which):
        for pos in which:
            self.dice[pos] = random.randrange(1, 7)
    """
    El rollAll se utiliza para enrollar todos los dices.
    """
    def rollAll(self):
        self.roll(range(2))
    """
    El values función se utiliza para enseñar el valor de todos los
    dices.
    """
    def values(self):
        return self.dice[:]
    """
    El score función es utilizado para enseñar que tipo de score el usuario
    recibió dependiendo de los valores de los dices.
    """
    def score(self):
        counts = [0] * 7
        for value in self.dice:
            counts[value] = counts[value] + 1

        if counts.count(2) == 1:
            return "One Pair"

    def __init__(self):
        self.dice = [0]*2
        self.rollAll()
"""
El class button es utilizado para crear botones para el juego.
"""
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
    """
    El clicked function es utilizado para determinar si el botón fue
    dado o no.
    """
    def clicked(self, p):
        return self.active and \
               self.xmin <= p.getX() <= self.xmax and \
               self.ymin <= p.getY() <= self.ymax

    """
    El getLabel function es utilizado para adquirir el texto del botón
    """
    def getLabel(self):
        return self.label.getText()
    """
    El activate function es utilizado para activar un botón creado.
    """
    def activate(self):
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = 1
    """
    El deactivate function es utilizado para desactivar un botón activado.
    """
    def deactivate(self):
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = 0

"""
El Gameplay class es utilizado para empezar el juego con las piezas,
el board, y las reglas.
"""
class Gameplay:
    """
    El board function es utilizado para crear el window del juego
    acompañado con el board del juego.
    """
    def board(self):
        gameImage = Image(Point(280, 279), "parcheesi_board.png")
        gameImage.draw(self.win)
    """
    El player function es utilizado para crear todas las piezas para los
    jugadores.
    """
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

    """
    El movePLayer function es utilizado para determinar que tipo
    de acción haría la pieza del jugador dependiendo del valor
    de los dices.
    """
    def movePlayer(self, x, y):
        if (x == 5 and y == 5):
            self.playerA1.undraw()
            self.playerA1 = Circle(Point(338, 449), 10)
            self.playerA1.setFill("red")
            self.playerA1.draw(self.win)
        elif (x == 5 or y == 5):
            if (self.A1 == 0):
                self.A1 = 1
                self.playerA1.undraw()
                self.playerA1 = Circle(Point(338, 449), 10)
                self.playerA1.setFill("red")
                self.playerA1.draw(self.win)
            else:
                self.playerA1.move(0, -8*5)
    """
    El dices function dibuja los dices en el window del juego.
    """
    def dices(self):
        self.diceA = Rectangle(Point(212, 596), Point(260, 640))
        self.diceA.setFill("red")
        self.diceA.draw(self.win)

        self.diceB = self.diceA.clone()
        self.diceB.move(70, 0)
        self.diceB.draw(self.win)

        self.pickKey = Text(Point(275, 685),
                            "Hit the Roll Dice Button to roll the dice!")
        self.pickKey.draw(self.win)
    """
    El buttons function es utilizado para crear los botones para el juego con
    el Button class.
    """
    def buttons(self):

        self.rollDice = Button(self.win, Point(117, 622), 100, 100, "Roll Dice")
        self.rollDice.activate()

        self.exitButton = Button(self.win, Point(430, 620), 100, 100, "EXIT")
        self.exitButton.activate()
        """
        Verifica que tipo de valor tiene los dices cuando el usuario le da al
        "Roll Dice" button.
        """
        while(True):
            mouseClick = self.win.getMouse()

            if (self.rollDice.clicked(mouseClick)):
                self.dice.roll([0])
                self.dice.roll([1])
                return self.dice.values()
            elif (self.exitButton.clicked(mouseClick)):
                exit()
    """
    El game function es utilizado para dibujar los valores de los dices
    y verificar que tipo de acción haria el jugador con el movePlayer
    function.
    """
    def game(self):

        diceXText = Text(Point(240, 584), "Dice 1: ")
        diceXText.setFace("courier")
        diceXText.setSize(10)
        diceXText.draw(self.win)
        diceYText = Text(Point(310, 584), "Dice 2: ")
        diceYText.setFace("courier")
        diceYText.setSize(10)
        diceYText.draw(self.win)

        diceXTextNumber = Text(Point(235, 618), "0")
        diceXTextNumber.setFace("times roman")
        diceXTextNumber.setTextColor("white")
        diceXTextNumber.draw(self.win)

        diceYTextNumber = Text(Point(305, 618), "0")
        diceYTextNumber.setFace("times roman")
        diceYTextNumber.setTextColor("white")
        diceYTextNumber.draw(self.win)
        """
        Dibuja el valor del dice con el buttons función.
        """
        while (True):
                diceX, diceY = self.buttons()

                diceXTextNumber.undraw()
                diceXTextNumber = Text(Point(235, 618), diceX)
                diceXTextNumber.setFace("times roman")
                diceXTextNumber.setTextColor("white")
                diceXTextNumber.draw(self.win)

                diceYTextNumber.undraw()
                diceYTextNumber = Text(Point(305, 618), diceY)
                diceYTextNumber.setFace("times roman")
                diceYTextNumber.setTextColor("white")
                diceYTextNumber.draw(self.win)

                if (diceX == 5 or diceY == 5 or (diceX + diceY) == 10):
                    self.move = self.movePlayer(diceX, diceY)

    def __init__(self):
        self.win = GraphWin("Parcheesi", 560, 700)
        self.dice = Dice()
        self.board()
        self.player()
        self.dices()
        self.buttons()
        self.game()
"""
Gameplay object esta creado.
"""
def main():
    board = Gameplay()

"""
El main function esta llamado.
"""
if __name__ == "__main__":
    main()