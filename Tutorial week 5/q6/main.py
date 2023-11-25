secret = input("Enter secret word:")
length = len(secret)
turns = length+1
print("Let's play Guess the Word")
print(f"You have {turns} turns to guess the word correctly!")

guesses = []
guess = ''

msg = "_" * length
print(msg)

for count in range (turns):
    guess = input("Enter a guess:").lower()
    guess = guess[0]
    
    if count > 0 :
        if guess in guesses:
            print(f"you already guessed letter {guess}! try differnt one.")
            
    

    if guess in secret:
        loc = secret.index(guess)
        msg = msg[:loc] + guess + msg[loc +1:]
        print(msg)
        print("correct guess")
        guesses.append(guess)
        if msg == secret:
            print("congratulations!you have won!")
            print(f"you have used {count+1} turns to guess the word correctly!")
            exit()
    else:
        print(f"Incorrect guess,you have {turns-(count+1)} guess(es) remaing.")
        
if msg != secret:
    print("sorry!no more guesses left,you lost")
    exit()
