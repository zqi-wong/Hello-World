print("使用说明：先后输入小数点前最高位数和该数\n")
n = input("请输入小数点前最高位数:(例如10.10，输入2；101.1100，输入3；0.1101，输入1)")
a = input("请输入该数：")
n = int(n)-1
b = a[0:n+1]
b += a[n+2:]
b += 'e'
#print(b)
i = 0
s = 0.0
while True:
    k = 2**float(n)
    s += float(b[i:i+1])*k
    #print(s)
    n -= 1
    i += 1
    if b[i:i+1]=='e':
        break
print(s)