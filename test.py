while True:
    n = input()
    if len(n) == 18:
        break
    else:
        print("please retype")
s = 0
a = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
for i in range(0,17):
    s += int(n[i:i+1])*a[i]
print(s%11)