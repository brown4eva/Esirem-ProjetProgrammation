
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import random as random
import pygame
import sys
import math


class ColorsTerminal:
    Black = "\033[30m"
    Red = "\033[31m"
    Green = "\033[32m"
    Yellow = "\033[33m"
    Blue = "\033[34m"
    Magenta =  "\033[35m"
    LightGray = "\033[37m"
    DarkGray = "\033[90m"
    LightRed = "\033[91m"
    LightGreen = "\033[92m"
    LightYellow = "\033[93m"
    LightBlue = "\033[94m"
    LightMagenta = "\033[95m"
    LightCyan = "\033[96m"
    White = "\033[97m"

class ColorsRGB:
    Black = (0,0,0)
    Red = (255,0,0)
    Green = (0,255,0)
    Yellow = (255,255,0)
    Blue = (0,0,255)
    Cyan = (0, 255, 255)
    Magenta =  (255,0,255)
    White = (255,255,255)

class Joueur:
    def __init__(self, name="A", symbole="*", colorTerminal=ColorsTerminal.Green, colorUI=ColorsRGB.Green):
        self.symbole = symbole
        self.name = name
        self.colorTerminal = colorTerminal
        self.colorUI = colorUI
        self.numberOfVictory = 0


class Puissance4:
    def __init__(self):
        self.joueurA = Joueur("A", "*", ColorsTerminal.Red, colorUI=ColorsRGB.Red)
        self.joueurB = Joueur("B", "&", ColorsTerminal.Yellow, colorUI=ColorsRGB.Yellow)
        self.board = Board((7,6),
                           {
                               self.joueurA.symbole: self.joueurA.colorTerminal,
                               self.joueurB.symbole: self.joueurB.colorTerminal
                           }) #Creation d'un tableau de 8x8
        self._squarePixel = 100
        self._width = self.board.size[0] * self._squarePixel
        self._height = (self.board.size[1] + 1) * self._squarePixel
        self._radius = int(self._squarePixel / 2 - 5)
        pygame.init()
        self.font = pygame.font.SysFont('arial', 50)

    def startGame(self):
        while(True):
            self.board.clear()
            self.createWindows()
            self.game()
            self.closeGame()
            if(input("Tappez N pour rejouer") != "N"):
                break


    def inputValidValue(self):
        while True:
            value = input('Value between 0 and 6:\n')
            try:
                value = int(value)
            except ValueError:
                print('Not integer value')
                continue
            if 0 <= value < 7 and not self.board.fullColumn(value):
                break
            else:
                print("Invalid value")
        return value

    def game(self):
        gameOver = False
        if random.random() > 0.5:
            joueur = self.joueurA
        else:
            joueur = self.joueurB
        while(not gameOver):
            #idx = self.inputValidValue()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self.window, ColorsRGB.Black, (0, 0, self._width, self._squarePixel))
                    posx = event.pos[0]
                    pygame.draw.circle(self.window, joueur.colorUI, (posx, int(self._squarePixel / 2)), self._radius)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(self.window, ColorsRGB.Black, (0, 0, self._width, self._squarePixel))
                    posx = event.pos[0]
                    idx = int(math.floor(posx / self._squarePixel))
                    self.board.fullColumn(idx)
                    row = self.setTokenBoard(idx, joueur.symbole)
                    print(self.board)
                    if self.alignToken((row, idx),joueur.symbole) >= 4:
                        joueur.numberOfVictory += 1
                        label = self.font.render(str(self.joueurA.numberOfVictory) + " - " + str(self.joueurB.numberOfVictory), 1, joueur.colorUI)
                        self.window.blit(label, (int(self._width/2 - 35), 10))
                        print("Le joueur " + joueur.name + " a gagné!")
                        gameOver = True
                    else:
                        gameOver = True
                        for i in range(self.board.size[1]):
                            if not self.board.fullColumn(i):
                                gameOver = False
                        if joueur == self.joueurA:
                            joueur = self.joueurB
                        else:
                            joueur = self.joueurA

            self.updateBoard()

    def createWindows(self):
        pixelSize = (self._width, self._height)
        self.window = pygame.display.set_mode(pixelSize)

    def closeGame(self):
        pygame.time.wait(3000)

    def drawBoard(self):
        if self.window == None:
            print("Error window")
            return
        pygame.draw.rect(self.window, ColorsRGB.Blue, (0, self._squarePixel, self._width,self._height))
        for col in range(self.board.size[0]):
            for row in range(self.board.size[1]):
                if self.board[row,col] == self.joueurA.symbole:
                    pygame.draw.circle(self.window, self.joueurA.colorUI, (
                    int(col * self._squarePixel + self._squarePixel / 2), int(row * self._squarePixel + self._squarePixel + self._squarePixel / 2)), self._radius)
                elif self.board[row,col] == self.joueurB.symbole:
                    pygame.draw.circle(self.window, self.joueurB.colorUI, (
                    int(col * self._squarePixel + self._squarePixel / 2), int(row * self._squarePixel + self._squarePixel + self._squarePixel / 2)), self._radius)
                else:
                    pygame.draw.circle(self.window, ColorsRGB.Black, (
                    int(col * self._squarePixel + self._squarePixel / 2), int(row * self._squarePixel + self._squarePixel + self._squarePixel / 2)), self._radius)

    def updateBoard(self):
        self.drawBoard()
        pygame.display.update()

    def drawScore(self):
        print("Joueur " + self.joueurA.name + ":"+ str(self.joueurA.numberOfVictory))
        print("- Joueur " + self.joueurB.name + ":"+ str(self.joueurB.numberOfVictory))


    def setTokenBoard(self, idx, symbol):
        row = self.board.size[1] - 1
        while self.board[(row,idx)] != ".":
            row -= 1
        self.board[(row, idx)] = symbol
        return row

    def numberTokenDir(self, position, dir,symbol):
        count = 1
        row = position[0] + dir[0]
        col = position[1] + dir[1]
        while row < self.board.size[1] and col < self.board.size[0]  and row >= 0 and col >= 0 and self.board[(row,col)] == symbol:
            count = count + 1
            row = row + dir[0]
            col = col + dir[1]

        row = position[0] - dir[0]
        col = position[1] - dir[1]
        while row >= 0 and col >= 0 and row < self.board.size[1] and col < self.board.size[0] and self.board[(row, col)] == symbol:
            count = count + 1
            row = row - dir[0]
            col = col - dir[1]
        return count

    def alignToken(self, position, symbol):
        numToken = self.numberTokenDir(position, (1,0), symbol)
        numToken = max(numToken, self.numberTokenDir(position, (1, 1), symbol))
        numToken = max(numToken, self.numberTokenDir(position, (0, 1), symbol))
        numToken = max(numToken, self.numberTokenDir(position, (1, -1), symbol))
        return numToken


class Board:
    def __init__(self, size, symcolor=None):
        if symcolor is None:
            symcolor = {"*": ColorsTerminal.Red, "&": ColorsTerminal.Green}
        self.size = size
        self.window = None
        self._board = [["." for _ in range(size[0])] for _ in range(size[1])]
        self.symcolor = symcolor

    def clear(self):
        self._board = [["." for _ in range(self.size[0])] for _ in range(self.size[1])]

    def fullColumn(self, idx):
        if self._board[0][idx] != '.':
            return True
        else:
            return False

    def __getitem__(self, position):
        return self._board[position[0]][position[1]]

    def __setitem__(self, position, value):
        self._board[position[0]][position[1]] = str(value)


    def __repr__(self):
        board = ""
        for i in range(self.size[1]):
            for j in range(self.size[0]):
                if self._board[i][j][0] in self.symcolor:
                    board += self.symcolor[self._board[i][j]] + self._board[i][j] + " " + '\033[0m'
                else:
                    board += self._board[i][j] + " "
            board += "\n"
        return board

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = Puissance4()
    a.startGame()
    a.drawScore()
