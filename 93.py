import glob

file_list = glob.glob("./Files/Ex_93/**/*.py", recursive=True)
print(len(file_list))
