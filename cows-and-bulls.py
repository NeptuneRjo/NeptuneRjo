import random

def cows_and_bulls():
    global CPU_number
    cows = 0
    bulls = 0

    # while the user# doesnt equal the CPU number, continue the program
    while cows != 4:
        user_number = str(input("Enter a 4-digit number: "))

        # check each digit, if its the same, add to cows, if not, add to bulls
        for i in range(len(CPU_number)):
            if user_number[i] == CPU_number[i]:
                print("Digit", i+1, "is correct")
                cows += 1
            else: bulls += 1


        print(cows, "cows and", bulls, "bulls")
        print("Please try again")

        # if all digits are the same, end the program
        if cows == 4:
            print(cows, "cows and", bulls, "bulls")
            print("You guessed correctly! The 4-digit number was:", CPU_number)
            break

        cows = 0
        bulls = 0



# create a random 4-digit number
CPU_number = str(random.randint(1000, 10000))
cows_and_bulls()
