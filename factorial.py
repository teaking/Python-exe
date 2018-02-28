"""
factorial program to take the num parameter and return the factorial of it
"""
#4 x 3 x 2 x 1
def factorial(num):
    if num == 1:
        return 1
    return (num * factorial(num - 1))    


def main():
   print(factorial(8))     

main()
