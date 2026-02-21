# eligibility.py - pārbauda vai cilvēks ir tiesīgs balsot

#=====ievades dati===== (vecumu ievade ar kļūdu apstrādi)
try: #python mēģina izpildīt šo kodu
vecums = int(input("Ievadi savu vecumu: ")) 

if vecums <0: #ja vecums ir mazāks par 0, tiek izvadīts kļūdas paziņojums
print("Vecums nevar būt negatīvs.")
exit() #aptur programmu, ja ir kļūda

except ValueError: #ja ievade nav skaitlis, tiek izvadīts kļūdas paziņojums
print("Lūdzu, ievadi skaitli.") 

exit() #aptur programmu, ja ir kļūda  

#(pārbauda vai ir autovadītāja apliecība, students vai veterāns) 
aplieciba = input("Vai tev ir autovadītāja apliecība? (j/n): ").lower() == "j" # .lower() pārvērš ievadi mazajiem burtiem, lai atbalstītu gan "j" gan "J"
aplciba == "j" #pārbauda vai ievade ir "j", ja jā, tad aplieciba būs True, pretējā gadījumā False 

students = input("Vai tu esi students? (j/n): ").lower() == "j"
students == "j" #pārbauda vai ievade ir "j", ja jā, tad students būs True, pretējā gadījumā False   

veterans = input("Vai tu esi veterāns? (j/n): ").lower() == "j" 
veterans == "j" #pārbauda vai ievade ir "j", ja jā, tad veterans būs True, pretējā gadījumā False

#=====loģiskie nosacījumi===== (pārbauda vai cilvēks ir tiesīgs balsot, īrēt auto, saņemt senioru atlaidi vai studentu atlaidi)
vecums >= 18 #nosacījums balsot - jābūt vismaz 18 gadiem
var_balsot = vecums >= 18 #pats atgriež True vai False atkarībā no vecuma 

vecums >= 21 and aplieciba #nosacījums auto īrei - jābūt vismaz 21 gadam un jābūt autovadītāja apliecībai
var_iret_auto = vecums >= 21 and aplieciba #pats atgriež True vai False atkarībā no vecuma un apliecības esamības

vecums >= 65 or ir veterans #nosacījums senioru atlaidei - jābūt vismaz 65 gadiem vai jābūt veterānam
var_senioru_atlaide = vecums >= 65 or veterans #pats atgriež True vai False atkarībā no vecuma vai veterāna statusa 

vecums >= 16 and vecums <= 26 and students #nosacījums studentu atlaidei - jābūt vecumā no 16 līdz 26 gadiem un jābūt studentam
var_studentu_atlaide = vecums >= 16 and vecums <= 26 and students #pats atgriež True vai False atkarībā no vecuma un studentu statusa (vecums ir starp 16 un 26 ieskaitot un ir students) 

#izvade ar f-stringiem, ļauj ievietot mainīgs tekstā, lai parādītu rezultātus ar "Jā ✓" vai "Nē ✗" atkarībā no nosacījumu izpildes
print(f"Balsošana: {'Jā ✓' if var_balsot else 'Nē ✗'}")
print(f"Auto īre: {'Jā ✓' if var_iret_auto else 'Nē ✗'}")
print(f"Senioru atlaide: {'Jā ✓' if var_senioru_atlaide else 'Nē ✗'}")
print(f"Studentu atlaide: {'Jā ✓' if var_studentu_atlaide else 'Nē ✗'}")   

#=====paskaidrojums auto īrei===== 
if var_iret_auto:
    auto_teksts = "Jā ✓"
else:
    auto_teksts = "Nē ✗"
    if not aplieciba:
        auto_teksts += " (nav apliecības)"
    elif vecums < 21:
        auto_teksts += " (par jaunu)" 
print(f"Auto īre: {auto_teksts}") #izvada rezultātu ar paskaidrojumu, ja nav tiesību īrēt auto


#=====izvade=====
print("\n---") # Escape sequence \n tiek izmantota, lai izvadītu jaunu rindu, tādējādi atdalot ievades un izvades daļas, padarot rezultātu pārskatāmāku. Izdrukā tukšu rindu un izdrukā ---, lai vizuāli atdalītu ievades un izvades daļas, padarot rezultātu pārskatāmāku.
print(f"Balsošana:         {'Jā ✓' if var_balsot else 'Nē ✗'}") #izvada rezultātu par balsotāju statusu, izmantojot f-string un nosacījuma operatoru, lai parādītu "Jā ✓" vai "Nē ✗" atkarībā no var_balsot vērtības
print(f"Auto īre:          {'Jā ✓' if var_iret_auto else 'Nē ✗'}{auto_teksts[3:]}") #pievieno paskaidrojumu tikai, ja nav tiesību īrēt auto
print(f"Senioru atlaide:   {'Jā ✓' if var_senioru_atlaide else 'Nē ✗'}") #izvada rezultātu par senioru atlaides statusu, izmantojot f-string un nosacījuma operatoru, lai parādītu "Jā ✓" vai "Nē ✗" atkarībā no var_senioru_atlaide vērtības
print(f"Studentu atlaide:  {'Jā ✓' if var_studentu_atlaide else 'Nē ✗'}") #izvada rezultātu par studentu atlaides statusu, izmantojot f-string un nosacījuma operatoru, lai parādītu "Jā ✓" vai "Nē ✗" atkarībā no var_studentu_atlaide vērtības    




#=====paskaidrojumi=====
# .lower() - pārvērš tekstu mazajiem burtiem, lai atbalstītu gan "j" gan "J" ievadi
# == "j" - pārbauda vai ievade ir "j", ja jā, tad mainīgais būs True, pretējā gadījumā False
# and - loģiskais operators, kas atgriež True tikai tad, ja abi nosacījumi ir patiesi
# or - loģiskais operators, kas atgriež True, ja vismaz viens nosacījums ir patiesi
# f-string - formāta string, kas ļauj ievietot mainīgos tekstā, izmantojot {}. Piemēram, f"Vecums: {vecums}" izvadīs "Vecums: " un mainīgā vecums vērtību.      
