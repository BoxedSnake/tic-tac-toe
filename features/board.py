class Board():
    #class name for the Tic tac toe grid
    def __init__(self):
        self.mark = [' ',' ',' ',' ',' ',' ',' ',' ',' '] # this list is for the board where user will input data
        self.new = [' ',' ',' ',' ',' ',' ',' ',' ',' ']  #placeholder for new game, clean slate
        self.key = ['1','2','3','4','5','6','7','8','9'] #key is for what button the user has to press to input value
        self.win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8)) #all winning combos
        self.end = False #just to define variable to stop a loop in main.py.
        
    def display(self): #method to pull up the game board
        print(
f'''
 {self.mark[6]} | {self.mark[7]} | {self.mark[8]} 
---|---|---
 {self.mark[3]} | {self.mark[4]} | {self.mark[5]} 
---|---|---
 {self.mark[0]} | {self.mark[1]} | {self.mark[2]} 
''') #displays the game board in a grid

    def showkey(self): #method to pull up the help key
        print(
f'''
 {self.key[6]} | {self.key[7]} | {self.key[8]} 
---|---|---
 {self.key[3]} | {self.key[4]} | {self.key[5]} 
---|---|---
 {self.key[0]} | {self.key[1]} | {self.key[2]} 
''') #prints the help key in the grid to show what you need to press

    def game(self,side): # method to determine winner
        for a in self.win:
            if self.mark[a[0]] == self.mark[a[1]] == self.mark[a[2]] == side:
                print (f"{side} is the winner.")
                self.end = True
                return
            # a for loop to match the piece(side) in player class to see if it
            # matches each tuple in the list for the game winning combo.
            #variable to return true to define variable in main. will
            #allows main.py loop for winner to stop
