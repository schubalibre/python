import os
import pickle
from pprint import pprint

wordfiles = {} #leerer Ordner

for root, dirs, files in os.walk('.'):
    for filename in files:
        if filename.endswith(".txt"):
            path = os.path.join(root, filename)  #Verzeichnispfad und Dateinamen zusammensetzen
            with open(path) as file:
                words = file.read().split() #alle Worte in Liste
            
            for word in words:
                if not word in wordfiles:
                    wordfiles[word] = []  #nicht existierende worte neu anlegen
               	wordfiles[word].append(filename) #Verzeichnispfad hinzufuegen
pprint(wordfiles)  
pickle.dump( wordfiles, open( "save.p", "wb" ) )
