def santa_users(users):
    d = {}
    for user in users:
        if len(user) == 1:
            d[user[0]] = None
            continue
        d[user[0]] = user[1]
    return d

array = [["name1 surname1", 12345], ["name2 surname2"], ["name3 surname3", 12354], ["name4 surname4", 12435]]

print(santa_users(array))
