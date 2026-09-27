"""
Module 2 — Lesson 4: Functions 
Student: Lovendin Jade Montero
Date: 09/27/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
A function is a block of code that performs a specific task and where you can write your logic.
We can create a function once and use it many times in our program.
Functions help make code easier to understand, efficient and organized, so you wont have to
write the same code repeatedly.


============================================
KEY VOCABULARY
============================================
- function: A block of code that performs a specific task
- parameter: A value that a function expects to receive
- argument: The actual value given to a function
- return: Sends a result or value back from a function
- function call: The action of running a function
- def: The keyword used to create a function in Python
- local variable: A variable that can only be used inside a function


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---
def remaining_money(money, spent):
    return money - spent

left = remaining_money(500, 150)
print("Money left:", left)

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]
One mistake I want to avoid is forgetting to call the function. If I don't call the function, the code inside it will not run.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
Functions can help me make my programs shorter and easier to manage. I can use functions when I have a task that I need to do many times.
"""
