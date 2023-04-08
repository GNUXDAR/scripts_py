# listas con map() y filter()
# map() para tranformar a los usuarios

users = [
    ["admin", 1],
    ["gnuxdar", 7],
    ["grebo", 5]
]

names = list(map(lambda user: user[0], users))
print(names)

# filter()
menos_users = list(filter(lambda user: user[1] > 2, users))
print(menos_users)