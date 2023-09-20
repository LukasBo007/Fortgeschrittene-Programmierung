#Aufgabe 1: Decorator Timer
#Erstellen Sie einen Decorator timer, der die verbrauchte Zeit einer Funktion messen kann.
#Hilfreich kann Ihnen folgender Code sein:
import time
before = time.time()
# Something happens here
sekunden = time.time() - before
#Wenden Sie Ihren Decorator auf folgenden Code an:
def f(a, b=42):
 time.sleep(2) # Warte 2 Sekunden
 print(a, b)
