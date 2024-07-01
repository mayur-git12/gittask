import csv

def admin_login(username, password):
    with open("users.csv", mode="r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == username and row[1] == password:
                return True
    return False

def add_question(question_text):
    with open("questions.csv", mode="a", newline="") as f:
        writer = csv.writer(f)
        question_id = get_next_question_id()
        writer.writerow([question_id, question_text])
    return question_id

def add_options(question_id, options):
    with open("options.csv", mode="a", newline="") as f:
        writer = csv.writer(f)
        for option in options:
            writer.writerow([question_id, option[0], option[1], option[2]])

def get_next_question_id():
    with open("questions.csv", mode="r") as f:
        reader = csv.reader(f)
        data = list(reader)
        if data:
            return int(data[-1][0]) + 1
        else:
            return 1

def add_user(username, password):
    with open("users.csv", mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([username, password, ""])

def main():
    while True:
        print("\nAdmin Login")
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        
        if admin_login(username, password):
            print("Login successful.")
            break
        else:
            print("Invalid username or password. Please try again.")
    
    while True:
        print("\nWelcome Admin!")
        print("1. Add a new question")
        print("2. Add a new user")
        choice = input("Enter your choice (1/2): ")
        
        if choice == "1":
            question_text = input("Enter the question text: ")
            options = []
            for i in range(4):
                option_text = input(f"Enter option {chr(65 + i)}: ")
                options.append([chr(65 + i), option_text, False])
            
            correct_option = input("Enter the correct option (A/B/C/D): ").upper()
            for option in options:
                if option[0] == correct_option:
                    option[2] = True
            
            question_id = add_question(question_text)
            add_options(question_id, options)
            print("Question added successfully.")
        
        elif choice == "2":
            username = input("Enter the new username: ")
            password = input("Enter the new password: ")
            add_user(username, password)
            print("User added successfully.")
        
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
