# ==========================================
#            QUIZ GAME
#      Industrial Internship Project
# ==========================================

print("=" * 50)
print("         WELCOME TO QUIZ GAME")
print("=" * 50)

name = input("Enter your name: ")

print(f"\nHello, {name}! Welcome to the Quiz Game.")

print("\nInstructions:")
print("1. The quiz contains 10 multiple-choice questions.")
print("2. Each correct answer gives you 1 mark.")
print("3. There is no negative marking.")
print("4. Enter only A, B, C, or D as your answer.")
print("5. Your result will be shown at the end.")

input("\nPress Enter to start the quiz...")
# Questions
questions = [
    {
        "question": "1. What is the correct extension of Python files?",
        "options": ["A. .py", "B. .java", "C. .cpp", "D. .html"],
        "answer": "A"
    },
    {
        "question": "2. Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    },
    {
        "question": "3. Which function is used to take input from the user?",
        "options": ["A. print()", "B. input()", "C. scan()", "D. read()"],
        "answer": "B"
    },
    {
        "question": "4. Which data type is used to store True or False?",
        "options": ["A. int", "B. float", "C. bool", "D. str"],
        "answer": "C"
    },
    {
        "question": "5. Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!--", "C. #", "D. **"],
        "answer": "C"
    },
    {
        "question": "6. Which loop is used to iterate over a sequence?",
        "options": ["A. while", "B. do while", "C. for", "D. repeat"],
        "answer": "C"
    },
    {
        "question": "7. Which data structure stores key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
        "answer": "C"
    },
    {
        "question": "8. Which function displays output on the screen?",
        "options": ["A. print()", "B. input()", "C. display()", "D. write()"],
        "answer": "A"
    },
    {
        "question": "9. Which operator is used for multiplication?",
        "options": ["A. +", "B. /", "C. *", "D. %"],
        "answer": "C"
    },
    {
        "question": "10. Which keyword is used for conditional statements?",
        "options": ["A. switch", "B. if", "C. case", "D. loop"],
        "answer": "B"
    }
]

score = 0
question_number = 1

for q in questions:
    print("\n" + "=" * 50)
    print(f"Question {question_number} of {len(questions)}")
    print(q["question"])

    for option in q["options"]:
        print(option)

    while True:
        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        if user_answer in ["A", "B", "C", "D"]:
            break
        else:
            print("❌ Invalid input! Please enter A, B, C or D.")

    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong!")
        print("Correct Answer:", q["answer"])
    question_number += 1

print("\n" + "=" * 50)
print("              QUIZ RESULT")
print("=" * 50)

total_questions = len(questions)
percentage = (score / total_questions) * 100

print(f"Name        : {name}")
print(f"Score       : {score}/{total_questions}")
print(f"Percentage  : {percentage:.2f}%")

if percentage >= 90:
    grade = "A+"
    remark = "Excellent!"
elif percentage >= 75:
    grade = "A"
    remark = "Very Good!"
elif percentage >= 60:
    grade = "B"
    remark = "Good Job!"
elif percentage >= 40:
    grade = "C"
    remark = "Needs Improvement!"
else:
    grade = "F"
    remark = "Better Luck Next Time!"

print(f"Grade       : {grade}")
print(f"Remark      : {remark}")

if percentage >= 40:
    print("\n🎉 Congratulations! You Passed the Quiz.")
else:
    print("\n❌ Sorry! You Failed the Quiz.")

print("=" * 50)
print("Thank you for playing the Quiz Game!")
print("=" * 50)
while True:
    choice = input("\nDo you want to play again? (Y/N): ").upper()

    if choice == "Y":
        print("\nPlease run the program again to play another quiz.")
        break
    elif choice == "N":
        print("\nThank you! Have a great day.")
        break
    else:
        print("❌ Invalid choice! Please enter Y or N.")