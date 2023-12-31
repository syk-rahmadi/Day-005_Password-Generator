# Input a list of student scores
student_scores = input("Give input students score! ").split()
for score in range(0, len(student_scores)):
  student_scores[score] = int(student_scores[score])

# Write your code below this row 👇

print(f"Student scores are {student_scores}")

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is {highest_score}")
