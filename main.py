import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}
# print(nato_dict)

usr_word = input("Enter a word: ").upper()
usr_nato = [nato_dict[letter] for letter in usr_word]
print(usr_nato)