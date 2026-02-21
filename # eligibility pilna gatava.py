# eligibility.py

try:
    vecums = int(input("Ievadi vecumu: "))
    
    if vecums < 0:
        print("Vecums nevar būt negatīvs!")
        exit()

except ValueError:
    print("Lūdzu ievadi skaitli!")
    exit()


aplieciba = input("Vai ir autovadītāja apliecība? (j/n): ").lower()
ir_aplieciba = aplieciba == "j"

students = input("Vai ir students? (j/n): ").lower()
ir_students = students == "j"

veterans = input("Vai ir veterāns? (j/n): ").lower()
ir_veterans = veterans == "j"


var_balsot = vecums >= 18
var_iret_auto = vecums >= 21 and ir_aplieciba
senioru_atlaide = vecums >= 65 or ir_veterans
studentu_atlaide = 16 <= vecums <= 26 and ir_students


if var_iret_auto:
    auto_teksts = "Jā ✓"
else:
    if not ir_aplieciba:
        auto_teksts = "Nē ✗ (nav apliecības)"
    elif vecums < 21:
        auto_teksts = "Nē ✗ (par jaunu)"
    else:
        auto_teksts = "Nē ✗"


print("\n---")
print(f"Balsošana:        {'Jā ✓' if var_balsot else 'Nē ✗'}")
print(f"Auto īre:         {auto_teksts}")
print(f"Senioru atlaide:  {'Jā ✓' if senioru_atlaide else 'Nē ✗'}")
print(f"Studentu atlaide: {'Jā ✓' if studentu_atlaide else 'Nē ✗'}")
