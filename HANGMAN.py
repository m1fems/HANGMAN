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
lives = 9

for letter in word:
    coded_word.append(letter)
for i in range(len(word)):
    guess_list.append('_')

while guess_list.__contains__('_'):
    guess = input("Guess a letter: ")
    if coded_word.__contains__(guess):
        cnt = 0
        for i in coded_word:
            if i == guess:
                    guess_list[cnt] = guess
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
print('Congratulations you guest the word')
