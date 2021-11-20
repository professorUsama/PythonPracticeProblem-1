"""
    Author: Usama Amjid
    Purpose: Learning/practice
    Date: 20-November-2021
    Facebook Page: https://www.facebook.com/informationTechnology5256/
    YouTube Channel: https://www.youtube.com/channel/UC6NrVQEqUXQq4tHdDrfMipw
    Email: ith9055@gmail.com
    Problem Statement:  User input the birth-year or his age. The program tell the user  year that when he will be  100 years old.
    This program written in (python3.7)
"""

def check(number):
    """
    define function to detect the user input age or year... 
    """
    if len(str(number)) <= 3:
        return number
    else:
        if len(str(number)) <= 4:
            return number
        else:
            return f"invalid age or year...."

# main function 
if __name__ == '__main__':
    try:
        #initial a variable user_input where the user give his age or birth year
        user_input = int(input("Enter your age or birth_year: "))
        # current_year variable takes the current year... e.g current year is 2021
        current_year = int(input("Enter current year: "))
        #function calling which detect the user_input....
        value = check(user_input)
        if value >= 100 and len(str(value)) <= 3:
            if value == 100:
                print("you already 100 year old...")
            else:
                print("your age is 100 years above.. its mean you are very old man")
        elif value < 100:
            birth_year = current_year - value
            new_age = birth_year + 100
            remaining_age = new_age - current_year
            print(
                f"your birth year is: {birth_year}\nYour remaining age to complete 100 years old: {remaining_age}\nYour age will be 100 years in {new_age}")
        elif value >= current_year and len(str(value)) == 4:
            if value == current_year:
                print(
                    f"You born in this year...\nAnd Your age will be 100 years in {value+100}")
            else:
                print(f"You are not born yet...!")
        elif value < current_year and len(str(value)) == 4:
            print(f"Your age will be 100 years in {value+100}")
        else:
            print(f"Please input valid age or year...")
    except Exception as e:
        print(e)
