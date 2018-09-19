# fibonacci.py
# Program that computes the nth term in a classic Fibonacci sequence

def main():
    fib = int(input("Enter a number that you would like to know the value of in a classic Fibbonacci sequence: "))
    n1 = 1
    n2 = 1
    n3 = n1
    for i in range(1,fib-1): 
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    print(n3)

main()
