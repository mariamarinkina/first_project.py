with open("numbers.txt", "r") as f:

    max = 0

    for line in f:
        cl_lines = line.strip()
        num = int(cl_lines)

        if max < num:
            max = num

print(num)