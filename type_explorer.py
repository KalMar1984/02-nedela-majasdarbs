python pamata datu tipi ir:
    string (str) - teksta dati, piemēram, "Hello, World!" vinmēr tiek iekļauti pēdiņās
    integer (int) - veseli skaitļi, piemēram, 42 saskaitīšanai, atņemšanai, reizināšanai un dalīšanai
    float (float) - decimāldaļas skaitļi, piemēram, 3.14 mērījumiem un precīzām aprēķināšanām komatu vietā izmanto punktu
    boolean (bool) - loģiskās vērtības, True vai False raksta ar lielo burtu T un F, un tās tiek izmantotas nosacījumu pārbaudei un loģiskajām operācijām
    NoneType (NoneType) - īpašs tips, kas apzīmē "nekas" vai "nav vērtības", piemēram, None

type - iebūvēta python funkcija, parāda kāda datu tipa objekts ir dotā vērtība vai mainīgais
x=5
print(type(x))  # This will output <class 'int'>, indicating that x is an integer
class - Python ir objektorientēta valoda, un katram datu tipam ir sava klase. Piemēram, int tips pieder klasei int, un str tips pieder klasei str. Mēs varam izmantot funkciju type(), lai noskaidrotu, kurai klasei pieder konkrēts objekts.

Piemērs
# virkņu savienošana - Python neveic automātisku tipu konvertēšanu, tāpēc, ja mēģināsim savienot virkni ar skaitli, tas radīs kļūdu. Mēs varam izmantot funkciju int() vai float(), lai konvertētu virkni uz skaitli, ja tas ir iespējams.
print("5" + "3")  # Tiek apvienotas virknes un izvadīts"53"
# print("5"+3)    # TypeError kļūda, jo virkni un vesalu skaitli nevar apvienot
print (int("5") + 3)  # virkne "5" konvertē par veselu skaitli un saskaita ar 3 rezultātā iegūst 8

studijas
print("17"+"28" + "35")  # Tiek apvienotas virknes un izvadīts "172835" Svarīgi saprast, nenotiek matemātiskā saskaitīšana, bet gan virkņu savienošana
print(int("17") + int("28") + int("35"))  # Tiek konvertētas virknes uz veseliem skaitļiem un izvadīts 80
print(type("17"+"28" + "35"))  # Tiek parādīts, ka rezultāts ir string (str) tips
print(type(int("17") + int("28") + int("35")))  # Tiek parādīts, ka rezultāts ir integer (int) tips

piemērs
# Robežgadījumi - Python ir dažādi datu tipi, un katram no tiem ir savas īpašības un ierobežojumi. Piemēram, int tips var saturēt ļoti lielus skaitļus, bet float tips var saturēt tikai noteiktu precizitāti. Ja mēs mēģinām izmantot skaitli, kas pārsniedz int tipa robežas, tas var radīt kļūdu.
robežgadījumi ir ievades dati, kas atrodas tieši pie datu tipa robežas vai ārpus tās, un tie var izraisīt neparedzētas kļūdas vai uzvedību. Piemēram, int tips Pythonā var saturēt skaitļus līdz 2^63-1 (9223372036854775807) un līdz -2^63 (-9223372036854775808). Ja mēģinām izmantot skaitli, kas pārsniedz šīs robežas, tas var radīt OverflowError kļūdu.
# print(int("abc"))  # kļūda, jo "abc" nav skaitlis un to nevar konvertēt uz int. jāveic datu konertēšana uz string, lai izvairītos no kļūdas
print(float("3.14"))        # Tiek konvertēta virkne "3.14" uz float un izvadīts 3.14

studijas 
explicid conversion - Python neveic automātisku tipu konvertēšanu, tāpēc mums ir jāveic eksplicīta konversija, ja vēlamies savienot dažādus datu tipus. Piemēram, ja vēlamies savienot virkni ar skaitli, mums ir jākonvertē skaitlis uz virkni vai virkne uz skaitli, atkarībā no tā, kādu rezultātu mēs vēlamies sasniegt. Jānorāda kurai klasei pieder objekts, lai izvairītos no kļūdām un panāktu pareizu rezultātu.   
# print(str("abc"))  # tiek konvertēta virkne "abc" uz string, kas ir derīgs datu tips, un izvadīts "abc"
print(float("3,14")) # kļūda, jo "3,14" nav derīgs float formāts, komats nav atļauts decimāldaļas skaitļos
a = input(5)
b = input(3)
print(a + b)  # Ja ievadām 5 un 3, rezultāts būs "53", jo abi ievadi tiek uzskatīti par virkni (string) un tiek savienoti, nevis saskaitīti. Lai iegūtu matemātisku summu, mums jākonvertē ievadi uz skaitļiem, piemēram, int(a) + int(b).
print(int(a) + int(b))  # Tiek konvertēti ievadi uz skaitļiem un izvadīts 8

Piemērs
# Truthy / falsy - Pythonā ir jēdziens "truthy" un "falsy" vērtības, kas nosaka, kā dažādi datu tipi tiek interpretēti kā patiesi (True) vai nepatiesi (False) nosacījumos. Piemēram, tukša virkne "" tiek uzskatīta par falsy, bet ne tukša virkne "Hello" tiek uzskatīta par truthy. Līdzīgi, skaitlis 0 tiek uzskatīts par falsy, bet jebkurš cits skaitlis tiek uzskatīts par truthy. Šis jēdziens ir svarīgs, lai saprastu, kā Python apstrādā nosacījumus un loģiskās operācijas.
print(bool(""))  # Tiek konvertēta tukša virkne uz boolean, rezultāts būs False, jo tukša virkne tiek uzskatīta par falsy
print(bool(" "))  # Tiek konvertēta virkne ar vienu atstarpi uz boolean, rezultāts būs True, jo virkne ar saturu (pat ja tas ir tikai atstarpe) tiek uzskatīta par truthy
print(bool("0"))   # Tiek konvertēta virkne "0" uz boolean, rezultāts būs True, jo virkne ar saturu (pat ja tas ir "0") tiek uzskatīta par truthy
print(bool(0))    # Tiek konvertēts skaitlis 0 uz boolean, rezultāts būs False, jo 0 tiek uzskatīts par falsy
print(bool([]))    # Tiek konvertēta tukša saraksta (list) uz boolean, rezultāts būs False, jo tukšs saraksts tiek uzskatīts par falsy 
print(bool(None))  # Tiek konvertēts None uz boolean, rezultāts būs False, jo None tiek uzskatīts par falsy
print(True + True)   # Tiek saskaitītas divas True vērtības, rezultāts būs 2, jo True tiek interpretēts kā 1

Studijas
print(True + False)  # Tiek saskaitīta True un False vērtība, rezultāts būs 1, jo True tiek interpretēts kā 1 un False kā 0
print(False + False) # Tiek saskaitītas divas False vērtības, rezultāts būs 0, jo False tiek interpretēts kā 0 

# Jauktā aritmētika - Pythonā, ja mēs veicam aritmētiskas operācijas ar dažādiem datu tipiem, Python mēģinās konvertēt vienu no tiem uz otru, lai veiktu operāciju. Piemēram, ja mēs saskaitām int un float, int tiks konvertēts uz float, un rezultāts būs float. Ja mēs saskaitām int un str, tas radīs kļūdu, jo Python nevar automātiski konvertēt str uz int vai otrādi.
Piemērs
print(True * 10)     # Tiek reizināta True vērtība ar 10, rezultāts būs 10, jo True tiek interpretēts kā 1, un 1 * 10 = 10
print(False + 5)    # Tiek saskaitīta False vērtība ar 5, rezultāts būs 5, jo False tiek interpretēts kā 0, un 0 + 5 = 5
print(10 / True)    # Tiek dalīts 10 ar True, rezultāts būs 10.0, jo True tiek interpretēts kā 1, un 10 / 1 = 10.0 (rezultāts ir float, jo dalīšana vienmēr atgriež float)

studijas
print(5 + 3.0)  # Tiek saskaitīts int un float, rezultāts būs 8.0, jo int 5 tiek konvertēts uz float 5.0
# print(5 + "3")  # Tiks radīta TypeError, jo Python nevar automātiski konvertēt str "3" uz int 3 vai int 5 uz str "5" un veikt saskaitīšanu. Lai izvairītos no kļūdas, mums jāveic eksplicīta konversija, piemēram, int("3") + 5 vai str(5) + "3". 
print(int("3") + 5)  # Tiek konvertēta virkne "3" uz int 3 un saskaita ar 5, rezultāts būs 8
print(str(5) + "3")  # Tiek konvertēts int 5 uz str "5" un savieno ar "3", rezultāts būs "53"

#Skaitļu pārveidošana - Pythonā ir vairākas funkcijas, kas ļauj konvertēt datus uz skaitļiem. Piemēram, int() funkcija konvertē datus uz veselu skaitli, float() funkcija konvertē datus uz decimāldaļas skaitli, un bool() funkcija konvertē datus uz boolean vērtību. Šīs funkcijas ir noderīgas, lai veiktu matemātiskas operācijas vai loģiskās pārbaudes ar datiem, kas sākotnēji var būt citā formātā, piemēram, virknēs.
Piemēri
print(int(3.86))   # Tiek konvertēts float 3.86 uz int, rezultāts būs 3, jo int funkcija noņem decimāldaļu un atstāj tikai veselo daļu
print(int("3.14"))   # Tiek mēģināta konvertēšana virkne "3.14" uz int, kas radīs ValueError kļūdu, jo "3.14" nav derīgs int formāts. Lai izvairītos no kļūdas, vispirms jākonvertē uz float un pēc tam uz int, piemēram, int(float("3.14")), kas rezultēsies ar 3.
print(int(float("3.14")))   # Tiek konvertēta virkne "3.14" uz float, rezultāts būs 3.14, un pēc tam tas tiek konvertēts uz int, rezultāts būs 3, jo int funkcija noņem decimāldaļu un atstāj tikai veselo daļu
print(float("1e3"))     # Tiek konvertēta virkne "1e3" uz float, rezultāts būs 1000.0, jo "1e3" ir zinātniskā notaācija, kas apzīmē 1 reizinātu ar 10 pakāpē 3 (1 * 10^3 = 1000)

Studijas
print(int("123"))  # Tiek konvertēta virkne "123" uz veselu skaitli 123
print(float("45.67"))  # Tiek konvertēta virkne "45.67" uz decimāldaļas skaitli 45.67
print(bool("True"))  # Tiek konvertēta virkne "True" uz boolean vērtību True
print(bool("False"))  # Tiek konvertēta virkne "False" uz boolean vērtību False, jo "False" ir ne tukša virkne, un visas ne tukšas virknes tiek uzskatītas par truthy

#Citi interesanti gadījumi, izskaidrot kāpēc tā notiek.
print(0.1 + 0.2 == 0.3)     # Tiek veikta aritmētiska operācija ar float skaitļiem, un rezultāts būs False, jo 0.1 un 0.2 nevar precīzi attēlot binārajā formātā, kas var radīt nelielas noapaļošanas kļūdas, un tāpēc 0.1 + 0.2 var būt nedaudz lielāks vai mazāks par 0.3, kas izraisa salīdzinājuma rezultātu False
print(0.1 + 0.2)  # Tiek veikta aritmētiska operācija ar float skaitļiem, un rezultāts būs 0.30000000000000004, kas ilustrē, kā binārā reprezentācija var radīt nelielas noapaļošanas kļūdas ar decimāldaļas skaitļiem, un tas ir iemesls, kāpēc 0.1 + 0.2 == 0.3 ir False  
    
    round - Python funkcija, kas noapaļo skaitli līdz norādītajam decimāldaļu skaitam. Ja decimāldaļu skaits nav norādīts, tas noapaļo līdz tuvākajam veselajam skaitlim. Python izmanto "banker's rounding" (noapaļošana uz tuvāko pāra skaitli), kas nozīmē, ka ja skaitlis ir tieši starp diviem veseliem skaitļiem, tas tiks noapaļots uz tuvāko pāra skaitli. Piemēram, 2.5 tiks noapaļots uz 2, jo 2 ir tuvākais pāra skaitlis, savukārt 3.5 tiks noapaļots uz 4, jo 4 ir tuvākais pāra skaitlis.
    

print(round(2.5))   # Tiek noapaļots skaitlis 2.5, un rezultāts būs 2, jo Python izmanto "banker's rounding" (noapaļošana uz tuvāko pāra skaitli), un 2 ir tuvākais pāra skaitlis 2.5, savukārt 3 ir nepāra skaitlis
print(round(3.5))    # Tiek noapaļots skaitlis 3.5, un rezultāts būs 4, jo Python izmanto "banker's rounding" (noapaļošana uz tuvāko pāra skaitli), un 4 ir tuvākais pāra skaitlis 3.5, savukārt 3 ir nepāra skaitlis
bankers_rounding = [round(x) for x in [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]]  # Tiek izveidots saraksts ar noapaļotiem skaitļiem, un rezultāts būs [0, 2, 2, 4, 4, 6], jo Python izmanto "banker's rounding" (noapaļošana uz tuvāko pāra skaitli), un katrs skaitlis tiek noapaļots uz tuvāko pāra skaitli
print(bankers_rounding)  # Tiek izvadīts saraksts ar noapaļotiem skaitļiem, rezultāts būs [0, 2, 2, 4, 4, 6], jo Python izmanto "banker's rounding" (noapaļošana uz tuvāko pāra skaitli), un katrs skaitlis tiek noapaļots uz tuvāko pāra skaitli 

