
def RectangleArea(a, b):
    return a * b

def TriangleArea(a, b):
    return 0.5 * a * b

def CircleArea(r):
    return 3.14 * r * r

try:
    print("Що ви хочете обчислити?")
    print("1. Площу прямокутника")
    print("2. Площу трикутника")
    print("3. Площу кола")
   
    choice = int(input("Введіть ваш вибір: "))
    if choice == 1:
        a = int(input("Введіть довжину сторони a: "))
        b = int(input("Введіть довжину сторони b: "))
        print("Площа прямокутника: ", RectangleArea(a, b))
    elif choice == 2:
        a = int(input("Введіть довжину сторони a: "))
        b = int(input("Введіть довжину сторони b: "))
        print("Площа трикутника: ", TriangleArea(a, b))
    elif choice == 3:
        r = int(input("Введіть радіус r: "))
        print("Площа кола: ", CircleArea(r))
    else:
        print("Неправильний вибір")
except ValueError:
    print("Будь ласка, введіть число")
    exit()


