def sum_of_cubes(n):
    return sum([i**3 for i in range(1, n)])

# Example usage:
number = int(input("Enter a positive integer: "))
print("Sum of cubes:", sum_of_cubes(number))
