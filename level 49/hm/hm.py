def best_student():
    # სტუდენტების სახელები
    students_names = ["მარიამი", "კარლო", "ნიკა", "ანა", "თამარი"]
    students = {}

    for name in students_names:
        grades = input(f"შეიყვანეთ {name}-ის ნიშნები, გაწვდილი სივრცით: ")
        grades = list(map(float, grades.split()))

        average = sum(grades) / len(grades) if grades else 0
        students[name] = average

    if students:
        best = max(students, key=students.get)
        print(f"საუკეთესო სტუდენტი: {best} (საშუალო ნიშანი: {students[best]:.2f})")
    else:
        print("არაფერი არ იქნა შეყვანილი.")

best_student()
