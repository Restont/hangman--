import random

language = input("Choose a language/выбери язык (ru, en/рус, англ)").lower().strip()

if language in ["en", "англ", "engl", "eng", "анг"]:
    
    # words

    words = ["cat", "house", "forest", "ball", "cheese", "moon", "river", "winter", "bear"]
    word = random.choice(words)
    guessed = []
    
    # lives
    
    lives = int(input("How many lives do you want? (min. 3, max. 10.)"))
    if lives < 3:
        lives = 3
    elif lives > 10:
        lives = 10
    
    # your words
    
    while True:
        adword = input("If you want, you can add your own words, if you don`t want, print «no»").lower().strip()
        if adword == "no":
            print("Ok, so we start!")
            print()
            break
        elif adword in words:
            print("Already have it!")
        else:
            words.append(adword)
            print("Added, you can add more!")
            
    # rules

    print("Game «Hangman»!")
    print(f"{len(word)}-letter word. lives: {lives}")
    print()
    
    print("Rules:")
    print("- Guess the word letter by letter")
    print("- If the letter is in the word, it opens")
    print("- If not, you lose a life")
    print("- Only one letter per turn")
    print("- Only letters, no numbers or symbols")
    print("- Win by opening all letters")
    print("- Lose when lives run out")
    print("- You can take a hint in exchange for your life")
    print()
    
    # game

    while lives > 0:
        for letter in word:
            if letter in guessed:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print()
    
        guess = input("guess a letter: ").lower().strip()
        
    # letter test
        
        if len(guess) > 1:
            print("Only one letter!")
            continue
        if not guess.isalpha():
            print("Only letters!")
            continue
        
    # game
    
        if guess in word:
            guessed.append(guess)
            print("There is!")
            
        elif guess in ["hint", "help"]:
            lives -= 1
            for letter in word:
                if letter not in guessed:
                    guessed.append(letter)
                    print(f"Hint: {letter}")
                    break
            continue
        
        else:
            lives -= 1
            print(f"No! Remain lives: {lives}")
        
        win = True
        for letter in word:
            if letter not in guessed:
                win = False
                
        # end
                
        if win:
            print(f"You won! Word was: {word}")
            break

    if lives == 0:
        print(f"You lost! Word was: {word}")
 
    # слова

elif language in ["ru", "рус", "ру", "русский", "rus", "russian"]:
    words = ["планета", "монитор", "лес", "игрок", "сыр", "луна", "речка", "зима", "медведь"]
    word = random.choice(words)
    guessed = []
    
    # жизни
    
    lives = int(input("Сколько жизней хочешь? (мин. 3, макс. 10.)"))
    if lives < 3:
        lives = 3
    elif lives > 10:
        lives = 10
        
    # твои личные слова
    
    while True:
        adword = input("Если хочешь, можешь добавить свои слова. Если не хочешь, напиши «нет»").lower().strip()
        if adword == "нет":
            print("Хорошо, тогда начинаем!")
            print()
            break
        elif adword in words:
            print("Уже есть!")
        else:
            words.append(adword)
            print("Добавлено, можешь добавить еще!")
            
    # правила
    
    print("Правила:")
    print("- Угадывай слово по буквам")
    print("- Если буква есть в слове, она открывается")
    print("- Если нет, теряешь жизнь")
    print("- Только одна буква за ход")
    print("- Только буквы, без цифр и знаков")
    print("- Победа — открыть все буквы")
    print("- Поражение — кончились жизни")
    print("- Ты можешь взять подсказку, взамен на жизнь")
    print()
    
    # игра

    print("Игра «Виселица»!")
    print(f"Слово из {len(word)} букв. Жизней: {lives}")
    print()

    while lives > 0:
        for letter in word:
            if letter in guessed:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print()
    
        guess = input("угадай букву: ").lower().strip()
        
    # проверка на буквы
        
        if len(guess) > 1:
            print("Только одна буква!")
            continue
        if not guess.isalpha():
            print("Только буквы!")
            continue
        
    # игра
        
        if guess in ["подсказка", "подсказку", "помощь"]:
            lives -= 1
            for letter in word:
                if letter not in guessed:
                    guessed.append(letter)
                    print(f"Подсказка: {letter}")
                    break
            continue
    
        if guess in word:
            guessed.append(guess)
            print("Есть!")
        else:
            lives -= 1
            print(f"Нет! Осталось жизней: {lives}")
        
        win = True
        for letter in word:
            if letter not in guessed:
                win = False
                
        # конец        
        
        if win:
            print(f"Ты выиграл! Слово было: {word}")
            break

    if lives == 0:
        print(f"Ты проиграл! Слово было: {word}")
else:
    print("Unknown language/неизвестный язык")
    exit()