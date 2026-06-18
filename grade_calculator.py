def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent Work! Keep shining! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good Job! You can do even better! 😊"
    elif marks >= 60:
        return "D", "Keep Working Hard! Success is near! 💪"
    else:
        return "F", "Don't Give Up! Practice more and try again! 📚"


student_name = input("Enter student name: ")


while True:
    try:
        marks = int(input("Enter marks (0-100): "))

        if 0 <= marks <= 100:
            break
        else:
            print("❌ Marks must be between 0 and 100. Try again.")

    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")


grade, message = calculate_grade(marks)


print("\n📊 RESULT FOR", student_name.upper())
print("Marks:", marks, "/100")
print("Grade:", grade)
print("Message:", message)
