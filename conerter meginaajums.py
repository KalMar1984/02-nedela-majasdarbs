#===== KONSTANTES =====#
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