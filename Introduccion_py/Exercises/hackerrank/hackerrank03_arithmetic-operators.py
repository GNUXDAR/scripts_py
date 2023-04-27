# Task
# The provided code stub reads two integers from STDIN, and . Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers(first - second).
# The third line contains the product of the two numbers.
# Example
# a = 3
# b = 5
# print(10**10) #10000000000

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if a > 0 and b > 0:
        if a < 10**10 and b < 10**10:
            print(a + b)
            print(a - b)
            print(a * b)
        else:
            print('Error')
    else:
        print('Error')
