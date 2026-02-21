# eligibility.py

# -----------------------------
# Funkcija vecuma ievadei
# -----------------------------
def ievadi_vecumu():
    while True:
        ievade = input("Ievadi vecumu: ")
        
        try:
            vecums = int(ievade)
            
            if vecums < 0:
                print("Vecums nevar būt negatīvs!")
            else:
                return vecums
                
        except ValueError:
            print("Lūdzu ievadi veselu skaitli!")


# -----------------------------
# Funkcija J/N validācijai
# -----------------------------
def jautajums(teksts):
    while True:
        atbilde = input(teksts).strip().lower()
        
        # Atļautās JĀ atbildes
        ja_atbildes = ("j", "ja", "jā")
        
        # Atļautās NĒ atbildes
        ne_atbildes = ("n", "ne", "nē")
        
        if atbilde in ja_atbildes:
            return True
        elif atbilde in ne_atbildes:
            return False
        else:
            print("Lūdzu ievadi tikai 'j' vai 'n' (vai 'ja' / 'ne').")


# -----------------------------
# Programmas sākums
# -----------------------------

vecums = ievadi_vecumu()

ir_aplieciba = jautajums("Vai ir autovadītāja apliecība? (j/n): ")
ir_students = jautajums("Vai ir students? (j/n): ")
ir_veterans = jautajums("Vai ir veterāns? (j/n): ")


# -----------------------------
# Nosacījumi
# -----------------------------

var_balsot = vecums >= 18
var_iret_auto = vecums >= 21 and ir_aplieciba
senioru_atlaide = vecums >= 65 or ir_veterans
studentu_atlaide = 16 <= vecums <= 26 and ir_students


# -----------------------------
# Auto īres paskaidrojums
# -----------------------------

if var_iret_auto:
    auto_teksts = "Jā ✓"
else:
    if not ir_aplieciba:
        auto_teksts = "Nē ✗ (nav apliecības)"
    elif vecums < 21:
        auto_teksts = "Nē ✗ (par jaunu)"
    else:
        auto_teksts = "Nē ✗"


# -----------------------------
# Izvade
# -----------------------------

print("\n---")
print(f"Balsošana:        {'Jā ✓' if var_balsot else 'Nē ✗'}")
print(f"Auto īre:         {auto_teksts}")
print(f"Senioru atlaide:  {'Jā ✓' if senioru_atlaide else 'Nē ✗'}")
print(f"Studentu atlaide: {'Jā ✓' if studentu_atlaide else 'Nē ✗'}")