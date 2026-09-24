# Age Calculator 🧮

A simple Python-based **Age Calculator** that calculates a person's current age using their date of birth and the current date.

This project is beginner-friendly and demonstrates how to work with Python's built-in `datetime` module.

## 📌 Features

* Takes the user's date of birth as input
* Converts the input into a Python `datetime` object
* Gets the current date automatically
* Calculates the user's current age
* Displays the date of birth, today's date, and calculated age
* Uses only Python's built-in libraries

## 🛠️ Technologies Used

* **Python 3**
* **datetime module**
* **VS Code**
* **Git & GitHub**

## 📂 Project Structure

```text
Age-Calculator/
│
├── age_calculator.py
└── README.md
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Age-Calculator.git
```

### 2. Go to the project directory

```bash
cd Age-Calculator
```

### 3. Run the Python program

```bash
python age_calculator.py
```

## 💻 Example

After running the program:

```text
Enter your date of birth (YYYY-MM-DD): 2000-05-10

========== AGE CALCULATOR ==========
Date of Birth : 2000-05-10
Today's Date  : 2026-09-24
------------------------------------
Your Age      : 26 years
====================================
```

## 📚 Python Concepts Used

This project demonstrates several basic Python concepts:

### Importing a module

```python
from datetime import datetime
```

### Getting the current date and time

```python
today = datetime.now()
```

### Converting a string into a date

```python
birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
```

### Conditional statements

```python
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1
```

### Formatting dates

```python
birth_date.strftime("%Y-%m-%d")
```

## 🎯 Learning Objective

The main goal of this project is to understand how Python handles **dates and times** using the `datetime` module.

It is a small project designed for beginners who are learning Python and want to practice working with user input, date conversion, conditions, and calculations.

## 🔮 Future Improvements

Some possible improvements for this project are:

* Calculate age in years, months, and days
* Calculate the number of days until the next birthday
* Add input validation
* Add a graphical user interface (GUI)
* Add a web interface using Flask or Streamlit
* Add unit tests

## 👨‍💻 Author

**Amit Kumar Singh**

This project was created as part of my Python learning journey.

## 📄 License

This project is open-source and available for learning and educational purposes.
