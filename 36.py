import os

os.chdir('/home/digger/Classes/Python/Workbook_100_Ardit/Files')

def count_words(filepath):
    with open(filepath, 'r') as file:
        strng = file.read()
        strng_list = strng.split(" ")
        return len(strng_list)

print(count_words("words1.txt"))
