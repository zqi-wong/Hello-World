file_path = r'D:\coding\pi_digits.txt'
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())