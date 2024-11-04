import pandas
game_is_on = True
while game_is_on :
    try:
        data = pandas.read_csv("nato_phonetic_alphabet.csv")
        word = input("Enter a word: ").upper()
        New_data = {row.letter:row.code for (index,row) in data.iterrows()}
        if word == "EXIT":
            game_is_on = False
        output_list = [New_data[letter] for letter in word]
    except:

        print("Sorry, only letters in the alphabet please.")
    else:
        print(output_list)
