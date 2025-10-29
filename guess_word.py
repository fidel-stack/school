import random

word_bank = ["rizz", "ohio", "sigma", "tiktok", "skibidi"] #A list
word = random.choice(word_bank) #Choose a random word from word_bank and then assign it to the variable word
guessedWord = ["_"] * len(word)
attempts = 10

#game loop
while attempts > 0:
  print("\nCurrent word:  " + " ".join(guessedWord))
    
  guess = input("Guess a letter: ").lower()
    
  if guess in word:
     for i in range(len(word)):
        if word[i] == guess:
            guessedWord[i] = guess
        print("Great guess")
  else:
      attempts -= 1
      print("Wrong guess! Attempts left: " + str(attempts))
  if "_" not in guessedWord:
      print("\nCOngratulations! you guessed the word: " + word)
      break

  if attempts == 0 and "_" in guessedWord:
        print("\nYou have run out of attemts! The word was" + word)                    