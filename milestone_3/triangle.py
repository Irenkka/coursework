
def get_triangle(rows: int):
    triangle = [[1]]
    for i in range(1, rows):
        row = []
        for j in range(i+1):
            if j == 0:
                row.append(1)
            elif j + 1 <= i:
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            else:
                row.append(1)
        triangle.append(row)
    return triangle
       

number = int(input("Input a number: "))
print("")

triangle = get_triangle(number)

for i in range(number):
    print(" " * 2 * (number - i), end="")
    for j in range(i+1):
        print(" " + str(triangle[i][j]) + "  ", end="")
    print("")
