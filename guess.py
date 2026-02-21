import random

while True:   # ārējais cikls — spēlēt vēlreiz

    secret = random.randint(1, 100)
    attempts = 0
    MAX_ATTEMPTS = 10

    print("\nEs izdomāju skaitli no 1 līdz 100.")

    while True:   # iekšējais spēles cikls

        guess_input = input("Tavs minējums: ")

        try:
            guess = int(guess_input)
        except ValueError:
            print("Lūdzu ievadi skaitli!")
            continue

        attempts += 1

        if guess < secret:
            print("Par mazu")
        elif guess > secret:
            print("Par lielu")
        else:
            print("Pareizi!")
            break

        if attempts >= MAX_ATTEMPTS:
            print("Beidzās mēģinājumi.")
            break

    print(f"Mēģinājumi: {attempts}")
    print(f"Pareizais skaitlis bija: {secret}")

    again = input("Spēlēt vēlreiz? (j/n): ").lower()
    if again != "j":
        break
