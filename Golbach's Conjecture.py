from math import sqrt
import sys #to load output to a different file (Goldbach.txt)

original_stdout = sys.stdout

# not my own
def isPrime(n):
    if (n<=1):
        return False

    for i in range(2, int(sqrt(n))+1):
        if (n%i == 0):
            return False
        
    return True
#

num = int(input('Enter an even number: ')) #INPUT EVEN number only

if (num%2==0):
    with open("Goldbach.txt", 'w') as f: #to load output to a different file (Goldbach.txt)
        sys.stdout = f #to load output to a different file (Goldbach.txt)
        for i in range(2, int(num/2)): # check for numbers 2 to half of the num
            if isPrime(i) and isPrime(num-i):
                print(i,'+',num-i)
        sys.stdout = original_stdout #to revert back the output to the VSC terminal
        print("done!")
        with open(r"Goldbach.txt", 'r') as fp:
            count = 1
            for line in fp:
                count += 1

        print('Total pairs of prime additives (Number of prime pairs that add to the entered number): ', str(count)) # 8
        print('Total prime additives (Number of individual prime numbers that add to the entered number): ', str(count*2))
else:
    print("not an even number!")