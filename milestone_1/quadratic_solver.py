eq = "8x^2   + 4x +      (-16) = 0" 
# remove all spaces from input string
eq_clean = eq.replace (" ", "")

# split the clened eq at + into a list of strings
eq_split = eq_clean.split ('+')

# from the first string in the list remove x^2 
a = eq_split[0].replace("x^2", "")
a = int(a)

# from the second string in the list remove x 
b = eq_split[1].replace('x', '')
b = int(b)

# from the third string in the list remove =0 and bracets () 
c = eq_split[2].replace('=0', '').replace('(' , '').replace(')', '')
c = int (c)
print (a, b, c)

# step 2 calculate answer
x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)

print(x1,x2)