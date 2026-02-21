import sys

# ===== ARGUMENTA PĀRBAUDE =====

if len(sys.argv) < 2:
    print("Lietošana: python fizzbuzz.py N")
    exit()

try:
    N = int(sys.argv[1])
except ValueError:
    print("Kļūda — N jābūt skaitlim!")
    exit()

if N < 1:
    print("N jābūt >= 1")
    exit()

# ===== BONUS PARAMETRI =====

rules = [
    (3, "Fizz"),
    (5, "Buzz"),
    (7, "Jazz")   # bonus
]

# ===== GALVENAIS CIKLS =====

for i in range(1, N + 1):

    output = ""

    for divisor, word in rules:
        if i % divisor == 0:
            output += word

    if output == "":
        print(i, end=", ")
    else:
        print(output, end=", ")