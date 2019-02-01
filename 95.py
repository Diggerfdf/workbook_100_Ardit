line = input("Enter values (comma, separated): ")
line_list = line.split(",")
line_list = [element.strip() for element in line_list]

with open("./Files/user_data_commas.txt", "a+") as file:
    for i in line_list:
        file.write(i +"\n")
