import random

HANGMAN_PICS = [
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]

WORDS = [
    "apfel", "banane", "birne", "brot", "butter", "käse", "milch", "wasser", "kaffee", "tee",
    "haus", "tür", "fenster", "stuhl", "tisch", "bett", "lampe", "uhr", "sofa", "bild",
    "auto", "bus", "zug", "fahrrad", "straße", "brücke", "ampel", "bahn", "flugzeug", "schiff",
    "hund", "katze", "maus", "vogel", "pferd", "fisch", "hase", "ente", "kuh", "schaf",
    "schule", "lehrer", "schüler", "buch", "heft", "stift", "tafel", "test", "klasse", "pause",
    "garten", "baum", "blume", "gras", "erde", "stein", "wasserfall", "berg", "see", "fluss",
    "sommer", "winter", "herbst", "frühling", "regen", "sonne", "wolke", "schnee", "wind", "sturm",
    "freund", "familie", "mutter", "vater", "bruder", "schwester", "oma", "opa", "kind", "baby",
    "arzt", "polizei", "feuerwehr", "bäcker", "fahrer", "koch", "maler", "gärtner", "mechaniker",
    "computer", "handy", "tablet", "internet", "spiel", "musik", "film", "bildschirm", "taste", "programm",
]


def get_random_word():
    return random.choice(WORDS)


def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print("Falsche Buchstaben:", " ".join(missed_letters))
    print(" ".join(letter if letter in correct_letters else "_" for letter in secret_word))
    print()


def get_guess(already_guessed):
    while True:
        guess = input("Rate einen Buchstaben: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Bitte gib genau einen Buchstaben ein.")
        elif guess in already_guessed:
            print("Diesen Buchstaben hast du bereits geraten. Versuch es nochmal.")
        else:
            return guess


def play_again():
    return input("Moechtest du nochmals spielen? (ja/nein): ").lower().startswith("j")


def main():
    print("H A N G M A N")
    print("=============\n")

    while True:
        missed_letters = []
        correct_letters = []
        secret_word = get_random_word()

        while True:
            display_board(missed_letters, correct_letters, secret_word)
            guess = get_guess(missed_letters + correct_letters)

            if guess in secret_word:
                correct_letters.append(guess)
                if all(letter in correct_letters for letter in secret_word):
                    display_board(missed_letters, correct_letters, secret_word)
                    print(f'Gewonnen! Das gesuchte Wort war "{secret_word}".')
                    break
            else:
                missed_letters.append(guess)
                if len(missed_letters) == len(HANGMAN_PICS) - 1:
                    display_board(missed_letters, correct_letters, secret_word)
                    print(f'Du hast alle Versuche verbraucht. Das Wort war "{secret_word}".')
                    break

        if not play_again():
            break


if __name__ == "__main__":
    main()
