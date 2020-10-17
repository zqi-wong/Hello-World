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
    key = input("\nSIGN UP:\nPlease input your account:(If you want to quit, input 'q'.)")
    if key == 'q':
        return
    value = input("Please input your password:")
    for account in usernames.keys():
        if account == key:
            print("You had been signed up.Try to sign in then.")
            return True
    usernames[key] = value

def sign_in(usernames):
    global b
    b = False
    key = input("\nSIGN IN:\nPlease input your account:(If you want to quit, input 'q'.)")
    while key != 'q':
        value = input("Please input your password:")
        try:
            if value == usernames[key]:
                print("You have been signed in.")
                b = True
                break
            else:
                print("You input a wrong password.Please try it again.\n")
        except KeyError:
            print("We don't have this account.Please sign up first.")
            return True
        key = input("Please input your account:(If you want to quit input 'q'.)")

usernames = get_usernames()
while True:
    order = input("\nWhat order do you want to make?Please input 'sign in' , 'sign up' or 'quit'\n")
    if order == 'sign in':
        if sign_in(usernames):
            sign_up(usernames)
    elif order == 'sign up':
        if sign_up(usernames):
            sign_in(usernames)
    elif order == 'quit':
        break
    else:
        print("You have inputed sth wrong.Please try again.\n")
    if b:
        break
filename = "usernames.json"
with open(filename,'w') as ob:
    json.dump(usernames,ob)
