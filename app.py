from datetime import datetime

# Ask the user for their date of birth
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

# Get today's date
today = datetime.now()

# Calculate age
age = today.year - birth_year

# Check if birthday has happened this year
if (today.month, today.day) < (birth_month, birth_day):
    age -= 1

print("\nYour date of birth:", birth_year, birth_month, birth_day)
print("Today's date:", today.strftime("%Y-%m-%d"))
print("Your age is:", age, "years")