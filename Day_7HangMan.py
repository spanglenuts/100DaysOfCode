#Step 5

import random
import hangman_art
import hangman_words

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6



#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

already_guessed = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
#    print(already_guessed)
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess not in already_guessed:      
      already_guessed.append(guess)
      for position in range(word_length):
          letter = chosen_word[position]
          #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
          if letter == guess:
              display[position] = letter
    else:
      print("You already Guessed that, Go again!")

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that is not in the word. You lose a life!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])
