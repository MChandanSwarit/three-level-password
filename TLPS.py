import random
import re

class User:
    def __init__(self, username, password, security_questions):
        self.username = username
        self.password = password
        self.security_questions = security_questions  # Dictionary of security questions and answers
        self.otp = None

    def generate_otp(self):
        self.otp = random.randint(100000, 999999)
        print(f"An OTP has been sent to your registered contact. (For simulation, OTP: {self.otp})")
        return self.otp

    def verify_password(self, password):
        return self.password == password

    def verify_security_answers(self, answers):
        return self.security_questions == answers

    def verify_otp(self, otp):
        return self.otp == otp

class AuthSystem:
    def __init__(self):
        self.users = {}
        self.security_questions = [
            "What is your school's name?",
            "What is your pet's name?",
            "What is your mother's maiden name?",
            "What is your favorite color?",
            "What city were you born in?",
            "What was the name of your first teacher?",
            "What is your favorite food?",
            "What is your favorite movie?",
            "What was your first car?",
            "What is your father's middle name?"
        ]

    def register_user(self, username, password):
        if username in self.users:
            print(f"User '{username}' already exists.")
        else:
            if self.validate_password(password):
                # Select 2 random security questions
                selected_questions = random.sample(self.security_questions, 2)
                security_answers = {}
                for question in selected_questions:
                    answer = input(f"{question} ")
                    security_answers[question] = answer.lower()

                self.users[username] = User(username, password, security_answers)
                print(f"User '{username}' registered successfully.")
            else:
                print("Password does not meet the required criteria. Registration failed.")

    def validate_password(self, password):
        # Password must be at least 8 characters long and contain both letters and numbers
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
            return False
        if not re.search("[a-zA-Z]", password):
            print("Password must contain at least one letter.")
            return False
        if not re.search("[0-9]", password):
            print("Password must contain at least one number.")
            return False
        return True

    def authenticate(self, username):
        if username not in self.users:
            print(f"User '{username}' not found.")
            return False

        user = self.users[username]

        # First-Level Authentication
        password = input("Enter your password: ")
        if not user.verify_password(password):
            print("Invalid password.")
            return False

        # Second-Level Authentication (Ask the same 2 questions asked during registration)
        security_answers = {}
        for question in user.security_questions.keys():
            answer = input(f"{question} ")
            security_answers[question] = answer.lower()

        if not user.verify_security_answers(security_answers):
            print("Incorrect answers to the security questions.")
            return False

        # Third-Level Authentication (OTP)
        otp = user.generate_otp()
        entered_otp = int(input("Enter OTP: "))
        if not user.verify_otp(entered_otp):
            print("Incorrect OTP.")
            return False

        print(f"User '{username}' authenticated successfully.")
        return True

def main():
    auth_system = AuthSystem()

    while True:
        print("\n--- Three-Level Password System ---")
        print("1. Register User")
        print("2. Authenticate User")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            auth_system.register_user(username, password)

        elif choice == '2':
            username = input("Enter username: ")
            auth_system.authenticate(username)

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
