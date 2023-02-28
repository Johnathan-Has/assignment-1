import time
# In Python, you can accept user input via the `input` function like so:

# ```python
# x = input("Enter your age in years: ")
# print(f"You are {x} years old")
# ```

# **Create a timer program where the user will input a number of seconds and then a count down will begin.**

# Example:

# ```
# >>> # of seconds: 10
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# Ding!

def countdown(t):

    while t > 0:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('It hurts when I pee')

t=input("Time in seconds:")

countdown(int(t))
