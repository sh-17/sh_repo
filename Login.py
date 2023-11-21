email = input("Enter email id:")
password = input("Enter your password:")


def login(email,password):
    email = ['a@b.com', 'i@j.com', 'x@y.com']
    password = ['abc123', 'ijk234', 'xyz567']

    def success():
        print("Login successful")

    def error():
        print("Invalid username or password")

    for i in range(0,len(email)):
        if email[i]==email and password[i]==password:
            success()
            break
    else:
        error()

login(email,password)
