with open("numbers.txt", "r") as f:

    sum = 0
    n = 0

    for line in f:
        cl_lines = line.strip()
        if cl_lines:
            num = int(cl_lines)
            sum = sum + num
            n = n + 1
        
print(f"sum = {sum}")
      
print(f"n = {n}")

print(f"average = {sum / n}")