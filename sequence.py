n = int(input("Enter the length of the sequence: ")) # Do not change this line
num0 = 1
num1 = 2
num2 = 3
newnum = 0
print(num0, num1, num2, end=' ')

for i in range(1, n-2):
    newnum = num0 + num1 + num2
    print(newnum, end=" ")
    num0 = num1
    num1 = num2
    num2 = newnum