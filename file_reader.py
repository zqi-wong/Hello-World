file_path = 'pi_digits.txt'
filename = 'pi.txt'
with open(file_path,'r') as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

with open(filename,'a') as file_object:
    file_object.write(pi_string + '\n' + str(len(pi_string)) + '\n')