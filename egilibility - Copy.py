# ===== IEVADES BLOKS =====

try:
    age = int(input("Ievadi vecumu: "))
except ValueError:
    print("Kļūda — vecumam jābūt skaitlim!")
    exit()

if age < 0:
    print("Kļūda — vecums nevar būt negatīvs!")
    exit()

license_input = input("Vai ir autovadītāja apliecība? (j/n): ").lower()
student_input = input("Vai ir students? (j/n): ").lower()
veteran_input = input("Vai ir veterāns? (j/n): ").lower()

has_license = license_input == "j"
is_student = student_input == "j"
is_veteran = veteran_input == "j"

# ===== LOĢISKIE NOSACĪJUMI =====

can_vote = age >= 18
can_rent = age >= 21 and has_license
senior_discount = age >= 65 or is_veteran
student_discount = 16 <= age <= 26 and is_student

# ===== PAPILDU PASKAIDROJUMS AUTO ĪREI =====

rent_reason = ""
if not has_license:
    rent_reason = " (nav apliecības)"
elif age < 21:
    rent_reason = " (par jaunu)"

# ===== IZVADE =====

print("---")
print(f"Balsošana:         {'Jā ✓' if can_vote else 'Nē ✗'}")
print(f"Auto īre:          {'Jā ✓' if can_rent else 'Nē ✗'}{rent_reason}")
print(f"Senioru atlaide:   {'Jā ✓' if senior_discount else 'Nē ✗'}")
print(f"Studentu atlaide:  {'Jā ✓' if student_discount else 'Nē ✗'}")
