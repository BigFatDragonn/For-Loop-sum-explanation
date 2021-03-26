
n = int(input())
# sum_1 = 0 right way to do the for loop
for x in range(n):
    x = int(input())
    # sum_1 += x  otherwsie wont take the las x into the calculation
    x += x # not gonna work properly 
print(float(x / n)) # it is going to divide 10 / 3 instead of 15 / 3 >>>> range(n),range(n+1) etc.
