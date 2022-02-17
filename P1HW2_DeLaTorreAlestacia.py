# Python program to execute a students pizza order and determine how \n
# many pizza slices per student is needed.
# 20220216
# CTI-110 P1HW2 - Pizza Order
# De La Torre, Alestacia
#

# the amount of students
student_number = int(input('How many students do you want to order pizza for? '))

# Each student gets 3 slices, so you multiply 3 by the number of students.
slice_needed = student_number * 3

# every 2 students gets 1 pizza, so you divide 2 by the number of students.
pizza_number = student_number / 2

print('----Pizza Order-------')
print('Number of Students:', student_number)  # Number of students
print('Pizza Slices Needed:', slice_needed)  # product of slices needed
print('Pizzas Needed: ', pizza_number)  # The quotient of pizzas needed
print('-------------------------')
