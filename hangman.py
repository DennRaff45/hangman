import random

# constants
HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

MAX_WRONG = len(HANGMAN) - 1
WORDS = ("БИБЛИОТЕКА", "ВИРУС", "МАГАЗИН", "ЛЕСТНИЦА", "ДЕРЕВО", "ЛЕОПАРД", "КОТ", "КОМПЬЮТЕР", "НЕБО", "РОБОТ", "ЛАМПА", "СТАКАН", "ДВЕРЬ", "КОСМОС", "КЛАВИАТУРА",
"РЫБА", "ПТИЦА", "ОРУЖИЕ", "ЭКРАН", "СЛОВО", "ЧАСЫ", "ТЕЛЕФОН", "ГОРОД", "МАШИНА", "РУЧКА", "КНИГА", "НОЖНИЦЫ", "НОЖ", "ЧЕЛОВЕК", "ЗВЕРЬ", "ЕНОТ", "ДИНОЗАВР", "ЖИЗНЬ")

# initialize variables
word = random.choice(WORDS)   # the word to be guessed
so_far = "-" * len(word)      # one dash for each letter in word to be guessed
wrong = 0                     # number of wrong guesses player has made
used = []                     # letters already guessed


print ("Добро пожаловать в игру висилица! Удачи!")

while (wrong < MAX_WRONG) and (so_far != word):
    print (HANGMAN[wrong])
    print ("\nВы уже предлагали следующие буквы:\n", used)
    print ("\nОтгаданное вами в слове сейчас выглядит так:\n", so_far)

    guess = input("\n\nВведите букву: ")
    guess = guess.upper()
    
    while (guess in used):
        print ("Вы уже предлагали букву:", guess)
        guess = input("Введите букву: ")
        guess = guess.upper()

    used.append(guess)

    if (guess in word):
        print ("\nДа!", guess, "буква есть в слове!")

        # create a new so_far to include guess
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]              
        so_far = new

    else:
        print ("\nК сожалению, буквы", guess, "нет в слове.")
        wrong += 1

if (wrong == MAX_WRONG):
    print (HANGMAN[wrong])
    print ("\nВас повесили")
else:
    print ("\nВы отгадали!")
    
print ("\nБыло загадано слово ", word)

input("\n\nPress the enter key to exit.")