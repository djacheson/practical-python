# bounce.py
#
# Exercise 1.5

start_height = 100
for i in range(11):
    if i == 0:
        curr_height = start_height
    else:
        curr_height = curr_height * (3/5)
        print(f"{i} {round(curr_height, 4)}")
