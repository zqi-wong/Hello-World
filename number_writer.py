import json

filename = 'numbers.json'
with open(filename,'r') as f_obj:
    numbers = json.load(f_obj)

with open('output.txt','w') as obs:
    obs.write(str(numbers[:]) + '\t')
    