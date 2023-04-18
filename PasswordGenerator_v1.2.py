import random

class PasswordGenerator:
    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
        self.capletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '$', '%', '&','*', '+']
        self.fulllist = self.letters + self.numbers + self.symbols + self.capletters

    def generate_password(self, n_characters):
        passwordlist = []
        for i in range(n_characters):
            passwordlist.append(random.choice(self.fulllist))
        random.shuffle(passwordlist)
        password = ""
        for item in passwordlist:
            password += item
        return password

def main():
    print("Welcome to quick password generator")
    password_generator = PasswordGenerator()
    while True:
        proceed_question = input("Would you like to generate a password?? ").lower()
        if proceed_question in ("no", "n", ""):
            break
        elif proceed_question in ( "yes", "y"):
            n_characters = int(input("How many characters would you like in your password? Please enter a number: "))
            password = password_generator.generate_password(n_characters)
            print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
