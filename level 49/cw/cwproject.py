def main():
    students = ["გიო", "საბა", "ანდრია", "სანდრო", "ლუკა"]
    scores = {student: [] for student in students}

print(გიო: 85, 90, 78)
print(საბა: 88, 92, 95)
print(ანდრია: 75, 80, 82)
print( სანდრო: 95, 100, 98)
print(ლუკა: 70, 75, 80)

    while True:
        entry = input("შეიყვანეთ მონაცემები: ")
        if entry.lower() == 'დასრულება':
            break
        
        try:
            name, score_str = entry.split(':')
            name = name.strip()
            scores_list = list(map(float, score_str.split(',')))

            if name in scores:
                scores[name].extend(scores_list)
            else:
                print(f"{name} არ არის სტუდენტების სიაში.")
        except ValueError:
            print("გთხოვთ, შეიტანოთ მონაცემები სწორ ფორმატში.")

    # საშუალო ნიშნების გამოთვლა
    averages = {}
    for student, score_list in scores.items():
        if score_list:  # თუ არის ნიშნები
            average_score = sum(score_list) / len(score_list)
            averages[student] = average_score

    # საუკეთესო სტუდენტის განსაზღვრა
    if averages:
        best_student = max(averages, key=averages.get)
        best_score = averages[best_student]
        print(f"საუკეთესო სტუდენტი: {best_student} - საშუალო ნიშანი: {best_score:.2f}")
    else:
        print("არ არსებობს სტუდენტები.")

if __name__ == "__main__":
    main()
