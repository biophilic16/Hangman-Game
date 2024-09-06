#importing required packages
import random 
from hangman_word import word_list
from hangman_art import stages,logo

#printing hangman logo
print(logo)
print()

#choosing random word
random_word=random.choice(word_list)

#printing underscore
und_word=""
for i in range(len(random_word)):
    und_word+="_"
print("Word to guess:"+und_word) 
print("\n")    
lives=6
ply_won=False
correct_letters=[]

#main loop for getting values
while not ply_won:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess_word=input("guess a letter: ").lower()
    if guess_word in correct_letters:
        print(f"You've already guessed {guess_word}")

    #checking the input character   
    display=''
    for i in random_word:
        if i==guess_word:
            display=display+i
            correct_letters.append(guess_word)
        elif i in correct_letters:
            display+=i    
        else:
            display=display+'_'  
             
    print("Word to guess:"+display)
    
    #print lives and game over
    if guess_word not in random_word:
        lives-=1 
        print(f"You guessed {guess_word}, that's not in the word. You lose a life.")
        if lives==0:
            ply_won=True 
            print(f"***********************IT WAS -->{random_word}<-- YOU LOSE**********************")   

    #print if player won
    if '_' not in display:
        print("\n****************************YOU WIN****************************")
        ply_won=True

    #print stages of hangman
    print(stages[lives])     

    