from hangman import Hangman
from guess import Guess
from word import Word

def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())

    hangman = Hangman()
    maxNumOfTries = hangman.getLife()

    while guess.numOfTries < maxNumOfTries:
        display = hangman.get(maxNumOfTries - guess.numOfTries)
        print(display)
        guess.display()

        guessedChar = input('Select a letter: ')
        if len(guessedChar) != 1:
            print('One character at a time!')
            continue

        if guessedChar in guess.guessedChars:
            print('You already guessed \"' + guessedChar + '\"')
            continue

        if guess.guess(guessedChar):
            print('Success')
            return

    print(hangman.get(0))
    print('word [' + guess.word + ']')  # 원래 주어진 코드는 secretWord로 따로 관리하는데 이를 word로 통일
    print('guess [' + guess.currentStatus + ']')
    print('Fail')


if __name__ == '__main__':
    gameMain()
