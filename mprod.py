import sys

if len(sys.argv)==1:
    print("Invalid input")
    sys.exit()

def make_matrix(s):
    symb=s.split(",")
    matrix=[]
    for row in symb:
        values=row.split()
        matrix.append([float(n) for n in values])
    return matrix

def mult(A,B):
    rows_A=len(A)
    cols_A=len(A[0])
    rows_B=len(B)
    cols_B=len(B[0])

    if cols_A!=rows_B:
        return None

    result=[]
    for i in range(rows_A):
        row=[]
        for j in range(cols_B):
            s=0
            for k in range(cols_A):
                s+=A[i][k]*B[k][j]
            row.append(s)
        result.append(row)

    return result

matrices=[]
for arg in sys.argv[1:]:
    matrices.append(make_matrix(arg))

current=matrices[0]

for i in range(1, len(matrices)):
    current = mult(current, matrices[i])
    if current is None:
        print("Incompatible size of matrices")
        sys.exit()

print(current)