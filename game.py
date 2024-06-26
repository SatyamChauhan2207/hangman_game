import random

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def display_hangman(tries):
    hangman = [
        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========\n",
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========\n",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========\n",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========\n",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========\n",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========\n",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n=========\n"
    ]
    print(hangman[tries])

def hangman():
    words = {
        "apple": "A fruit that is red or green",
        "banana": "A long, curved fruit that is yellow when ripe",
        "cat": "A small, furry animal that is often kept as a pet",
        "dog": "A domesticated mammal with four legs and a tail",
        "bird": "A warm-blooded egg-laying vertebrate with feathers",
        "tree": "A woody perennial plant with branches and leaves",
        "car": "A road vehicle, typically with four wheels, powered by an internal combustion engine",
        "book": "A written or printed work consisting of pages glued or sewn together along one side",
        "sun": "The star around which the Earth orbits"
    }

    word = random.choice(list(words.keys()))
    hint = words[word]

    guessed_letters = []
    tries = 0
    max_tries = 6

    print("******************************")
    print("Welcome to Hangman Game!")
    print("******************************")
    print("Hint: ", hint)

    while tries < max_tries:
        display_hangman(tries)

        print("correct guesses:", " ".join(guessed_letters))

        print(display_word(word, guessed_letters))

        guess = input("Enter your guess: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            print("Correct!")
            guessed_letters.append(guess)
            if "_" not in display_word(word, guessed_letters):
                print("Congratulations! You've won.")
                print("You saved the man from being hanged!!!")
                break
        else:
            print("Incorrect!")
            tries += 1

    if tries == max_tries:
        display_hangman(tries)
        print("Sorry, you've lost.")
        print("The word was:", word)
        print("You couldn't save the man from being hanged!!!")

if __name__ == "__main__":
    hangman()
