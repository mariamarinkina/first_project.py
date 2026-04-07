with open("sorted_small.txt", "w") as f:
    for i in range(1, 11):
        f.write(str(i) + "\n")

with open("sorted_medium.txt", "w") as f:
    for i in range(1, 101):
        f.write(str(i) + "\n")

with open("sorted_large.txt", "w") as f:
    for i in range(1, 1001):
        f.write(str(i) + "\n")

print("Файлы созданы: sorted_small.txt, sorted_medium.txt, sorted_large.txt")     