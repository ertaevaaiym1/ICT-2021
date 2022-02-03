'''1'''
rows = int(input("Enter rows number: "))
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()

'''2'''
n = int(input("Enter number: "))
sum = 0
for num in range(1, n + 1, 1):
    sum = sum + num
print("Sum of first ", n, "numbers is: ", sum)
average = sum / n
print("Average of ", n, "numbers is: ", average)

'''3'''


'''4'''
starting = int(input("Enter starting number: "))
ending = int(input("Enter ending number: "))
for i in range(starting, ending + 1):
   if i > 1:
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            print(i)

'''5'''
fib = int(input("Enter number of terms: "))
a = 0
b = 1
if fib == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2,fib):
        c = a + b
        a = b
        b = c
        print(c)