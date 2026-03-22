from function import circle_area, triangle_area, rectangle_area


def main():
    try:
        print("Ведіть що хочете обчислити")
        print("1. Площа круга")
        print("2. Площа трикутника")
        print("3. Площа прямокутника")

        choice = int(input("Ваш вибір: "))

        if choice == 1:
            r = float(input("Введіть радіус: "))
            print("Площа круга: ", circle_area(r))
        elif choice == 2:
            a = float(input("Введіть довжину катета А: "))
            b = float(input("Введіть довжину катета Б: "))
            print("Площа трикутника: ", triangle_area(a, b))
        elif choice == 3:
            a = float(input("Введіть довжину сторони А: "))
            b = float(input("Введіть довжину сторони Б: "))
            print("Площа прямокутника: ", rectangle_area(a, b))
    except ValueError:
        print("Невірний ввід")


if __name__ == "__main__":
    main()
