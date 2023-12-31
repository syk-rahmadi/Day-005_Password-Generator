# Input a Python list of student heights
student_heights = input("Write students height...").split()
for student in range(0, len(student_heights)):
    student_heights[student] = int(student_heights[student]) #This line is for making a list

total_height = 0
for height in student_heights: #creating for loop to add all components in a list
    total_height += height
print(f"Total height of students {total_height}")

number_of_students = 0
for student in student_heights: #creating for loop to add all components in a list
    number_of_students += 1 #Since python count from 0, there is necessity for counting adjustmet with adding 1
print(f"Total number of students {number_of_students}")

average_height = total_height / number_of_students
print(f"Average height of students {average_height}")