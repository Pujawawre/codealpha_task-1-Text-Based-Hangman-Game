# Hangman Game!!

import random

def main():
    # A list of welcome messages to introduce the game
    welcome = ['Welcome...Hangman!! Your goal is to figure out the hidden word by guessing one letter at a time ',
               'You have ten chances'," but don't worry if you guess a correct letter, it won't count against your attempts."
               ]

    # Print each line of the welcome message
    for line in welcome:
        print(line, sep='\n')

    # Boolean variable to control whether the player wants to play again
    play_again = True

    while play_again:
        # List of possible words for the game
        words = ["hangman", "engineer", "internship", "java", "software",
                 "designer", "placement", "program", "database", "game",
                 "project", "company", "website", "code", "resume","web",
                 "data", "react", "fresher", "aptitude", "python","codealpha"
                 ]

        # Randomly select a word from the above list
        chosen_word = random.choice(words).lower()

        # Initialize variables for the game
        player_guess = None  # Stores the current player's guess
        guessed_letters = []  # List to keep track of guessed letters
        word_guessed = []  # List to keep track of the word with correct guesses
        for letter in chosen_word:
            word_guessed.append("-")  # Initialize with dashes for each letter in the word

        joined_word = None  # Stores the current state of the word with guesses
        attempts = 10  # Number of attempts allowed

        while (attempts != 0 and "-" in word_guessed):
            # Display remaining attempts and current state of the word
            print(("\n\n\nAttempts Remaining: {}").format(attempts))
            joined_word = "".join(word_guessed)  # Convert list of guessed letters to a string
            print("Word: " + joined_word)

            try:
                # Prompt the player to enter a letter
                player_guess = str(input("\nType in a letter: ")).lower()
            except:
                # Handle any unexpected input errors
                print("That is not valid input. Please try again.")
                continue
            else:
                # Input validation
                if not player_guess.isalpha():  # Check if input is a letter
                    print("That is not a letter. Please try again.")
                    continue
                elif len(player_guess) > 1:  # Check if input is a single letter
                    print("That is more than one letter. Please try again.")
                    continue
                elif player_guess in guessed_letters:  # Check if letter was already guessed
                    print("You have already guessed that letter. Please try again.")
                    continue
                else:
                    pass  # Proceed with the valid input

            # Add the guessed letter to the list of guessed letters
            guessed_letters.append(player_guess)

            # Update the word with correct guesses
            for letter in range(len(chosen_word)):
                if player_guess == chosen_word[letter]:
                    word_guessed[letter] = player_guess

            # Reduce attempts if the guessed letter is not in the word
            if player_guess not in chosen_word:
                attempts -= 1

        # End of the game
        if "-" not in word_guessed:  # Check if the word has been fully guessed
            print(("\nCongratulations! You guessed the word, {}").format(chosen_word))
        else:  # Game ended due to running out of attempts
            print(("\n\You lose! The word was {}.").format(chosen_word))

        # Prompt the player to play again
        print("\nWould you like to play again?")

        response = input("> ").lower()
        # Check if the response indicates a desire to play again
        if response not in ("yes", "y", "yeah", "yep", "1", "ok"):
            play_again = False  # Exit the game loop
            exit()  # End the program

# Ensure the main function runs only if the script is executed directly
if __name__ == "__main__":
    main()

raw_input()
