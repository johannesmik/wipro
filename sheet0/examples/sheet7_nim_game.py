#!/usr/bin/python2.7 
from Tkinter import *
import tkMessageBox

class NimBoard(object):
    def __init__(self):
        self.matches = [[1 for i in range(j*2-1)] for j in range(1,5)]
        self.temp_removed = []
        self.current_row = -1

    def remove_match(self, i, j):
        """ Remove the match in the i-th row and the j-th column """
        if self.current_row == -1 or self.current_row == i:
            self.current_row = i
            if self.matches[i][j] != 0:
                self.matches[i][j] = 0
                return True

    def add_match(self, i, j):
        if self.matches[i][j] == 0:
            self.matches[i][j] = 1
            return True

    def remove_match_temp(self, i, j):
        """  Temporarily removes a match """
        if self.remove_match(i, j):
            self.temp_removed.append((i, j))

    def restore_match_temp(self):
        """ Restores temporary removed matches. """
        for i, j in self.temp_removed:
            self.add_match(i, j)
        self.temp_removed = []
        self.current_row = -1

    def submit(self, player="mensch"):
        """  Submit the current move. (temporary removed matches)
             Also look if the game is over
        """

        print player, ":", self.temp_removed
        if len(self.temp_removed) == 0:
            tkMessageBox.showinfo('Fehler!', 'Du musst mindestens ein Streicholz ziehen')
            return False

        self.temp_removed = []
        self.current_row = -1

        # Has the game ended?
        s = self.spaltensumme()
        if s[0] == 0 and s[1] == 0 and s[2] == 0:
            tkMessageBox.showinfo('Spielende', '%s hat verloren' % player)
            # Reinitialize board
            self.matches = [[1 for i in range(j*2-1)] for j in range(1,5)]
            return False
        return True

    def spaltensumme(self):
        """  Returns a list with 3 elements, in each is the Spaltensumme.
         Example from the exercise-sheet: [2,2,4]
         """
        spaltensumme = 0
        for i in range(4):
            zeile = self.int2bin(sum(self.matches[i]))
            spaltensumme += zeile
        string = "%03d" % spaltensumme
        return [int(string[0]), int(string[1]), int(string[2])]

    @staticmethod
    def int2bin(i):
        """ Example: 5 -> 0b0101 -> '0101' -> 101 """
        b = bin(i)
        bs = str(b)[2:]
        return int(bs)

    def winningCondition(self):
        """ Aktuell eine Gewinnformation?
            Entweder alle Glieder der Spaltensumme gerade,
            oder Spaltensumme = [0,0,1] oder [0,0,3]
        """
        s = self.spaltensumme()
        if s[0] == 0 and s[1] == 0:
            # Sonderfall: Uebrige muss 1 oder 3 sein
            if s[2] == 1 or s[2] == 3:
                return True
            else:
                return False
        else:
            # Alle Glieder der Spaltensumme gerade
            return s[0] % 2 == 0 and s[1] % 2 == 0 and s[2] % 2 == 0

    def cpu_draw(self):
        """ The cpu does one draw
            by testing all possible moves
        """
        # Test every row
        for i in range(4):
            for j in range((i+1)*2-1):
                self.remove_match_temp(i, j)
                if self.winningCondition():
                    self.submit("cpu")
                    return
            self.restore_match_temp()

class NimGui(object):
    def __init__(self, parent):
        self.parent = parent
        self.parent.title('Nim-Spiel ala Marienbad')
        self.board = NimBoard()
        self.frame = Frame(parent)
        self.frame.pack()
        self.setupButtons()
        self.refresh()
        self.board.cpu_draw()

    def setupButtons(self):
        """ Sets up the buttons """
        self.match_image = PhotoImage(file="match.gif")

        self.match_buttons = [[Button(self.frame, image=self.match_image) for j in range(i*2-1)] for i in range(1, 5)]
        for i in range(4):
            for j in range((i+1)*2-1):
                indent = 3-i
                self.match_buttons[i][j].grid(row=i, column=indent+j, ipadx=2, ipady=2, padx=20, pady=20)
                self.match_buttons[i][j].configure(command=lambda x=i, y=j: self.matchButtonClick(x, y))

        self.finish_button = Button(self.frame, text='Finish', command=self.finishButtonClick)
        self.finish_button.grid(row=4, column=2)

        self.resetmove_button = Button(self.frame, text='Reset\nMove', command=self.resetmoveButtonClick)
        self.resetmove_button.grid(row=4, column=3)

        self.reset_button = Button(self.frame, text='Reset', command=self.resetButtonClick)
        self.reset_button.grid(row=4, column=4)

    def matchButtonClick(self, i, j):
        self.board.remove_match_temp(i, j)
        self.refresh()

    def finishButtonClick(self):
        if self.board.submit("Johannes"):
            self.board.cpu_draw()
        self.refresh()

    def resetmoveButtonClick(self):
        self.board.restore_match_temp()
        self.refresh()

    def resetButtonClick(self):
        self.board = NimBoard()
        self.refresh()

    def refresh(self):
        """ Refreshes the display of the matches """
        for i in range(4):
            for j in range((i+1)*2-1):
                if self.board.matches[i][j] == 1:
                    self.match_buttons[i][j].configure(relief=RAISED, state=NORMAL)
                else:
                    self.match_buttons[i][j].configure(relief=SUNKEN, state=DISABLED)

root = Tk()
nimboard = NimGui(root)
root.mainloop()