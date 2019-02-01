file = open('./Files/user_data_save_close.txt', 'a+')

while True:
    line = input("Enter value: ")
    if line == "SAVE":
        file.close()
        file = open("./Files/user_data_save_close.txt", "a+")

    elif line == "CLOSE":
        file.close()
        break

    else:
        file.write(line + "\n")
