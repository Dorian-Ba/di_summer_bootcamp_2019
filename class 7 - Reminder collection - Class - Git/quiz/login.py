import json,os
users=[]
connected_user={}

def load_json_to_python():
    global users
    if os.path.exists("users.json"):
        f=open("users.json","r")
        users = json.load(f)
        f.close()
    else:
        users=[]

def load_python_to_json():
    global users
    global connected_user
    f=open("users.json","w")
    f.write(json.dumps(users))
    f.close()

def create_new_user():
    global connected_user
    username = input('Username:')
    password = input('Password:')
    email = input('Email:')

    new_user = {
        "username": username,
        "password": password,
        "email": email
    }
    users.append(new_user)
    connected_user=new_user
    return connected_user

def log_in():
    global users
    global connected_user
    username = input('What is your username:')
    password = input('What is your password:')

    for user in users:
        if user['username'] == username:
            for i in range(3):
                if user['password'] == password:
                    print('you are logged in')
                    connected_user=user
                    return True
                else:
                    password = input('Password wrong, please enter it again:')


    answer = input("We didn't find any user matching those credentials do you want to create a new user (Y/N):")
    if answer == 'Y':
        connected_user=create_new_user()
        return True
    else:
        return False

