
secret_word = "giraffe"
guess = ""
amt_of_guesses = 1
difficulty = input("What difficulty would you like to play? (Easy, Medium, Hard): ")
guess_limit = ""

if difficulty == "Easy":
    guess_limit = 5
elif difficulty == "Medium":
    guess_limit = 4
elif difficulty == "Hard":
    guess_limit = 3

while guess != secret_word and amt_of_guesses <= guess_limit:
    guess = input("Enter guess: ")
    amt_of_guesses += 1
if amt_of_guesses <= guess_limit:
    print("You win! The word was " + secret_word + ".")
else:
    print("You lose.")


