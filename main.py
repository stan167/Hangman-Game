import random

def guess_word(word):
    guess = input("What do you think the word is? ")
    if guess == word:
        return("y")
    else:
        return("n")

def guess_letter(word_as_list, list):
    guess = input("What letter do you want to guess? ")
    if guess not in word_as_list:
        list.append(guess)
        return("n")
    else:
        while True:
            if guess in word_as_list:
                word_as_list.remove(guess)
                letters_guessed.append(guess)
            else:
                return("y")

def show_info(letters_guessed, lives):
    print(f"You have guessed {letters_guessed}!")
    print(f"You have {lives} lives left!")
    
    
    

words = ["jazz", "horse", "radish", "school", "coding", "bear", "computer"]
letters_guessed_wrong = []

print("Welcome to my Hangman Game!")
word = random.choice(words)
word_as_list = []
letters_guessed = []
for i in range(0, len(word)):
    word_as_list.append(word[i])
lives = 10
print(f"You have {lives} live(s)!")
while True:
        print(f"The word is {len(word)} letter(s) long in total.")
        print("\n")
        choice = input("Do you want to:\nguess a word (w)\nor guess a letter (l)\nChoice: ").lower()
        if choice == "w":
            word_outcome = guess_word(word)
            if word_outcome == "y":
                print(f"Nice!, You got the word with {lives} lives left!")
                break
            else:
                print("Unlucky, wrong word!")
                lives -= 1
                if lives == 0:
                     print("Unlucky, you are out of lives!")
                     break
        elif choice == "l":
            print(f"You have already incorrectly guessed {letters_guessed_wrong}!")
            letter_outcome = guess_letter(word_as_list, letters_guessed_wrong)
            if letter_outcome == "y":
                print("Nice, you removed a/some letter(s)!")
                if word_as_list != 0:
                    show_info(letters_guessed, lives)
                else:
                    print(f"Nice!, You got the word with {lives} lives left!")
                    break
            else:
                 print("Unlucky, wrong letter!")
                 lives -= 1
                 if lives == 0:
                     print("Unlucky, you are out of lives!")
                     print(f"The word was {word}!")
                     break
                 else:
                     show_info(letters_guessed, lives)
        else:
            print("Please enter a valid letter (w or l)")
