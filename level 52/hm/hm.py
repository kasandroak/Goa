#codewars !!!
def area_or_perimeter(length, width):
    if length == width:
        return length * width  # Area of the square
    else:
        return 2 * (length + width)  # Perimeter of the rectangle

# Example test cases
print(area_or_perimeter(4, 4))   # Output: 16 (Area of square)
print(area_or_perimeter(6, 10))  # Output: 32 (Perimeter of rectangle)