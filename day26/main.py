
import pandas as pd

df = pd.read_csv("day26/nato_phonetic_alphabet.csv")

new_dict_with_nato = {row.letter:row.code for (index, row) in df.iterrows()}

def generate_phonetic():
    user_input = input("enter a word: ").upper()

    try:
    
        output_list = [new_dict_with_nato[letter] for letter in user_input]
    except KeyError:
        print("please enter a word")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()