alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

def encrypt(plain_text, shift_amount): # the encrypt function
  cipher_text = "" # make an empty string that will be the output
  for letter in plain_text: # for each letter in text
    position = alphabet.index(letter) # find the position of the letter in the alphabet
    new_position = position + shift_amount # new position is now the original + the shift amount
    cipher_text += alphabet[new_position] # adding the empty string and the new letters from the new position from the alphabet
  print(f"The encoded text is {cipher_text}") # output for encrypt()

def decrypt(cipher_text, shift_amount): #  the decrypt function
  plain_text = "" # create an empty string
  for letter in cipher_text: # for each letter in the cipher_text
    position = alphabet.index(letter) # find the position of the letter in the alphabet
    new_position = position - shift_amount # new position is now the original - the shift amount
    plain_text += alphabet[new_position] # adding the empty string and the new letters from the new position from the alphabet
  print(f"The decoded text is {plain_text}") # output for decrypt()


def ceaser(plain_text,cipher_text, shift_amount): # the ceaser function
  cipher_text = "" # make an empty string that will be the output
  for letter in plain_text: # for each letter in text
    position = alphabet.index(letter) # find the position of the letter in the alphabet
    new_position = position + shift_amount # new position is now the original + the shift amount
    cipher_text += alphabet[new_position]  # adding the empty string and the new letters from the new position from the alphabet
  print(f"The encoded text is {cipher_text}") # output for ceaser()
  plain_text = ""  # create an empty string
  for letter in cipher_text:  # for each letter in the cipher_text
    position = alphabet.index(letter) # find the position of the letter in the alphabet
    new_position = position - shift_amount # new position is now the original - the shift amount
    plain_text += alphabet[new_position] # adding the empty string and the new letters from the new position from the alphabet
  print(f"The decoded text is {plain_text}") # output for decrypt()



program_run = True
while program_run == True:
    text = input("Type your message:\n").lower() # asking the user for their message
    shift = int(input("Type the shift number:\n")) # the shift number is how many characters we shift over.
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or type 'ceaser' to see both encoded and decoded text:\n You can also type 'end' or 'stop' to quit the program. ") # starting point to session

    if direction == "ceaser": # if the user selects ceaser function
      ceaser(plain_text = text, cipher_text = text, shift_amount=shift) #  assigning parameters
    elif direction == "encode": # if the user selects encrypt function
      encrypt(plain_text=text, shift_amount=shift)   #  assigning parameters
    elif direction == "decode":  # if the user selects decrypt function
      decrypt(cipher_text=text, shift_amount=shift) #  assigning parameters
    elif direction == "end" or direction == "stop": # if the users selects the end or stop option.
        program_run = False
