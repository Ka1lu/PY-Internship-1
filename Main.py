import pandas as pd
import random as rm

df = pd.read_csv("words.csv")
adjectives = df["adjective"].tolist()
nouns = df["noun"].tolist()

maxlength = int(input("Please enter the maximum number of characters: "))
minlength = int(input("Please enter the minimum number of characters: "))

splchar = input("Enter your custom special sequence you wish to have in the name: ")

while True:
    try:
        structure = int(input("""
Enter 1 for NOUN , ADJECTIVE , SPECIAL CHARACTER
Enter 2 for NOUN , SPECIAL CHARACTER , ADJECTIVE
Enter 3 for ADJECTIVE , NOUN , SPECIAL CHARACTER
Enter 4 for ADJECTIVE , SPECIAL CHARACTER , NOUN
Enter 5 for SPECIAL CHARACTER , NOUN , ADJECTIVE
Enter 6 for SPECIAL CHARACTER , ADJECTIVE , NOUN
"""))
        if 1 <= structure <= 6:
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")
    except ValueError:
        print("Invalid input! Please enter a number.")

def generate_username():
    while True:
        random_noun = rm.choice(nouns)
        random_adjective = rm.choice(adjectives)

        match structure:
            case 1:
                generated = random_noun + random_adjective + splchar
            case 2:
                generated = random_noun + splchar + random_adjective
            case 3:
                generated = random_adjective + random_noun + splchar
            case 4:
                generated = random_adjective + splchar + random_noun
            case 5:
                generated = splchar + random_noun + random_adjective
            case 6:
                generated = splchar + random_adjective + random_noun

        if minlength <= len(generated) <= maxlength:
            return generated  
            
while True:
    try:
        count = int(input("How many usernames do you want to generate? (Enter a number): "))
        break
    except ValueError:
        print("Invalid input! Please enter a valid number.")

with open("usernames.txt", "a") as file:
    for _ in range(count):
        username = generate_username()
        file.write(username + "\n")
        print(f"Generated Username: {username}")

print("Usernames have been saved to usernames.txt.")
