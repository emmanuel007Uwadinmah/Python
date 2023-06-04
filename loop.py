"""
student_height = input(" Input a list of student heights ").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)
total = 0
for size in student_height:
    total += size
print(total)
    
number = 0
for student in student_height:
    number += 1
print(number)

average = round(total / number)
print(average)

student_score = input(" Input a list of student scores ").split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

highest_score = 0
for score in student_score:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")

total = 0
for number in range (0, 101, 2):
    total += number
print(total)

for number in range (1, 101):
    if number % 3 == 0 and number % 5 == 0:
       print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    
    else:
        print(number)
"""
 










