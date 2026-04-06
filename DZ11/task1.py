def process_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    
    if age % 2 == 0:
        return "even"
    else:
        return "odd"

def main():
    user_input = input("Please enter your age: ")
    try:
        age_int = int(user_input)
        result = process_age(age_int)
        print(f"Your age ({age_int}) is {result}.")
    except ValueError as e:
        print(f"Error encountered: {e}")

if __name__ == "__main__":
    main()
