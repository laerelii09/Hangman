import random
import secrets

HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

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
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']



wordList = [
    "apfel", "banane", "birne", "brot", "butter", "käse", "milch", "wasser", "kaffee", "tee",
    "haus", "tür", "fenster", "stuhl", "tisch", "bett", "lampe", "uhr", "sofa", "bild",
    "auto", "bus", "zug", "fahrrad", "straße", "brücke", "ampel", "bahn", "flugzeug", "schiff",
    "hund", "katze", "maus", "vogel", "pferd", "fisch", "hase", "ente", "kuh", "schaf",
    "schule", "lehrer", "schüler", "buch", "heft", "stift", "tafel", "test", "klasse", "pause",
    "garten", "baum", "blume", "gras", "erde", "stein", "wasserfall", "berg", "see", "fluss",
    "sommer", "winter", "herbst", "frühling", "regen", "sonne", "wolke", "schnee", "wind", "sturm",
    "freund", "familie", "mutter", "vater", "bruder", "schwester", "oma", "opa", "kind", "baby",
    "arzt", "polizei", "feuerwehr", "bäcker", "fahrer", "koch", "maler", "gärtner", "mechaniker", "lehrer",
    "computer", "handy", "tablet", "internet", "spiel", "musik", "film", "bildschirm", "taste", "programm"
]



#Wähe ein zufälliges wort aus der Liste wordlist und gibt es mit return zurück.
def getRandomWord(wordList):
    wort = random.choice(wordList)
    return wort

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()
    
    print('Falsche Buchstaben:', end=' ')

    #Zeige hier alle falschen Buchstaben hintereinander an, welche in missedLetters gespeichert sind.
    for letter in missedLetters:
        print(letter, end=' ')
    print('\n')

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): 
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: 
        print(letter, end=' ')
    print('\n')


#Hier soll ein Buchstabe vom Benutzer abgefragt werden. Aber Achtung nur ein Buchstabe.
#Falls es eine Zahl, mehrere Buchstaben oder ein Sonderzeichen oder nichts ist. Wiederhole die Abfrage
def getGuess(alreadyGuessed):
    while True:
        guess = input('Rate einen Buchstaben: ').lower()
        if len(guess) != 1:
            print('Bitte gib nur EINEN Buchstaben ein.')
        elif not guess.isalpha():
            print('Bitte gib nur Buchstaben ein (keine Zahlen oder Sonderzeichen).')
        elif guess in alreadyGuessed:
            print('Diesen Buchstaben hast du bereits geraten. Versuch es nochmal.')
        else:
            return guess


#Willst Du nochmals spielen? Frage den Spieler. Als Rueckgabewert wird True oder False erwartet.
def playAgain():
    JaNein = input('Moechtest du nochmals spielen? (ja/nein): ')
    if JaNein.lower().startswith('j'):
        return True
    else:
        return False
   

#Hier beginnt das Programm
#Gib einen schoenen Titel aus, damit der Benutzer weiss, worum es geht

for i in range(1,200):
    print()
print('H A N G M A N')
print('=============\n')

missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(wordList)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yep! Das gesuchte Wort ist "' + secretWord + '"! Du hast gewonnen!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('Du hast alle Versuche verbraucht\nNach ' + str(len(missedLetters)) +
                  ' falschen Versuchen und ' + str(len(correctLetters)) +
                  ' korrekten Versuchen, wäre das Wort "' + secretWord + '" gewesen')
            gameIsDone = True

    if gameIsDone:
        #Falls der Spieler nochmals spielen will, muessen alle Variablen (missedLetters, correctLetters) wieder geleert werden und gameIsDone auf False gesetz werden
        #Auch sollte ein neues Wort in secretWord ueber die Methode getRandomWord(words) gewaehlt werden
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(wordList)
        else:
            break
