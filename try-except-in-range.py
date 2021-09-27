def read_int(prompt, min, max):


    try:
        user_num = int(input(prompt))
        user_min = int(input(min))
        user_max = int(input(max))

        assert user_num >= user_min 
        assert user_num <= user_max 
        print("The number:", user_num, "is in your given range")

    except AssertionError:
        print("Error: The value is not in the given range.")
        print("The number is:", user_num)

    except TypeError:
        print("Error: The value entered is not correct.")
    
var = read_int("Enter a number: ", "Enter your minimum: ", "Enter your maximum: ")

