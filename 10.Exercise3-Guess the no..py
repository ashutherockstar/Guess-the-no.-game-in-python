n = 18
no_of_guesses = 1
print("You have only 9 guesses!!!\n")
while(no_of_guesses<=9):
    guess = int(input("Enter the no.="))
    if(guess>=15 and guess<18):
        print("You have entered no. to close!!!")
    elif(guess>18 and guess<=23):
        print("You have entered no. to close!!!")
    elif(guess<15):
        print("You have enter to smaller no.")
    elif(guess>23):
        print("you have enter to high no.")
    else:
        print("you won")
        print("No. of Guesses",no_of_guesses)
        break
    print("No. of guesses left ",9-no_of_guesses)
    no_of_guesses = no_of_guesses+1
if(no_of_guesses>9):
    print("Game over")

