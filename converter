# ===== KONSTANTES =====
KM_TO_MI = 0.621371
KG_TO_LB = 2.20462
L_TO_GAL = 0.264172
USD_TO_EUR = 0.84235020

# ===== IZVĒLNE =====
print("=== Vienību konvertors ===")
print("1 - km → jūdzes")
print("2 - jūdzes → km")
print("3 - kg → mārciņas")
print("4 - mārciņas → kg")
print("5 - litri → galoni")
print("6 - galoni → litri")
print("7 - USD → EUR")
print("8 - EUR → USD")

choice = input("Izvēlies numuru: ")

# ===== SKAITĻA IEVade =====
try:
    value = float(input("Ievadi vērtību: "))
except ValueError:
    print("Kļūda — jāievada skaitlis!")
    exit()

# ===== APRĒĶINI =====
if choice == "1":
    result = value * KM_TO_MI
    print(f"{value:.2f} km = {result:.2f} mi")

elif choice == "2":
    result = value / KM_TO_MI
    print(f"{value:.2f} mi = {result:.2f} km")

elif choice == "3":
    result = value * KG_TO_LB
    print(f"{value:.2f} kg = {result:.2f} lb")

elif choice == "4":
    result = value / KG_TO_LB
    print(f"{value:.2f} lb = {result:.2f} kg")

elif choice == "5":
    result = value * L_TO_GAL
    print(f"{value:.2f} L = {result:.2f} gal")

elif choice == "6":
    result = value / L_TO_GAL
    print(f"{value:.2f} gal = {result:.2f} L")

elif choice == "7":
    result = value * USD_TO_EUR
    print(f"{value:.2f} USD = {result:.2f} EUR")

elif choice == "8":
    result = value / USD_TO_EUR
    print(f"{value:.2f} EUR = {result:.2f} USD")

else:
    print("Nepareiza izvēle!")
