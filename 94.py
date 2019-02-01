with open ("./Files/urls.txt", 'r') as file:
    text = file.read()
    text.replace("https:/","http://")

print(text)

'''
with open("./Files/urls.txt", "r") as file:
    lines = file.readlines()

with open("urls_corrected.txt", "w") as file:
    for line in lines:
        line_remove_s = line.replace("s", "", 1)  The one removes the first occurrence only
        line_remove_s_add_slash = line_remove_s[:6] + "/" + line_remove_s[:6]
        file.write(line_remove_s_add_dash)
'''
