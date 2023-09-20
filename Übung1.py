import time
before = time.time()
# Something happens here
sekunden = time.time() - before
#Wenden Sie Ihren Decorator auf folgenden Code an:
def f(a, b=42):
 time.sleep(2) # Warte 2 Sekunden
 print(a, b)