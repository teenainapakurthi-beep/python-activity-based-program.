
students = []

n = int(input("Enter number of applicants: "))

for i in range(n):
    print("\nEnter details for applicant", i + 1)

    name = input("Student name: ")

    m1 = float(input("Subject 1 marks: "))
    m2 = float(input("Subject 2 marks: "))
    m3 = float(input("Subject 3 marks: "))

    attendance = float(input("Attendance percentage: "))
    income = float(input("Annual family income: "))

    aggregate = (m1 + m2 + m3) / 3

    if (aggregate >= 75 and m1 >= 60 and m2 >= 60
            and m3 >= 60 and attendance >= 75
            and income <= 250000):

        students.append(
            [name, aggregate, attendance, income]
        )

# Rank eligible students
students.sort(key=lambda x: (-x[1], -x[2], x[3]))

print("\n--- Scholarship Selection Results ---")

if len(students) == 0:
    print("No eligible students found.")
else:
    for i in range(len(students)):
        print("\nRank:", i + 1)
        print("Name:", students[i][0])
        print("Aggregate:", round(students[i][1], 2), "%")
        print("Attendance:", students[i][2], "%")
        print("Family Income: Rs.", students[i][3])
