import random
class Player: #class for the players
    def __init__(self,name):
        self.name=name #user display name, will be defined by the user
        self.piece = None 
        self.human = False
        self.select= None
        #Variables are empty so the class can still run at startup
        #select is just a holder for user input

    def side(self,name=None,piece=None): #has a default of none to allow the program to run
        if piece == "X":
            self.piece = "O"
            print (f"{name} is already {piece}\n{self.name} will be {self.piece}")
        elif piece == "O":
            self.piece = "X"
            print (f"{name} is already {piece}\n{self.name} will be {self.piece}")            
        #statement to default pieces if other object has already selected.
            
        while self.piece not in["X","O"]: # when the user hasn't chosen a piece this will run
            choice = str(input ( f"{self.name}\nPick a Token:\n[1] X\n[2] O\n")or "1").upper()
            if choice == "1":
                self.piece = "X"
            elif choice == "2":
                self.piece = "O"                
            else:
                print ("Wrong option, Please try again.")
        #used list in the while loop so I don't have to us raise and exceptions.

    def cpu(self):
        while  type(self.human) == bool:
        #used type and bool so it'll always run and also don't need to define another variable for loop pass.
            cpu1= input(f"is {self.name} a:\n[1] Human\n[2] Computer\n")
            if cpu1 == "1":
                self.human = True
                print (f"{self.name} is now a Human.")
                return
            elif cpu1== "2":
                self.human = False
                print (f"{self.name} is now a Computer.")
                return
            else:
                print ("Please select the correct choice.")


    def action(self,mapper):
        while True:
            if self.human is True:
               self.select =(input(f"{self.name}\nWhere do you want to place your {self.piece}?\n"))
               right_num = ['1','2','3','4','5','6','7','8','9']
               #used list and string so else statement will cover int and str value

               while self.select not in right_num:
                  if self.select in right_num:
                       continue
                  else:
                      print ("Input value is wrong, please try again.")
                      self.select = input ("Please choose a number betweem 1 and 9?\n")
                      
               self.select = int(self.select)-1
               # the -1 is needed to convert from basic to programming
               # convert the value input from str to int
               
               
            elif self.human is False:
                 self.select = random.randint(1,9)-1
                 #very basic AI, could be better.
                 
            if mapper[self.select] != (' '):
                if self.human is True:
                   print ("Tile Occupied, Please try again.") # if the Human player picks a filled spot this will run
                   # AI won't need this so it'll just loop the action method.
                   
            else:
                              
                mapper[self.select]=self.piece        
                self.select = None
                #clears the user input so it's empty for next turn
                return
