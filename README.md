# Hangman

A small command-line word game, written in Python. Guess the hidden German word
one letter at a time. You get six incorrect guesses.

```text
+---+       H A N G M A N
|   |       Wrong: e, i
O   |
/|\  |       Word:  _ a _ _ e
/ \  |
=========
```

## Run

You need Python 3. On Windows, double-click `hangman.bat`, or run it from this
folder in PowerShell:

```powershell
.\hangman.bat
```

The launcher tries `py -3` first, then falls back to `python`. To start the game
directly, run `python hangman.py`.

## Run from anywhere in Command Prompt

To use `hangman` as a command from any folder, add this project folder to your
user PATH. Open PowerShell in the project folder and run this once:

```powershell
.\setup-cmd-alias.ps1
```

Open a new Command Prompt window and enter `hangman`. The setup changes only your
Windows user PATH; it does not require administrator access.

In PowerShell, the same command also works from any folder after setup. The
optional `setup-alias.ps1` profile helper is not required for CMD.

## Files

- `hangman.py` - game
- `hangman.bat` - Windows launcher
- `setup-cmd-alias.ps1` - adds the project folder to your user PATH
- `setup-alias.ps1` - optional PowerShell profile helper
