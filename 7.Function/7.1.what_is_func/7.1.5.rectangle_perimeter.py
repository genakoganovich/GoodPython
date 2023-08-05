def calc_perimeter(width, height):
    print(f"Периметр прямоугольника, равен {2 * (width + height)}")


calc_perimeter(*map(int, input().split()))
