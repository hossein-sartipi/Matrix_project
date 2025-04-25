from sympy import *


def create_row(row):
    if row==[]:
        return []
    for element in row:
        try:
            float(S(element))
            row=[Rational(element) for element in row]
        except:
            return 0
    return row


def create_matrix():
    matrix = []
    i = 0
    j = 1
    while True:
        x = input(f"row{j}: ").split()
        row = create_row(x)
        if row == 0:
            print("wrong entery")
            continue
        elif row == []:
            show_matrix(matrix)
            break
        else:
            if i == 0:
                matrix.append(row)
                i += 1
            elif len(row) == len(matrix[i-1]):
                matrix.append(row)
                i += 1
            else:
                print("wrong length")
                continue
        j += 1
    return matrix


def show_matrix(matrix):
    for row in matrix:
        print(row)


def opp_1(matrix,columns_number,rows_number):
    while True:
        r =get_row("")
        if not r:
            break
        elif 1 <= r <= rows_number:
            c=get_constant()
            if not c:
                break
            try:
                float(c)
            except:
                print("just constant!")
                continue
            for i in range(columns_number):
                matrix[r-1][i] = S(c) * S(matrix[r-1][i])
            show_matrix(matrix)

        else:
            print("row dose not exist!")


def opp_2(matrix,rows_number):
    while True:
        r = get_row(1)
        if not r:
            break
        elif not 1<=r<=rows_number:
            print("wrong row")
            continue
        s = get_row(2)
        if not s:
            break
        elif not 1<=s<=rows_number:
            print("wrong row")
            continue
        else:
            matrix[r-1], matrix[s-1] = matrix[s-1], matrix[r-1]
            show_matrix(matrix)
            continue
def opp_3(matrix,coulumn_numbers,row_numbers):
    while True:
        r=get_row("Target-")
        if not r:
            break
        elif not 1<=r<=row_numbers:
            print("wrong row")
            continue
        c=get_constant()
        s=get_row("Desired-")
        if not s:
            break
        elif not 1<=s<=row_numbers:
            print("wrong row")
            continue
        for i in range(coulumn_numbers):
            matrix[r-1][i]=(c*matrix[s-1][i])+(matrix[r-1][i])
        show_matrix(matrix)
            
def main():
    x = create_matrix()
    while True:
        try:
            answer=int(input("opp_1(1)-opp_2(2)-opp_3(3)-echelon(4)-new matrix(5)-exist(6)"))
        except:
            print("wrong input!")
            continue
        if answer==6:
            break
        elif answer==1:
            opp_1(x,len(x[0]),len(x))
        elif answer==2:
            opp_2(x,len(x))
        elif answer==3:
            opp_3(x,len(x[0]),len(x))
        elif answer==4:
            echelon(x)
        elif answer ==5:
            x=create_matrix()
        else:
            print("command not valid!")
            continue
def get_row(i):
    while True:
        r = input(f"{i}row:")
        if r == "":
            break
        try:
            return int(r)
        except:
            print("wrong input!")
            continue
def get_constant():
    while True:
        c = input("number:")
        if c == "":
            break
        try:
            return S(c)
        except:
            print("wrong input!")
            continue
def I_matrix(m):
    matrix=[]
    for i in range(m):
        row=[]
        for j in range(m):
            if i==j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix
def echelon(A):
    box=[]
    B=[]
    def c_div(matrix,i,j):
        for k in range(0,len(matrix[0])):
            matrix[i][k]= Rational(S(1/j) * S(matrix[i][k]))
        return matrix

    def col_e(matrix,row_index,column_index):
        for k in range(len(matrix)):
            counter=column_index
            if k ==row_index:
                continue
            elif matrix[k][column_index]!=0:
                target=-matrix[k][column_index]
                while counter <len(matrix[0]):
                    matrix[k][counter]=(matrix[row_index][counter]*target) + (matrix[k][counter])
                    counter+=1
                
        return matrix
    for i in range(0,len(A)):
        for j in range(0,len(A[0])):
            if A[i][j]!=0:
                A=c_div(A,i,A[i][j])
                A=col_e(A,i,j)
                break
    for row in range(len(A)):
        for column in range(len(A[0])):
            if A[row][column]==1:
                box.append((row,column))
    box.sort(key=lambda x:x[1])
    for item in box:
        B.append(A[item[0]])
    show_matrix(B)
main()