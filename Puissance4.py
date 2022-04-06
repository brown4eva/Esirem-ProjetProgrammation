import pygame
import sys

class Joueur :
    ...

class Board :
    def __init__ ( self , size ):
        self.size = size
        self.board = None
    def clear ( self ):
        ...
    def fullColumn ( self , idx ):
        if self.board [ 0 ][ idx ] != '.':
            return True
        else:
            return False
    def __repr__ ( self ):
        return ...


class Puissance4:
    def __init__ ( self ):
        self.joueurA = ...
        self.joueurB = ...
        self.board = ...

    def startGame ( self ):
        while ( True ):
            self.board.clear()
            self.game()
            if ( input ( " Tappez N pour rejouer " ) != " N " ):
                break

    # Entree clavier d ’ un entier entre 0 - 6
    def inputValidValue ( self ):
        while True :
            value = input ("Value between 0 and 6:\ n")
            # Si le caractere n ’ est pas un entier lever une exception
            try:
                value = int(value)
            except ValueError :
                print ( "Not integer value")
                continue
            if 0 <= value < 7 and not self . board . fullColumn ( value ):
                break
            else :
                print ("Invalid value ")
        return value

    # Gestion du jeu
    def game ( self ):
        gameOver = False
        joueur = self.joueurA # Le JoueurA debute la partie
        while ( not gameOver ):
            # Index de la colonne entree par le joueur
            idx = self . inputValidValue ()
            # Verification si 4 jetons sont alignes
                # Si oui le joueur a gagne
                # Mise a jour du compteur de victoire
                    # Fin de partie
                # Sinon verifier si la grille est complete
                    # Si oui Fin de partie
                # Sinon changement de joueur


        # Met un Jeton au nom de joueur sur
        # la ligne la plus basse la colonne Idx
        # Retourne l ’ index de la ligne
        def setTokenBoard ( self , idx , name ):
            ...
            return row # Index de la ligne

        # Retourne le maximum de jeton aligne parmi une direction
        # Position est un tuple tel que ( Ligne , Col )
        def numberTokenDir(self, position, dir, symbol):
            count = 1
            row = position[0] + dir[0]
            col = position[1] + dir[1]
            while row < self.board.size[1] and col < self.board.size[0] and row >= 0 and col >= 0 and self.board[
                (row, col)] == symbol:
                count = count + 1
                row = row + dir[0]
                col = col + dir[1]
            # Sens inverse
            row = position[0] - dir[0]
            col = position[1] - dir[1]
            while row >= 0 and col >= 0 and row < self.board.size[1] and col < self.board.size[0] and self.board[
                (row, col)] == symbol:
                count = count + 1
                row = row - dir[0]
                col = col - dir[1]
            return count

        # Retourne le maximum de jeton aligne
        def alignToken ( self , position , name ):
            numToken = self . numberTokenDir ( position , ( 1 ,0 ) , name )
            ...
            return numToken

        '''
        def game(self):
            gameOver = False

            joueur = self.joueurA  # Le JoueurA debute la partie
            while (not gameOver):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    # Si la souris est en mouvement
                    if event.type == pygame.MOUSEMOTION:
                        # Affichage du rectangle noir superieur
                        pygame.draw.rect(...)
                        # Position de la souris en X
                        posx = event.pos[0]
                        # Afficher un jeton a la position de la souris
                        pygame.draw.circle(...)
                    # Si le bouton de la souris est presse
                        # Position de la souris en X
                        posx = event.pos[0]
                        # Calcul de l ’ index de la colonne en fonction la position
                        # de la souris
                        idx = ...
                        # Verification si 4 jetons sont alignes
                            # Si oui le joueur a gagne
                            # Mise a jour du compteur de victoire
                                # Fin de partie
                            # Sinon verifier si la grille est complete
                                # Si oui Fin de partie
                            # Sinon changement de joueur
                    self.drawBoard()
                    pygame.display.update()
        '''
