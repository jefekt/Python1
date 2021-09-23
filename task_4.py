def authorization1(users, user_name, user_password):
    for key, value in users.items():
        if key ==user_name:
            if value['password'] == user_password and value['activation']:
                return "Welcome"
            elif value['password'] == user_password and not value['activation']:
                return "Eror"
            elif value['password']
                return "The password is not correct"
    return "The user was not found"


def authorization2(users, user_name, user_password):
    if users.get(user_name):
        if users[user_name]['password'] == user_password and users[user_name]['activation']:
            return "Welcome"
        elif users[user_name]['password'] == user_password and not users[user_name]['activation']:
            return "Eror"
        elif users[user_name]['password'] != user_password:
            return "The password is not correct"
    else:
        return "The user was not found"


users = {'user1' :{'password' : '12345', 'activation': True},
        'user2' :{'password' : '12345', 'activation': False},
        'user3' :{'password' : '12345', 'activation': False},
        'user4' :{'password' : '12345', 'activation': True}
         }
print(authorization2(users, 'user3' , '12345'))