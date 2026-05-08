def calculate_geometric_mean(x, y):
    gmean = (x*y)/(x+y)
    return gmean
def isGreater(x, y):
    if x > y:
        print(x, "is greater than", y)
    else:
        print(y, "is greater than", x)  
def isLesser(x, y):
    if x < y:
     pass     
            

a = 9
b = 8
isGreater(a, b)
# if(a>b):
#     print(a, "is greater than", b)
# else:
#     print(b, "is greater than", a)
gmean1 = calculate_geometric_mean(a, b)
print("The geometric mean of", a, "and", b, "is", gmean1)
c = 8 
d = 7
isGreater(c, d)
gmean2 = calculate_geometric_mean(c, d)
print("The geometric mean of", c, "and", d, "is", gmean2)
