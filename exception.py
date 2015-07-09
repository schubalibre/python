dividiere = lambda x, y : x / y
tests = ((666.0, 3), (69, 3), (42, "0"))
try:
    try:
        for a, b in tests:
            try:
                print (a, b)
                print dividiere(a, b)
            finally:
                print("Division ausgefuehrt")
    except:
        print("Allg. Fehler")
        raise ZeroDivisionError
except ZeroDivisionError:
    print("Nicht durch Null teilen...")
finally:
        print("Aufraeumen.")
print("Ende.")
print("\n")

dividiere = lambda x, y : x / y
tests = ((42, 2), (42.0, 2.0), (42, "Zero"))

try:
    for a, b in tests:
        try:
            print(a, b)
            print dividiere(a, b)
        finally:
            print("Division ausgefuehrt")
except ZeroDivisionError:
    print("Nicht durch Null teilen...")
except:
    print("Allg. Fehler")
print("Bye.")
print("\n")

def dividiere(x,y):return(x/y)
tests = ((23, 69), (42, 0), ("Spam", "Eggs"))

try:
    for a, b in tests:
        print(a, b),
        try:
            print dividiere(a, b)
        finally:
            print("Versuche zu dividieren.")
except ZeroDivisionError:
    print("Aber ich mag nicht durch Null teilen!")
print("\n Bye.")
print("\n")

def devivdiere(x,y) : return (x/y)
tests= ((42,2),(3,0),(4,5))
try:
	for a,b in tests:
		print("Division"),
		print(a,b),
		print("mit Resultat"),
		print dividiere(a,b)
except ZeroDivisionError:
	print ("Aunahme: bitte nicht durch 0 teilen")
else: print("Alles unter Kontrolle")
print ("bye")
print("\n")
