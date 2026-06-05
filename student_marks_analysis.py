import numpy as np

# Student marks: rows = students, columns = subjects
marks = np.array([
    [85, 90, 78],
    [70, 65, 80],
    [95, 88, 92],
    [40, 55, 60],
    [75, 82, 79]
])

students = np.array(["Hari", "Ravi", "Asha", "Ram", "Priya"])
subjects = np.array(["Maths", "Science", "English"])

print("Student Marks:")
print(marks)

# 1. Total marks of each student
total_marks = np.sum(marks, axis=1)
print("\nTotal Marks of Each Student:")
print(total_marks)

# 2. Average marks of each student
average_marks = np.mean(marks, axis=1)
print("\nAverage Marks of Each Student:")
print(average_marks)

# 3. Highest marks of each student
highest_marks = np.max(marks, axis=1)
print("\nHighest Marks of Each Student:")
print(highest_marks)

# 4. Lowest marks of each student
lowest_marks = np.min(marks, axis=1)
print("\nLowest Marks of Each Student:")
print(lowest_marks)

# 5. Subject-wise average
subject_average = np.mean(marks, axis=0)
print("\nSubject-wise Average:")
print(subject_average)

# 6. Topper
topper_index = np.argmax(total_marks)
print("\nTopper:")
print(students[topper_index], "with", total_marks[topper_index], "marks")

# 7. Students who passed
# Pass condition: average >= 60
passed_students = students[average_marks >= 60]
print("\nPassed Students:")
print(passed_students)

# 8. Students who failed
failed_students = students[average_marks < 60]
print("\nFailed Students:")
print(failed_students)

# 9. Grade calculation
print("\nGrades:")

for i in range(len(students)):
    avg = average_marks[i]

    if avg >= 90:
        grade = "A+"
    elif avg >= 80:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    else:
        grade = "Fail"

    print(students[i], "Average:", avg, "Grade:", grade)
