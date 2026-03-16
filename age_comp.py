import sys
my_age = int(sys.argv[1])

friend_age = 20

if my_age > friend_age:
    print("я старше друга")
else:
    print("я не старше друга")

if my_age == friend_age:
    print("мы одного возраста")
else:
    print("мы не одного возраста")

if my_age < 18:
    print("мне меньше 18")
else:
    print("мне не меньше 18")

if friend_age > 18:
    print("другу больше 18")
elif friend_age == 18:
    print("другу 18")
else:
    print("другу меньше 18")