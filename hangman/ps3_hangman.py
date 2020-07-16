
import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    for i in secretWord:
        if i in lettersGuessed:
            continue
        else:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    count = 0
    guessedWord = ''
    for i in secretWord:
        if i in lettersGuessed:
            count += 1
            guessedWord += i
        else:
            guessedWord += '_ '
    return guessedWord


def getAvailableLetters(lettersGuessed):
    import string
    result = ''
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            result += letter
    return result


def hangman(secretWord):
    lettersGuessed = []
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is' , len(secretWord) , 'letters long.'
    print '-------------'
    total_guesses = 8
    while total_guesses > 0:
        print 'You have' , total_guesses , 'guesses left.'
        print 'Available Letters:' , getAvailableLetters(lettersGuessed)
        Guess= raw_input('Please guess a letter: ')
        Guess_letter = Guess.lower()
        if Guess_letter in secretWord and Guess_letter not in lettersGuessed:
            lettersGuessed += Guess_letter
            print 'Good guess:' , getGuessedWord(secretWord, lettersGuessed)
            print '-------------'
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print 'Congratulations, you won!'
                break
        elif Guess_letter in secretWord and Guess_letter in lettersGuessed:
            lettersGuessed += Guess_letter
            print 'Oops! You\'ve already guessed that letter:' , getGuessedWord(secretWord, lettersGuessed)
            print '-------------'
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print 'Congratulations, you won!'
                break
        elif Guess_letter not in secretWord and Guess_letter not in lettersGuessed:
            lettersGuessed += Guess_letter
            print 'Oops! That letter is not in my word:' , getGuessedWord(secretWord, lettersGuessed)
            print '-------------'
            total_guesses -= 1
            if isWordGuessed(secretWord, lettersGuessed) == False and total_guesses == 0:
                print 'Sorry, you ran out o guesses. The word was else.'
        elif Guess_letter not in secretWord and Guess_letter in lettersGuessed:
            lettersGuessed += Guess_letter
            print 'Oops! You\'ve already guessed that letter:' , getGuessedWord(secretWord, lettersGuessed)
            print '-------------'
            if isWordGuessed(secretWord, lettersGuessed) == False and total_guesses == 0:
                print 'Sorry, you ran out of guesses. The word was else.'