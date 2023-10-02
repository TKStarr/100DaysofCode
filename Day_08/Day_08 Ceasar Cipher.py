alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
text_list = list(text)
text_list_indexed = []
text_list_indexed_encrypted =[]
text_list_indexed_encrypted_str = []
def encrypt(text_code=text_list,shift_amt=shift):
    if direction == "decode":
        shift_amt = -shift_amt

    for char in range(0, len(text_code)):
        text_list_indexed.append(alphabet.index(text_code[char])) # convert input to list of letters and get the indexed amount of those letters.
        text_list_indexed_encrypted.append(shift_amt + alphabet.index(text_code[char])) # shift the index by the shift amount.

    for x in range(0,len(text_list_indexed_encrypted)):  #error checking for when the shift causes the index to go over 26.
        if text_list_indexed_encrypted[x] > 26:
            text_list_indexed_encrypted[x] = text_list_indexed_encrypted[x] - 26
        text_list_indexed_encrypted_str.append(alphabet[text_list_indexed_encrypted[x]])  #converting the list back into a string.

encrypt(text, shift)

encrypted_code = ''.join(text_list_indexed_encrypted_str)

print(encrypted_code)
