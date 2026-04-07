with open("numbers.txt", "r") as f:
    
    for line in f:
        cl_lines = line.strip()
        num = int(cl_lines)
        print(num * 2)