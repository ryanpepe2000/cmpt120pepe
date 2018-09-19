# pi.py
# Calculates the value of pi.

def main():
    n = int(input("Enter the number of terms to use to estimate pi: "))
    sign = 1
    pi = 0
    for i in range(1,n*2+1,2):
        pi = pi + sign * (4/i)
        sign = sign * -1
        
        
    print(pi)
main()
    
