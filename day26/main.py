
import pandas as pd

df = pd.read_csv("day26/nato_phonetic_alphabet.csv")

new_dict_with_nato = {row.letter:row.code for (index, row) in df.iterrows()}

user_input = input("enter a word: ")

for letter in user_input:
    print(f"{letter}: {new_dict_with_nato[letter.capitalize()]}")