from datetime import datetime

def get_user_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def is_adult(age):
    return age >= 18

def can_retire_next_year(birthdate):
    today = datetime.today()
    next_year_same_day = today.replace(year=today.year + 1)
    age_next_year = next_year_same_day.year - birthdate.year - ((next_year_same_day.month, next_year_same_day.day) < (birthdate.month, birthdate.day))
    return age_next_year >= 59

birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_input, "%Y-%m-%d")


age = get_user_age(birthdate)

adult_or_child = "Adult" if is_adult(age) else "Child"
retirement_eligibility = "Yes" if can_retire_next_year(birthdate) else "No"


print(f"Your age: {age} years")
print(f"You are an {adult_or_child}.")
print(f"Can you retire next year on the same day? {retirement_eligibility}")
