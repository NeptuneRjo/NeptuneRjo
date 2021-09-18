# print inputed number as seven-segment display 


ssd = {
    '0': ('###', '# #', '# #', '# #', '###'),
    '1': ('  #', '  #', '  #', '  #', '  #'),
    '2': ('###', '  #', '###', '#  ', '###'),
    '3': ('###', '  #', '###', '  #', '###'),
    '4': ('# #', '# #', '###', '  #', '  #'),
    '5': ('###', '#  ', '###', '  #', '###'),
    '6': ('###', '#  ', '###', '# #', '###'),
    '7': ('###', '  #', '  #', '  #', '  #'),
    '8': ('###', '# #', '###', '# #', '###'),
    '9': ('###', '# #', '###', '  #', '###'),
    '.': ('   ', '   ', '   ', '   ', '  #'),
}

    
def user_input():
    number = input("Please enter a number: ")
    # finds the dictionary index for each number in the string
    digits = [ssd[digit] for digit in str(number)]
    # the range is 5 because each number is prints 5 rows of text
    for i in range(5):
        print(" ".join(segment[i] for segment in digits))

user_input()
