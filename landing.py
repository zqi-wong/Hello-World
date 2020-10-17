import json

def get_usernames():
    filename = "usernames.json"
    try:
        with open(filename) as obs:
            usernames = json.load(obs)
    except FileNotFoundError:
        usernames = {}
    return usernames

def sign_up(usernames):
    key = input("Please input your account:(If you want to quit, input 'q'.)")
    if key == 'q':
        return
    value = input("Please input your password:")
    for account in usernames.keys():
        if account == key:
            print("You had been signed up.Try to sign in then.\n")
            return True
    usernames[key] = value

def sign_in(usernames,b=False):
    key = input("Please input your account:(If you want to quit, input 'q'.)")
    while key != 'q':
        value = input("Please input your password:")
        if value == usernames[key]:
            print("You have been signed in.")
            b = True
            break
        else:
            print("You input a wrong password.Please try it again.\n")
        key = input("Please input your account:(If you want to quit input 'q'.)")
        value = input("Please input your password:")

usernames = get_usernames()
b = False
while True:
    order = input("What order do you want to make?Please input 'sign in' , 'sign up' or 'quit'\n")
    if order == 'sign in':
        sign_in(usernames,b)
        break
    elif order == 'sign up':
        if sign_up(usernames):
            sign_in(usernames,b)
        break
    elif order == 'quit':
        break
    else:
        print("You have inputed sth wrong.Please try again.")
filename = "usernames.json"
with open(filename,'w') as ob:
    json.dump(usernames,ob)
