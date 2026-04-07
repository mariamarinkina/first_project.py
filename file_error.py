import sys

name = sys.argv[1]

try:
    with open("number.txt", "r") as f:
        list = []
        for line in f:
            list.append(int(line.strip()))
    print("файл успешно прочитан")
except FileNotFoundError:
    print(f"ошибка: файл '{name}' не найден")
    sys.exit(1)