grades_total = 0
grades_counter = 1
actual_grade = 0
approved_grades = 0
failed_grades = 0
average_approved = 0.0
average_failed = 0.0
average_total = 0.0

print("Ingress the total amount of grades: ")
grades_total = int(input())
while grades_counter <= grades_total:
    print("Enter the grade: ")
    grade = int(input())

    if grade < 70:
        failed_grades += 1
        average_failed += grade
    else:
        approved_grades += 1
        average_approved += grade
    average_total += grade
    grades_counter += 1
    
average_failed = average_failed / failed_grades if failed_grades > 0 else 0.0
average_approved = average_approved / approved_grades if approved_grades > 0 else 0.0
average_total = average_total / grades_total if grades_total > 0 else 0.0

print(f"The student has approved the following amount of grades: {approved_grades}")
print(f"This is the average of the approved grades: {average_approved}")
print(f"The student has failed the following amount of grades: {failed_grades}")
print(f"This is the average of the failed grades: {average_failed}")
print(f"This is the average of all the grades: {average_total}")