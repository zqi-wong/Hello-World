print("使用说明：先后输入整数部分和小数部分\n如：3.141，分别输入3和141\n如果没有小数部分请输入0\n")
a = input("请输入整数部分：")
b = input("请输入小数部分：")
b = float("0." + str(b))
ans = str(bin(int(a)))
ans = ans[2:]
i = 1
bo = False
while b != 0.0 and i <= 100:
    if not bo:
        ans += '.'
    bo = True
    b = b*2
    c = round(b,0)
    if c>b:
        c = c-1
    b = b-c
    ans += str(int(c))
    i += 1
print(ans)
