  
terms = int(input("Enter the number of terms for Fibonacci series: "))

 
first = 0
second = 1
count = 0

print("Fibonacci Series:")

if terms <= 0:
    print("Please enter a positive number.")
elif terms == 1:
    print(first)
else:
    while count < terms:
        print(first)
        next_term = first + second
        first = second
        second = next_term
        count += 1
