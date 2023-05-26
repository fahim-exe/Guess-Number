import random 


def guess_number():
    print("This is a number guessing game.")
    print("You have only one hint even or odd.")
    print("You will only know if your guess is high or low.")
    print("To quit the game enter 0\n")
    random_number = random.randint(1, 101)
    if random_number%2==0:
        hint = "The number is even!!"
    if random_number%2!=0:
        hint = "The number is odd!!"
    
    while True:
        x = int(input("Enter your guess: "))
        if random_number==x:
            print("\nYour Guess is Correct!!!!!")
            print("The number is", random_number)
            return

        elif x>random_number:
            if x==0:
                print("Quite Game!!!XXX")
                return
            print("\nYour guess is high!!")
            print("Hint: "+hint)
            
            

        elif x<random_number:
            if x==0:
                print("Quite Game!!!XXX")
                return
            print("\nYour guess is low!!\n")
            print("Hint: "+hint)

        
            


guess_number()