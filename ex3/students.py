import csv

def student_login(username, password):
    with open("users.csv", mode="r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == username:
                if row[1] == password:
                    return True
                else:
                    print("Wrong Password. Please enter the correct password.")
                    return False
        print("Username not found")
        return False

def load_questions():
    questions = []
    try:
        with open("questions.csv", mode="r") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 2:
                    questions.append(row)
                else:
                    pass
    except FileNotFoundError:
        print("Error")
    return questions

def load_options(question_id):
    options = []
    try:
        with open("options.csv", mode="r") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 4 and row[0] == question_id:
                    options.append(row)
                else:
                    pass
    except FileNotFoundError:
        print("Error")
    return options

def take_exam(username):
    questions = load_questions()
    if not questions:
        print("No questions available")
        return
    
    total_questions = len(questions)
    correct_answers = 0
    
    for i in range(total_questions):
        question_id = questions[i][0]
        question_text = questions[i][1]
        print(f"\nQuestion {i+1}: {question_text}")
        
        options = load_options(question_id)
        
        for option in options:
            print(f"{option[1]}: {option[2]}")
        
        answer = input("Enter your answer (A/B/C/D): ").upper()
        
        correct_answer = None
        for option in options:
            if option[3] == "True":
                correct_answer = option[1]
                break
        
        if correct_answer and correct_answer == answer:
            print("Correct answer.")
            correct_answers += 1
        else:
            print("Wrong answer.")
    
    score = (correct_answers / total_questions) * 100
    print(f"\nYour result: {score}% Passed.")
    
    update_student_result(username, score)

def update_student_result(username, score):
    rows = []
    updated = False
    
    with open("users.csv", mode="r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == username:
                if len(row) > 2:
                    row[2] = f"{score}%"
                else:
                    row.append(f"{score}%")
                updated = True
            rows.append(row)
    
    if not updated:
        print(f"User '{username}' not found.")
        return
    
    with open("users.csv", mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

def main():
    while True:
        print("\nWelcome to Exam Application - Student Login")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        if student_login(username, password):
            print("Login successful.")
            take_exam(username)
            break

if __name__ == "__main__":
    main()
