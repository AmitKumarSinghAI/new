from datetime import datetime


# Get date of birth from the user
birth_date = input("Enter your date of birth (YYYY-MM-DD): ")

# Convert string to datetime object
birth_date = datetime.strptime(birth_date, "%Y-%m-%d")

# Get today's date
today = datetime.now()

# Calculate age
age = today.year - birth_date.year

# Check if birthday has happened this year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

# Display result
print("\n========== AGE CALCULATOR ==========")
print("Date of Birth :", birth_date.strftime("%Y-%m-%d"))
print("Today's Date  :", today.strftime("%Y-%m-%d"))
print("------------------------------------")
print("Your Age      :", age, "years")
print("====================================")