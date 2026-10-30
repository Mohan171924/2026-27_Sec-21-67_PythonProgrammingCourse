# program to calculate the sum and average of N numbers using for loop
n = int(input("Enter the number of elements: "))
sum = 0
for i in range(n):
    num = int(input("Enter a number: "))
    sum += num
average = sum / n if n > 0 else 0
print(f"Sum: {sum}")
print(f"Average: {average}")