import random as rnd

def hidden_word(word: str, letters: list) -> str:
    word_list = list(word)
    hword = [l if l in letters else "-" for l in word_list ]
    return "".join(hword)

def show_scoreboard():
    print(f"You won: {score} times.")
    print(f"You lost: {losts} times.")



words = ["python", "java", "swift", "javascript"]

# choose a pseudorandom word



score = 0
losts = 0

print("H A N G M A N")

message = 'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:'
choices = {"play", "results", "exit"}

while True:
    choice = input(message)
    if choice not in choices:
        continue

    if choice == "play":
        word_to_guess = rnd.choice(words)
        word_len = len(word_to_guess)
        letters = []
        attempts = 8

        while attempts > 0:
            print("")
            print(hidden_word(word_to_guess, letters))

            letter = input("Input a letter:")
            if len(letter) != 1:
                print("Please, input a single letter.")
                continue
            if letter.islower() != True:
                print("Please, enter a lowercase letter from the English alphabet.")
                continue

            if letter not in word_to_guess:
                print("That letter doesn't appear in the word.")
                attempts -= 1

            if letter in letters:
                print("You've already guessed this letter.")

            if letter not in letters:
                letters.append(letter)

            if hidden_word(word_to_guess, letters) == word_to_guess:
                print()
                print(f"{word_to_guess}")
                print(f"You guessed the word {word_to_guess}!")
                print("You survived!")
                score += 1
                break

        if hidden_word(word_to_guess, letters) != word_to_guess:
            print()
            print("You lost!")
            losts += 1

    elif choice == "results":
        show_scoreboard()

    else:
        break
