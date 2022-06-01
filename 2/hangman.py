
# Hangman Game
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings) 
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word :
        if char not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    s = ""
    for char1 in secret_word :
        if char1 in letters_guessed:
            s += char1
        else :
            s += "_ "
    print (s)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    s = list(string.ascii_lowercase)
   # convert (s)
    #total = []
    for i in letters_guessed :
        if i in s :
            s.remove(i)
    #rest = s.remove(total)
    return s   


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    '''
    print ("Welcome to the game Hangman!")
   
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    
    L = []
    for j in range (0, 6) :
        print(secret_word)
   
        print ("You have", 6-j, "guesses left.")
        print("Please guess a letter:")
        letter = input()
        if letter not in L:
            L.append(letter)
        else :
            print ("Enter another letter")
        if letter in secret_word:
            
            print ("Good guess:")
        else :
            print("Oops! That letter is not in my word:")
     
        get_guessed_word(secret_word, L)
        print ("Available letters: ")
        print (''.join(get_available_letters(L)))
        print("------------")



if __name__ == "__main__":
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
