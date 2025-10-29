import random
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

def randomwortinListe():
  buchstabe = random.choice(wörterliste)
  buchstabe = list[buchstabe.split(" ")]
  print(buchstabe)
randomwortinListe() 

