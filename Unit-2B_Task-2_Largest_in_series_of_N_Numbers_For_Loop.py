# program to print the multiplication table of a number using for loop
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)

# program to print the multiplication table of a number using while loop
num = int(input("Enter a number: "))
i = 1 
while i <= 10:
    print(num, 'x', i, '=', num*i)
    i +=1
    