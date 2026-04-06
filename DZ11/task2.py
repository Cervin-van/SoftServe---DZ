def determine_day_of_week():
    user_input = input("Please enter a number (1-7) to get the day of the week: ")
    
    try:
        day_num = int(user_input)
        
        days_mapping = {
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"
        }
        
        if day_num in days_mapping:
            print(f"The day of the week is {days_mapping[day_num]}.")
        else:
            # Handles cases like 0, negative numbers, or 8 and more
            print("Error: The number is out of range. Please enter a number between 1 and 7.")
            
    except ValueError:
        # Handles cases with non-numerical data
        print("Error: You entered non-numerical data. Please enter a valid integer.")

if __name__ == "__main__":
    determine_day_of_week()
