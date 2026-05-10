def average(a, b):
    print("The average is",(a+b)/2)
average(5, 10)
average(15, 20)
def average(numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum+i
    print("The average is", sum/len(numbers))
average([5, 10, 15, 20])