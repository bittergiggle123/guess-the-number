import random #the random moudule is taken to put random number
def guess_the_number():
    print("\n welcome to guess the number")
    print("think of a number in bettween 1 and 100")
    print("can you guess it")

     
    number_to_guess = random.randint(1,100)
    attempts=0

    while True:
        try:
             guess=int(input("enter your numbers: "))
             attempts +=1


             if guess < number_to_guess:
                print("to low try again")
             elif guess > number_to_guess:
             
                print(" to high try again")
             else:
              print(f"you guessed correct in {attempts} attempts")
              break
        except ValueError:
            print("are you dumb that is not a number")
guess_the_number()
        
         