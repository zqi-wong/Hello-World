print("Give me two numbers,and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    f_n = input("\nfirst number:")
    if f_n == 'q':
        break
    s_n = input("\nsecond number:")
    try:
        answer = float(f_n)/float(s_n)
    except ZeroDivisionError:
        print("You can't ivide by 0!")
    else:
        print(answer)
    