from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
from random import randint

#   this is going to be the main class for Tic Tac Toe Game
#   All the objects will be inside the class
class TicTacToe:
    def __init__(self):
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.vsAI = False
        self.currentPlayer = "Player 1"
        self.currentTurn = 0
        self.p1 = []
        self.p2 = []
        self.ai = []
        self.root = Tk()
        self.main = ""
        self.gamePage = ""
        self.gamePad = {}
        self.movedTics = []
        self.lblDispTurn = ""
        self.initializeGraphics()

#   Method to set basic properties of the TKINTER Window
    def initializeGraphics(self):
        # self.root.geometry("270x110+500+300") #Define the size of the window of TKINTER
        self.root.title("Tic Tac Toe")
        self.homePage()

#   Method to define Main page of the Game
    def homePage(self):
        self.root.geometry("270x110+500+300")
        self.main = LabelFrame(self.root, text="Welcome")
        self.main.grid(row=0, columnspan=7, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)
        Label(self.main, text="Select an Opponent to begin", font="Arial 8 italic").grid(row=0, sticky='E', padx=5, pady=2)
        Button(self.main, text="vs AI", width=10, activebackground="red", command=self.playWithAI).grid(row=3, column=0, sticky=W, pady=4, padx=5)
        Button(self.main, text="vs Player", width=10, activebackground="green", command=self.playVS).grid(row=3, column=2, sticky=W, pady=4,padx=5)

    def createGamePad(self):
        self.currentTurn = 0
        self.currentPlayer = "Player 1"
        self.p1 = []
        self.p2 = []
        self.ai = []
        self.movedTics = []
        self.root.geometry("450x225+500+300")
        txt = "VS AI" if self.vsAI == True else "Player 1 vs Player 2"
        self.gamePage = LabelFrame(self.root, text=txt)
        self.gamePage.grid(row=3, columnspan=36, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)
        Button(self.gamePage, text="HOME", width=10, activebackground="blue", command=self.goHome).grid(row=3, column=2,sticky=W,pady=4,padx=5)
        self.lblDispTurn = Label(self.gamePage, text=" ", font="Arial 8 italic").grid(row=4, sticky='E', ipadx=5, ipady=5)
        self.createMatrix()

    def createMatrix(self):
        self.root.title("Tic Tac Toe: Player 1's Turn")
        self.gamePad[11] = ttk.Button(self.gamePage, text="")
        self.gamePad[11].grid(row=7, column=5, sticky='nsew', ipadx=5, ipady=5)
        self.gamePad[11].config(command=lambda: self.btnClick(11))

        self.gamePad[12] = ttk.Button(self.gamePage, text="")
        self.gamePad[12].grid(row=7, column=10, sticky='nsew', ipadx=5, ipady=5)
        self.gamePad[12].config(command=lambda: self.btnClick(12))

        self.gamePad[13] = ttk.Button(self.gamePage, text="")
        self.gamePad[13].grid(row=7, column=15, sticky='nsew', ipadx=5, ipady=5)
        self.gamePad[13].config(command=lambda: self.btnClick(13))

        self.gamePad[21] = ttk.Button(self.gamePage, text="")
        self.gamePad[21].grid(row=12, column=5, sticky='nsew', ipadx=5, ipady=5)
        self.gamePad[21].config(command=lambda: self.btnClick(21))

        self.gamePad[22] = ttk.Button(self.gamePage, text="")
        self.gamePad[22].grid(row=12, column=10, sticky='nsew', ipadx=5, ipady=5)
        self.gamePad[22].config(command=lambda: self.btnClick(22))

        self.gamePad[23] = ttk.Button(self.gamePage, text="")
        self.gamePad[23].grid(row=12, column=15, sticky='nsew', ipadx=5, ipady=5)
        self.gamePad[23].config(command=lambda: self.btnClick(23))

        self.gamePad[31] = ttk.Button(self.gamePage, text="")
        self.gamePad[31].grid(row=17, column=5, sticky='nsew', ipadx=5, ipady=5)
        self.gamePad[31].config(command=lambda: self.btnClick(31))

        self.gamePad[32] = ttk.Button(self.gamePage, text="")
        self.gamePad[32].grid(row=17, column=10, sticky='nsew', ipadx=5, ipady=5)
        self.gamePad[32].config(command=lambda: self.btnClick(32))

        self.gamePad[33] = ttk.Button(self.gamePage, text="")
        self.gamePad[33].grid(row=17, column=15, sticky='nsew', ipadx=5, ipady=5)
        self.gamePad[33].config(command=lambda: self.btnClick(33))

    def btnClick(self, id):
        self.currentTurn += 1
        self.movedTics.append(id)
        if(self.currentPlayer == "Player 1"):
            self.setLayout(id, 'X')
            self.p1.append(id)
            self.checkWinner(self.p1, self.currentPlayer)
            if self.vsAI == True:
                self.currentPlayer = "AI"
                self.root.title("Tic Tac Toe: AI's Turn")
                time.sleep(2)
                self.movesForAI()
            else:
                self.currentPlayer = "Player 2"
                self.root.title("Tic Tac Toe: Player 2's Turn")
        elif(self.currentPlayer=="Player 2"):
            self.setLayout(id, 'O')
            self.p2.append(id)
            self.checkWinner(self.p2, self.currentPlayer)
            self.currentPlayer = "Player 1"
            self.root.title("Tic Tac Toe: Player 1's Turn")
        # elif(self.currentPlayer=="AI" and self.vsAI==True):
            # self.setLayout(id, 'A')
            # self.ai.append(id)
            # self.checkWinner(self.ai, self.currentPlayer)
            # self.currentPlayer = "Player 1"
            # self.root.title("Tic Tac Toe: Player 1's Turn")
            # print("AI: {}".format(self.ai))

        if (self.currentTurn >= 9):
            ms = messagebox.askquestion(title="Tie: Game Over", message="Have another round?")
            print(ms)
            self.goHome() if ms == 'no' else self.createGamePad()

    def movesForAI(self):
        allMoves = {
            1:11, 2:12, 3:13,
            4:21, 5:22, 6:23,
            7:31, 8:32, 9:33
        }
        aiMoved = False
        while aiMoved != True:
            ranNum = randint(1, 9)
            if allMoves[ranNum] in self.movedTics:
                continue
            aiMoved = True
            self.setLayout(allMoves[ranNum], 'A')
            self.ai.append(allMoves[ranNum])
            self.movedTics.append(allMoves[ranNum])
            self.checkWinner(self.ai, self.currentPlayer)
            self.currentPlayer = "Player 1"
            self.root.title("Tic Tac Toe: Player 1's Turn")

    def checkWinner(self, movesList, player):
        movesList.sort()
        if (list(filter(lambda x: x in [11, 12, 13], movesList)) == [11, 12, 13]):
            ms = messagebox.askquestion(title="{} Won.".format(player),message="Have another round?")
        elif (list(filter(lambda x: x in [21, 22, 23], movesList)) == [21, 22, 23]):
            ms = messagebox.askquestion(title="{} Won.".format(player),message="Have another round?")
        elif (list(filter(lambda x: x in [31, 32, 33], movesList)) == [31, 32, 33]):
            ms = messagebox.askquestion(title="{} Won.".format(player),message="Have another round?")
        elif (list(filter(lambda x: x in [11, 21, 31], movesList)) == [11, 21, 31]):
            ms = messagebox.askquestion(title="{} Won.".format(player),message="Have another round?")
        elif (list(filter(lambda x: x in [12, 22, 32], movesList)) == [12, 22, 32]):
            ms = messagebox.askquestion(title="{} Won.".format(player),message="Have another round?")
        elif (list(filter(lambda x: x in [13, 23, 33], movesList)) == [13, 23, 33]):
            ms = messagebox.askquestion(title="{} Won.".format(player),message="Have another round?")
        elif (list(filter(lambda x: x in [11, 22, 33], movesList)) == [11, 22, 33]):
            ms = messagebox.askquestion(title="{} Won.".format(player),message="Have another round?")
        elif (list(filter(lambda x: x in [13, 22, 31], movesList)) == [13, 22, 31]):
            ms = messagebox.askquestion(title="{} Won.".format(player),message="Have another round?")
        else:
            ms = "Continue"

        if ms == 'no':
            self.goHome()
        elif ms == 'yes':
            self.createGamePad()

    def setLayout(self, id, playerSymbol):
        self.gamePad[id].config(text=playerSymbol)
        self.gamePad[id].state(['disabled'])
        self.movedTics.append(id)

    def playWithAI(self):
        self.main.grid_forget()
        self.vsAI = True
        self.createGamePad()

    def playVS(self):
        self.main.grid_forget()
        self.vsAI = False
        self.createGamePad()

    def goHome(self):
        self.gamePage.grid_forget()
        self.root.title("Tic Tac Toe: New Game")
        self.currentTurn = 0
        self.currentPlayer = "Player 1"
        self.p1 = []
        self.p2 = []
        self.ai = []
        self.movedTics = []
        self.homePage()


    def getPlayer1(self):
        pass

    def getPlayer2(self):
        pass

    def setPlayer1(self):
        pass

    def setPlayer2(self):
        pass

    def startGame(self):
        pass


#   call the method to start the game.
#   If the python program in getting executed directly then only the game would start
if __name__ == "__main__":
    objTicTacToe = TicTacToe() #Call Class method -> Start Game
    objTicTacToe.root.mainloop()