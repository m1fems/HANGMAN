play_again = ''
word_guessed = False
while play_again.upper() != 'N':
    word = input('What is going to be the word: ')
    print('\n')
    print('_______________')
    print('|      |')
    print('|      |')
    print('|      |')
    print('|      |')
    print('|      |')
    print('|   --------')
    print('|  |        |')
    print('|  |  X  X  |')
    print('|  |        |')
    print('|  |  ----  |')
    print('|   --------')
    print('|      |')
    print('|      |')
    print('|      |')
    print('|      |')
    print('| -----|-----')
    print('|      |')
    print('|      |')
    print('|      |')
    print('|      |')
    print('|      |')
    print('| -----------')
    print('| |         |')
    print('| |         |')
    print('| |         |')
    print('| |         |')
    print('| |         |')
    coded_word = []
    guess_list = []
    guessed_letters = []
    lives = 9
    for letter in word.lower():
        coded_word.append(letter.lower())
    for i in range(len(word)):
        if word[i].lower() == word[0].lower() or word[i].lower() == word[-1].lower():
            guess_list.append(word[i])
        else:
            guess_list.append('_')
    print(guess_list)
    while guess_list.__contains__('_'):
        while True:
            guess = input("Guess a letter: ")
            if guess.lower() == word.lower():
                word_guessed = True
                break
            elif len(guess) > 1:
                print('Please write a letter')
                pass
            else:
                break
        if word_guessed:
            break
        if guessed_letters.__contains__(guess):
            print("Letter already guessed")
            print(f'Letters guessed: {guessed_letters}')
        else:
            if coded_word.__contains__(guess.lower()):
                cnt = 0
                for i in coded_word:
                    if i.lower() == guess.lower():
                        guess_list[cnt] = guess.lower()
                    cnt += 1
                print(guess_list)
                pass
            else:
                lives -= 1
                print(f'Lives remaining {lives}')
                print(guess_list)
                pass
            if lives == 0:
                print("You don't have any more lives")
                print(f'The word was {word}')
                quit()
            guessed_letters.append(guess)
    print('Congratulations you guest the word')
    word_guessed = False
    while True:
        play_again = input('Do you want to play again (Y/N): ').upper()
        if play_again == 'Y':
            break
        elif play_again == 'N':
            break
        else:
            print('Wrong input try again')
            pass
