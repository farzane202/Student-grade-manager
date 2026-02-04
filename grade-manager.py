
def calculate_average(grades): 

    if not grades:
        return 0
    return sum(grades) / len(grades)

def main():
    student_grades = {}
    running = True

    while running:
        print("\n=== Student Grade Manager ===")
        print("1. Add a new student grade")
        print("2. Remove a student")
        print("3. Show all grades")
        print("4. Show average grade")
        print("5. Exit")

        option = input("Select an option (1-5): ")

        if option == "1":
            student_name = input("Enter student name: ")
            student_score = float(input("Enter grade: "))
            student_grades[student_name] = student_score
            print(f" {student_name}'s grade added!")
        elif option == "2":
            student_name = input("Enter student name to remove: ")
            if student_name in student_grades:
                student_grades.pop(student_name)
                print(f"{student_name} removed.")
            else:
                print("Student not found.")
        elif option == "3":
            if student_grades:
                print("\nAll student grades:")
                for name, score in student_grades.items():
                    print(f"{name}: {score}")
            else:
                print("No grades to show.")
        elif option == "4":
            avg = calculate_average(list(student_grades.values()))
            print(f" Average grade: {avg:.2f}")
        elif option == "5":
            print("Goodbye!")
            running = False
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()