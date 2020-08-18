import Player as P
#importing the player class into file with the alias P
import board as B
#same as above but for the board and the alias B
import random

class main():
    b=B.Board()
    print ("Tic Tac Toe\n\nLet's play.")
    print ("Please set-up the board first.")

    while True:
        print ("""Menu
[1] Play
[2] Set-up
[3] Help
[4] Quit""")

#multi line comment to display information for the user
        menu=input("Enter number:\n")
        if menu == "1": #this won't be possible until setup has been completed by user
            turn = 1
            b.display()

            while turn < 10:     # limits the game to 9 rounds, only 9 spaces in grid          
                  
                if (turn%2)!= 0:
                    #not equal function for first player ie not even
                    first.action(b.mark)
                    b.display()

                elif (turn%2)== 0:
                    # equal function so the second player runs when equal
                    second.action(b.mark)
                    b.display()
                    
                b.game(play01.piece)
                b.game(play02.piece)
                if b.end is True:
                    print ("Winner and Loser determined")
                    turn = 10 # triggers end loop uses the variable to trigger end game function
                    
                elif turn ==9:
                    print ("Game over, draw.")
                    #when the turn reaches 9 it'll call this statement when the board.end function doesn't
                    #return a true statement.
                    
                turn +=1 # adds +1 to the turn for each time a player takes turn

            if turn >=10:  
                turn = 1
                b.mark=b.new.copy()
                b.end=False
                #game finished, this resets the board for a new game.
                #copying the board.new list into the mark list

            
        elif menu == "2":
            #for player set up, most player class method is running here
            play01 = P.Player(input("Player01:\nWrite your name.\n") or "Player01")
            play02 = P.Player(input("Player02:\nWrite your name.\n") or "Player02")
            #adding input or so user don't need to think of a name
            play01.side(play02.name,play02.piece)
            play02.side(play01.name,play01.piece)
            while True:
                counter = input (f"who will start?\n[1] {play01.name}\n[2] {play02.name}\n") or str(random.randint(1,2))
                if counter in ["1","2"]:
                    if counter == "1":
                        first = play01 
                        second = play02
                        #first and second is for menu:[1] play,
                        print(f"{play01.name} will start first with {play01.piece}.")
                        break
                    elif counter == "2":
                        first = play02
                        second = play01
                        print(f"{play02.name} will start first with {play02.piece}.")
                        break
                else:
                   print ("input error, try again.")
                   #statement for input error
            play01.cpu()     
            play02.cpu() # runs the player class method for determining AI or Human

        elif menu == "3": 
            print ("Input number corresponding to the tile.")
            #explains what needs to be pressed to play game.
            b.showkey() #the key menu for key guidance
        elif menu == "4":
            confirm = True
            while confirm is True:
                conf=input("Are you sure?\n[1] Yes\n[2] No\n")
                if conf == "1":
                    break #breaks the loop and continue
                elif conf == "2":
                    confirm = False #ends the loopand runs the next line of code 
                else:
                    print ("Error, please try again.")
                    continue #maintains the loop until the user inputs correct value
            if conf == "1":
                print ("Game shutting down")
                input("Press enter to close window")
                break #ends the program

            
        else:
            print ("Input error, pick a number from 1 - 4.\n")
            continue # reloop the menu program 




main=main()
