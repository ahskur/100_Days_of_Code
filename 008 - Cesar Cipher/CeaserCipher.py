# Encode messages using this cipher
# List of all letters
# List needs to be duplicated to account for cases with letter Z that would be at the last positin of the list and couldn't be shifted
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)

# Let's state a boolean to ask the user if they still want to use the program
should_continue = True

# # Creating a function to encrypt the text - And for every letter inside the inputted text, we're going to shift it in x amount
# def encrypt(plain_text,shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         #We're using index(letter) to see which position the letter is in the List called alphabet (as integer)
#         position = alphabet.index(letter)
#         #Now we're adding the shift_amount to the position, so we can have the ending position of the letter after the shift
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}.")
# # Now we're gonna create a function to decode inputted text almost the same as with encrypt function but the shift amount needs to go to the other side
# def decrypt(cipher_text, shift_amount):
#     decrypted_text =""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         decrypted_text += alphabet[new_position]
#     print(f"The decoded text is {decrypted_text}.")

# Combining the two functions into one, so we can call it just once:
def caeser(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {direction}d text is {end_text}.")

# # Now let's set the directions
# # We're gonna call the function and use the inputs as arguments to the parameters of the function
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text,shift_amount=shift)

while should_continue:
    # What do you wish to do
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # Text of message
    text = input("Type your message:\n").lower()
    # How much do you want to shift the alphabet to encode the message
    shift = int(input("Type the shift number:\n"))
    # To account for big number cases e.g 67, it's needed to see how many times does the letter amount in alphabet can be repeated inside the given number
    # and the actual shift is going to be te remainder of this division
    shift = shift % 26

    caeser(start_text=text,shift_amount=shift,cipher_direction=direction)
    result = input("Type 'yes' if you want to go again, 'no' for stop.\n")
    if result == "no":
        should_continue = False
        print("Bye-bye! >:)")


