with open("numbers.txt", "r") as f:
    sum = 0

    for line in f:
        cl_line = line.strip()
        num = int(cl_line)
        sum = sum + num

print(sum)
