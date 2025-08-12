# Function calculate_square(number) that takes a number as an argument and returns its square.


num = float(input("Enter the number to calculate its square: ")) # For all type of number int and flaot
def calculate_square(number):
    return number ** 2
print(f"The square of",num,"is",calculate_square(num))