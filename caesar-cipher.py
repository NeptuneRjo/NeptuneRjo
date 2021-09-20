# Create caesar's cipher shift, but allow users to input the amount they 
# want the shift by


def caesar_cipher():
    user_input = input("Enter your text: ")
    cipher_shift = int(input("By how much do you want to shift? "))
    cipher_text = ""

    for i in user_input:
        # if the character is a-z, convert it to ASCII and add the shift to it
        if i.isalpha():
            keep_alphabet = ord(i) + cipher_shift
            # if the ASCII digit is higher than z after the shift, bring it back down to a
            if keep_alphabet > ord('z'):
                keep_alphabet -= 26
            # change the ASCII digit to alphabetical and place into new var
            shifted_text = chr(keep_alphabet)
            cipher_text += shifted_text
        # if the character is a digit, add it to the var
        if i.isdigit() or i.isspace():
            cipher_text += i
    
    print(cipher_text)

caesar_cipher()


