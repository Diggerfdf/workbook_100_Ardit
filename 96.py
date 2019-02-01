file = open('./Files/user_data.txt', 'a+')


while True:
    line = input("Enter value: ")
    if line == "CLOSE":
        file.close()
        break

    else:
        file.write(line + "\n")
