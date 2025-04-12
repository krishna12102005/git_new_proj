# Fibonacii program
def Fibonacci():
    n = int(input("Enter the number n:"))
    first = 0
    second = 1
    for i in range(1,n+1):
        print(first,end=" ")
        next = first + second
        first = second
        second = next
Fibonacci()
        