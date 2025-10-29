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


#Erstelle eine Liste aus Worten in der Form ['informatik', 'hardware', 'switch'] usw.
#Da diese Eingabe als Liste sehr muehsam ist, kannst du auch einen String eingeben un diesen splitten. "wort wort".split()
wort = [
    "informatik", "hardware", "software", "netzwerk", "switch", "router", "server", "client",
    "datenbank", "algorithmus", "python", "java", "csharp", "javascript", "html", "css", "php",
    "linux", "windows", "macos", "kernel", "firewall", "cloud", "backup", "security", "encryption",
    "decryption", "api", "json", "xml", "tcp", "udp", "ip", "ethernet", "wifi", "bluetooth",
    "sensor", "actuator", "robotik", "ai", "machinelearning", "deeplearning", "neuralnet", "dataset",
    "bigdata", "virtualisierung", "container", "docker", "kubernetes", "git", "github", "gitlab",
    "bitbucket", "branch", "commit", "merge", "pullrequest", "issue", "bug", "patch", "release",
    "update", "upgrade", "compiler", "interpreter", "syntax", "variable", "funktion", "klasse",
    "objekt", "array", "liste", "dictionary", "tuple", "stack", "queue", "hashmap", "pointer",
    "thread", "prozess", "parallel", "asynchron", "synchron", "event", "signal", "slot", "framework",
    "library", "modul", "package", "script", "pipeline", "devops", "testing", "debugging", "profiling"
]


#Waehle ein zufaelliges Wort aus der Liste wordList und gib dieses mit return zurück
def getRandomWord(wordList):
    zufall = random.choices (wort)
    wort = zufall[0]
    return wort

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()
    

    print('Falsche Buchstaben:', end=' ')
    #Zeige hier alle falschen Buchstaben hintereinander an, welche in missedLetters gespeichert sind.
    #hier kommt dein Code

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): 
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: 
        print(letter, end=' ')
    print()


#Hier soll ein Buchstabe vom Benutzer abgefragt werden. Aber Achtung nur ein Buchstabe.
#Falls es eine Zahl, mehrere Buchstaben oder ein Sonderzeichen oder nichts ist. Wiederhole die Abfrage
def getGuess(alreadyGuessed):
    
    return derBuchstabe

#Willst Du nochmals spielen? Frage den Spieler. Als Rueckgabewert wird True oder False erwartet.
def playAgain():
    JaNein = input('Moechtest du nochmals spielen? (True or False)')
    Yes = JaNein.upper()
    if Yes == 'TRUE':
        return
    else:
        finish
   

#Hier beginnt das Programm
#Gib einen schoenen Titel aus, damit der Benutzer weiss, worum es geht

for i in range(1,200):
    print(i)
print('H A N G M A N')
#hier kommt dein Code


missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
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
            print('Du hast alle Versuche verbraucht\nNach ' + str(len(missedLetters)) + ' falschen Versuchen und ' + str(len(correctLetters)) + ' korrekten Versuchen, wäre das Wort "' + secretWord + '" gewesen')
            gameIsDone = True

    if gameIsDone:
        #Falls der Spieler nochmals spielen will, muessen alle Variablen (missedLetters, correctLetters) wieder geleert werden und gameIsDone auf False gesetz werden
        #Auch sollte ein neues Wort in secretWord ueber die Methode getRandomWord(words) gewaehlt werden
        if playAgain():
            #hier kommt dein Code
        else:
            break
