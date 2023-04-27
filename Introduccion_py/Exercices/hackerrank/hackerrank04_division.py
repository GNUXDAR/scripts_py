# Task
# The provided code stub reads two integers,  and, from STDIN.

# Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

# No rounding or formatting is necessary.

# Example


# The result of the integer division .
# The result of the float division is .

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if a > 0 and b > 0:
        result_integer = a // b
        result_float = a / b
        print(f'The result of the integer division is {a}//{b}={result_integer}')
        print(f'The result of the float division is {a}/{b}={result_float}')
    else:
        print('Error')
