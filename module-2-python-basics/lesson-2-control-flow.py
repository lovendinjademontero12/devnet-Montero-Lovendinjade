"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Lovendin Jade Montero
Date: 09/27/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[write your own explanation here]
Control flow is used to make the program decide what to do.
We can use if, elif, and else to check different conditions.
If the condition is true, the code will run. If it is not true,
the program can check another condition or run the else part.
This helps the program make different decisions depending on
the situation.

============================================
KEY VOCABULARY
============================================
- condition: A rule or situation that the program checks.
- if: Checks if a condition is true.
- elif: Checks another condition if the first one is false.
- else: Runs when none of the conditions are true.
- comparison operator: A symbol used to compare values, like ==, >, or <.
- boolean expression: An expression that results in True or False.
- True: Means that a condition is correct.
- False: Means that a condition is not correct.

============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---
signal = 3

if signal >= 4:
    print("Internet is fast.")
elif signal >= 2:
    print("Internet is okay.")
else:
    print("Internet is slow.")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]
One mistake I want to avoid is using the wrong comparison
operator. I also need to remember to use the correct indentation
because Python uses indentation to know which code belongs to
the condition.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
Control flow can be useful in everyday programs because the
program needs to make decisions.
"""
