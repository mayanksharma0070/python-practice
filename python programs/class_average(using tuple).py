# Program: Student Grades using Tuple

# Step 1: Store data using tuples
student1 = ("Ravi", (85, 90, 88))
student2 = ("Neha", (78, 82, 80))
student3 = ("Arjun", (92, 88, 95))

students = (student1, student2, student3)

# Step 2: Function to display individual reports
def display_report(students):
    print("----- Student Report -----")
    for s in students:
        name = s[0]
        marks = s[1]
        avg = sum(marks) / len(marks)
        print(f"Name: {name}")
        print(f"Marks: {marks}")
        print(f"Average: {avg:.2f}\n")

# Step 3: Function to calculate class average
def calculate_class_average(students):
    total = 0
    for s in students:
        marks = s[1]
        total += sum(marks) / len(marks)
    class_avg = total / len(students)
    return class_avg

# Step 4: Main program
display_report(students)
class_avg = calculate_class_average(students)
print("Class Average:", round(class_avg, 2))
