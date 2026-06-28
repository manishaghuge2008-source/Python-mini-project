import random
import math

try:
    numbers = set()

    print("Enter 10 numbers:")

    for i in range(10):
        try:
            num = float(input(f"Enter number {i+1}: "))
            numbers.add(num)   
        except ValueError:
            print("Invalid input! Please enter a number.")

   
    num_tuple = tuple(numbers)

    print("\n nique numbers (Set):", numbers)
    print("Tuple:", num_tuple)

   
    if len(num_tuple) < 3:
        print("Not enough unique numbers for random selection!")
    else:
        print("3 Random numbers:", random.sample(num_tuple, 3))


    total = sum(num_tuple)
    print("Sum of numbers:", total)
    print("Square root of sum:", math.sqrt(total))

except Exception as e:
    print("Something went wrong:", e)


    