import os
import regex as re

os.chdir('/home/digger/Classes/Python/Workbook_100_Ardit/Files')

def count_words(filepath):
    with open(filepath, 'r') as file:
        string = file.read()
        string = string.replace(',', ' ')
        strng_list = string.split(" ")
        return len(strng_list)

print(count_words("words2.txt"))

# Solution with Regex

def count_words_re(filepath):
    with open(filepath, 'r') as file:
        string = file.read()
        string = string.replace(',', ' ')
        strng_list = re.split(",| ", string)
        return len(strng_list)

print(count_words_re("words2.txt"))