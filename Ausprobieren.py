wörterliste = [
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

import random
secretword = randomwortinListe(wörterliste)

def randomwortinListe(wörterliste):              #Random wort in Liste gepackt und es in buchstaben unterteilt.
  buchstabe = random.choice(wörterliste)            
  return list(buchstabe) 
  

#Zeige hier alle falschen Buchstaben hintereinander an, welche in missedLetters gespeichert sind.
    #hier kommt dein Code

  
def missedLetters():
  secretword = randomwortinListe(wörterliste)
  print(secretword)
  blanks = '_' * len(secretword)
  for i in range(len(secretword)): 
      if secretword[i] in correctLetters:
        blanks = blanks[:i] + secretword[i] + blanks[i+1:]

  for letter in blanks: 
        print(letter, end=' ')
  print()


missedLetters(wörterliste)
def randomwortinListe():                                #Random wort in Liste gepackt und es in buchstaben unterteilt.
  buchstabe = random.choice(wörterliste)            
  buchstabe = list[buchstabe.split()]
  print(buchstabe)
