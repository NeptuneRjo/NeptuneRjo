# Create caesar's cipher shift, but allow users to input the amount they 
# want the shift by


def caesar_cipher():
    user_input = input("Enter your text: ")
    cipher_shift = int(input("By how much do you want to shift? "))
    cipher_text = ""

    for i in user_input:
        if i.isalpha():
            keep_alphabet = ord(i) + cipher_shift
            
            if keep_alphabet > ord('z'):
                keep_alphabet -= 26
            
            shifted_text = chr(keep_alphabet)
            cipher_text += shifted_text
        
        if i.isdigit() or i.isspace():
            cipher_text += i
    
    print(cipher_text)

caesar_cipher()


