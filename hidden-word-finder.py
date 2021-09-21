import random
import string

letters = string.ascii_lowercase
random_letters = "".join(random.choice(letters) for i in range(13))

def hidden():
    global random_letters
    user_word = input("Enter your word: ")
    yes_no = input("Do you want to enter your own random letters? (yes/no) ")
    check_word = ""
   
    if yes_no == "no".casefold():
        for i in random_letters:
            if i in user_word:
                check_word += i
                    
        if check_word == user_word:
            print(random_letters, "contains the word", user_word)
        else: print(random_letters, "does not contain the word", user_word)
    
    if yes_no == "yes".casefold():
        user_random = input("Enter your random letters: ")

        for i in user_random:
            if i in user_word:
                check_word += i
                    
        if check_word == user_word:
            print(user_random, "contains the word", user_word)
        else: print(user_random, "does not contain the word", user_word)


hidden()

        




