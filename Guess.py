stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = list(input("Введите слово: ").lower())
live = 6
let = []
end_of_game = False
    # print(f'Pssst, the solution is {chosen_word}.')   #Testing code

for letter in chosen_word:
    let += '_'
print(let)

while end_of_game == False:
    guess = input("Guess a letter: ").lower()


    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == guess:
            let[i] = letter

    if guess not in chosen_word:
        live -= 1
        if live == 0:
            end_of_game = True
            print("\n Game over")
        print(stages[live])

    if '_' not in let:     # проверяет условие отсутствия "_"
        end_of_game = True
        print("\n Угадал!")
    print(let)


