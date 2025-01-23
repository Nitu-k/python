#zip(*iterables) aggregate element from 2 or more iterable (list, set, tuple)
#create zip obj with paired element stored in tuple

usernames=["Dude","Bro","Mister"]
passwords=("pas@eord","abc123","guest")

users=zip(usernames,passwords)

print(type(users))
for i in users:
    print(i)

    