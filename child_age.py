age=int(input("введите возраст "))

if age<7:
    print("детский сад")
elif age<=17:
    print("школа")
elif age<22:
    print("университет")
else:
    print("работа")