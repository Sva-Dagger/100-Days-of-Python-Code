alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
end_of_game = False

while not end_of_game :

    def encrypt(plain_text, shift_amount) :
        cipher_text = ""
        for letter in plain_text :
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(f"Encoded text is {cipher_text}")
        decryption =input("if you want to decrypt the word yes/no : ").lower()
        if decryption == "yes" :

            def decrypt(cipher_text, shift_amount):
                New_cipher_text = ""
                for letter in cipher_text :
                    position = alphabet.index(letter)
                    new_position = position - shift_amount
                    new_letter = alphabet[new_position]
                    New_cipher_text += new_letter
                print(New_cipher_text)

            decrypt(cipher_text, shift_amount=shift)

    def decrypt(plain_text, shift_amount):
        New_cipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
            New_cipher_text += new_letter
        print(New_cipher_text)

    if direction == "encrypt" :
        encrypt(plain_text = text, shift_amount = shift)
        user_choice = input("whether you want to continue yes/ no : ")
        if user_choice == "yes":
            end_of_geme = False
        else :
            end_of_geme = True
    elif direction == "decrypt" :
        decrypt(plain_text = text, shift_amount=shift)
