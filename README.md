# Typing Speed Test in Python

A simple beginner-friendly Python project that measures:

- Typing Speed (WPM)
- Total Typing Time
- Typing Errors

This project is built using basic Python concepts and is great for beginners learning Python fundamentals.

# Features

- Typing Speed Calculation (WPM)
- Error Detection
- Time Tracking
- Beginner Friendly Code
- Simple Console-Based Program

# Technologies Used

- Python
- Time Module

# How It Works

1. The program displays a sentence.
2. The user types the sentence.
3. The timer starts automatically.
4. The program calculates:
   - Total time taken
   - Words per minute (WPM)
   - Total typing errors

# Project Code

```python
import time

# Sentence for typing
sentence = "Python is easy and fun to learn"

# Show sentence
print("Type this sentence:")
print(sentence)

# Start time
start_time = time.time()

# User input
typed_text = input("Type your sentence: ")

# End time
end_time = time.time()

# Total time
total_time = end_time - start_time

# WPM calculation
words = len(typed_text.split())
minutes = total_time / 60

if minutes > 0:
    wpm = round(words / minutes)
else:
    wpm = 0

# Error calculation
errors = 0

for i in range(min(len(typed_text), len(sentence))):
    if typed_text[i] != sentence[i]:
        errors += 1

# Extra characters count as errors
errors += abs(len(sentence) - len(typed_text))

# Output
print("------- Results -------")
print("Time Taken:", round(total_time, 2))
print("WPM:", wpm)
print("Errors:", errors)
```
# Example Output

```text
Type this sentence:
Python is easy and fun to learn

Type your sentence: Python is easy and fun to learn

------- Results -------
Time Taken: 8.42
WPM: 43
Errors: 0
```
# Concepts Used

- Variables
- Strings
- Loops
- Conditions
- Functions
- Time Module
- String Comparison
- Error Calculation

# Author

Zoya Sarwar
