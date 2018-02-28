'''Add up al lthe number from 1 to num, using stack'''

def main():
    num = input("Enter number")
    print (add(int(num)))

def add(num):
    if num == 1:
        return 1
    return add(num - 1) + num



main()
