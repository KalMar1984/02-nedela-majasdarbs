python -pamata datu tipi ir:
    string (str) - teksta dati, piemēram, "Hello, World!" vinmēr tiek iekļauti pēdiņās
    integer (int) - veseli skaitļi, piemēram, 42 saskaitīšanai, atņemšanai, reizināšanai un dalīšanai
    float (float) - decimāldaļas skaitļi, piemēram, 3.14 mērījumiem un precīzām aprēķināšanām komatu vietā izmanto punktu
    boolean (bool) - loģiskās vērtības, True vai False raksta ar lielo burtu T un F, un tās tiek izmantotas nosacījumu pārbaudei un loģiskajām operācijām
    NoneType (NoneType) - īpašs tips, kas apzīmē "nekas" vai "nav vērtības", piemēram, None
    
    
    complex (complex) - kompleksi skaitļi, kas sastāv no reālās un iedomātās daļas, piemēram, 2 + 3j    
    kolekciju tipi - tie ir datu tipi, kas var saturēt vairākas vērtības vienā mainīgajā. Šie tipi ietver:
    list (list) - saraksti, kas var saturēt dažāda veida elementus, piemēram, [1, 2, 3] vai ["apple", "banana", "cherry"]
    tuple (tuple) - tupļi, kas ir līdzīgi sarakstiem, bet ir nemainīgi (immutable), piemēram, (1, 2, 3) vai ("apple", "banana", "cherry")
    set (set) - kopas, kas ir unikālu elementu kolekcijas, piemēram, {1, 2, 3} vai {"apple", "banana", "cherry"}
    dictionary (dict) - vārdnīcas, kas satur atslēgu-vērtību pārus, piemēram, {"name": "Alice", "age": 30, "city": "New York"}

type - iebūvēta python funkcija, parāda kāda datu tipa objekts ir dotā vērtība vai mainīgais
x=5
print(type(x))    # This will output <class 'int'>, indicating that x is an integer
class - Python ir objektorientēta valoda, un katram datu tipam ir sava klase. Piemēram, int tips pieder klasei int, un str tips pieder klasei str. Mēs varam izmantot funkciju type(), lai noskaidrotu, kurai klasei pieder konkrēts objekts.

() - iekavas tiek izmantotas, lai izsauktu funkcijas, piemēram, print() funkcija tiek izsaukta ar iekavām, un tās iekšpusē var ievietot argumentus, piemēram, print("Hello, World!") izvadīs tekstu "Hello, World!" uz ekrāna.

aritmētiskie operatori - tie ir simboli, kas tiek izmantoti, lai veiktu matemātiskas operācijas ar skaitļiem. Šie operatori ietver:
+ - plus zīme tiek izmantota, lai veiktu saskaitīšanu ar skaitļiem vai apvienotu tekstu (konkatenācija) ar string tipa datiem. Piemēram, 2 + 3 dos rezultātu 5, un "Hello, " + "World!" dos rezultātu "Hello, World!"
- - mīnus zīme tiek izmantota, lai veiktu atņemšanu ar skaitļiem. Piemēram, 5 - 2 dos rezultātu 3.
* - zvaigznīte tiek izmantota, lai veiktu reizināšanu ar skaitļiem. Piemēram, 4 * 3 dos rezultātu 12.
/ - slīpsvītra tiek izmantota, lai veiktu dalīšanu ar skaitļiem. Piemēram, 10 / 2 dos rezultātu 5.0 (rezultāts vienmēr būs float tipa, pat ja dalāmie ir veseli skaitļi).
// - dubultā slīpsvītra tiek izmantota, lai veiktu veselo dalīšanu, kas atgriež tikai veselo daļu no rezultāta. Piemēram, 10 // 3 dos rezultātu 3, jo vesela daļa no 10 dalīta ar 3 ir 3.
% - procentu zīme tiek izmantota, lai veiktu atlikuma operāciju, kas atgriež atlikumu pēc dalīšanas. Piemēram, 10 % 3 dos rezultātu 1, jo 10 dalīts ar 3 dod 3 ar atlikumu 1.
** - dubultā zvaigznīte tiek izmantota, lai veiktu pakāpju operāciju, kas atgriež rezultātu, kad pirmais skaitlis tiek pacelts otrā skaitļa pakāpē. Piemēram, 2 ** 3 dos rezultātu 8, jo 2 pacelts 3. pakāpē ir 8.

salīdzināšanas operatori - tie ir simboli, kas tiek izmantoti, lai salīdzinātu divas vērtības un atgrieztu True vai False atkarībā no salīdzinājuma rezultāta. Šie operatori ietver:
== - divi vienādas vērtības operatori tiek izmantoti, lai pārbaudītu, vai divas vērtības ir vienādas. Piemēram, 5 == 5 dos rezultātu True, bet 5 == 3 dos rezultātu False.
!= - nav vienādas vērtības operatori tiek izmantoti, lai pārbaudītu, vai divas vērtības nav vienādas. Piemēram, 5 != 3 dos rezultātu True, bet 5 != 5 dos rezultātu False.
> - lielāks nekā operatori tiek izmantoti, lai pārbaudītu, vai pirmā vērtība ir lielāka par otro. Piemēram, 5 > 3 dos rezultātu True, bet 3 > 5 dos rezultātu False.
< - mazāks nekā operatori tiek izmantoti, lai pārbaudītu, vai pirmā vērtība ir mazāka par otro. Piemēram, 3 < 5 dos rezultātu True, bet 5 < 3 dos rezultātu False.
>= - lielāks vai vienāds operatori tiek izmantoti, lai pārbaudītu, vai pirmā vērtība ir lielāka vai vienāda ar otro. Piemēram, 5 >= 5 dos rezultātu True, un 5 >= 3 dos rezultātu True, bet 3 >= 5 dos rezultātu False.
<= - mazāks vai vienāds operatori tiek izmantoti, lai pārbaudītu, vai pirmā vērtība ir mazāka vai vienāda ar otro. Piemēram, 3 <= 5 dos rezultātu True, un 5 <= 5 dos rezultātu True, bet 5 <= 3 dos rezultātu False.

loģiskie operatori - tie ir simboli, kas tiek izmantoti, lai veiktu loģiskās operācijas ar boolean vērtībām. Šie operatori ietver:
and - šis operators atgriež True tikai tad, ja abas puses ir True. Piemēram, True and True dos rezultātu True, bet True and False dos rezultātu False.
or - šis operators atgriež True, ja vismaz viena puse ir True. Piemēram, True or False dos rezultātu True, bet False or False dos rezultātu False.
not - šis operators maina boolean vērtību uz pretējo. Piemēram, not True dos rezultātu False, bet not False dos rezultātu True. 

fstrings - f-string ir formāta string, kas ļauj ērti iekļaut mainīgo vērtības tekstā. F-string tiek izveidots, sākot ar burtu 'f' vai 'F' un izmantojot iekavas {} lai norādītu, kur mainīgais jāievieto. Piemēram:
(f""Hello, {name}!"") - ja mainīgais name satur vērtību "Alice", tad šis f-string izvadīs "Hello, Alice!" uz ekrāna. F-string ļauj arī veikt izteiksmes iekavās, piemēram:
(f""The sum of 2 and 3 is {2 + 3}!"") - šis f-string izvadīs "The sum of 2 and 3 is 5!" uz ekrāna, jo izteiksme {2 + 3} tiek novērtēta un rezultāts tiek iekļauts tekstā. F-string ir ļoti noderīgs, lai veidotu dinamiskus tekstus, kas ietver mainīgo vērtības vai izteiksmes rezultātus.
    
{} - iekavas tiek izmantotas dažādos kontekstos Pythonā. Piemēram, tās tiek izmantotas f-string, lai norādītu, kur mainīgie vai izteiksmes jāievieto tekstā. Tās arī tiek izmantotas vārdnīcās (dict) kā atslēgu-vērtību pāru delimitatori, piemēram, {"name": "Alice", "age": 30}. Turklāt iekavas tiek izmantotas arī set tipa datiem, piemēram, {1, 2, 3}.
{"name": "Alice", "age": 30}. Šajā piemēra vārdnīcā iekavas {} norāda, ka tas ir vārdnīcas datu tips, un atslēgu-vērtību pāri tiek norādīti ar iekavām. Iekavas arī tiek izmantotas set tipa datiem, piemēram, {1, 2, 3}, kur tās norāda, ka tas ir set datu tips un satur unikālus elementus 1, 2 un 3.

set - šis operators tiek izmantots, lai veiktu darbības ar set tipa datiem, piemēram, apvienošanu, krustojumu un atšķirību. Piemēram, set1 = {1, 2, 3} un set2 = {3, 4, 5} apvienojums set1 | set2 dos rezultātu {1, 2, 3, 4, 5}, krustojums set1 & set2 dos rezultātu {3}, un atšķirība set1 - set2 dos rezultātu {1, 2}.
dict - šis operators tiek izmantots, lai veiktu darbības ar dict tipa datiem, piemēram, piekļuvi vērtībām pēc atslēgām, pievienošanu un dzēšanu. Piemēram, my_dict = {"name": "Alice", "age": 30} piekļuve vērtībai pēc atslēgas my_dict["name"] dos rezultātu "Alice", pievienošana my_dict["city"] = "New York" pievienos jaunu atslēgu-vērtību pāri {"city": "New York"} vārdnīcai, un dzēšana del my_dict["age"] noņems atslēgu "age" un tās vērtību no vārdnīcas.



formāta specifikatori - tie ir simboli, kas tiek izmantoti, lai formatētu skaitļus un tekstu f-string vai format() metodes kontekstā. Šie specifikatori ļauj kontrolēt, kā dati tiek attēloti, piemēram, ar noteiktu skaitu decimāldaļu vai noteiktu platumu. Piemēri formāta specifikatoriem ietver:
:.2f - šis specifikators tiek izmantots, lai formatētu skaitli ar divām decimāldaļām. Piemēram, f"{3.14159:.2f}" dos rezultātu "3.14".
:10s - šis specifikators tiek izmantots, lai formatētu tekstu ar noteiktu platumu. Piemēram, f"{'Hello':10s}" dos rezultātu "Hello     ", kur teksts "Hello" tiek formatēts ar platumu 10 rakstzīmju, un atlikušie rakstzīmes tiek aizpildītas ar atstarpēm. 
4d- šis specifikators tiek izmantots, lai formatētu veselu skaitli ar noteiktu platumu. Piemēram, f"{42:4d}" dos rezultātu "  42", kur skaitlis 42 tiek formatēts ar platumu 4 rakstzīmju, un atlikušie rakstzīmes tiek aizpildītas ar atstarpēm. 

piešķiršanas operatori - tie ir simboli, kas tiek izmantoti, lai veiktu darbības ar kolekciju tipiem, piemēram, list, tuple, set un dict. Šie operatori ietver:
in - šis operators tiek izmantots, lai pārbaudītu, vai konkrēta vērtība ir kolekcijā. Piemēram, 3 in [1, 2, 3] dos rezultātu True, bet 4 in [1, 2, 3] dos rezultātu False.
not in - šis operators tiek izmantots, lai pārbaudītu, vai konkrēta vērtība nav kolekcijā. Piemēram, 4 not in [1, 2, 3] dos rezultātu True, bet 3 not in [1, 2, 3] dos rezultātu False.     
= - vienādojuma zīme tiek izmantota, lai piešķirtu vērtību mainīgajam. Piemēram, x = 5 piešķir vērtību 5 mainīgajam x. Šis operators tiek izmantots arī, lai veiktu darbības ar kolekciju tipiem, piemēram, list, tuple, set un dict. Piemēram, my_list = [1, 2, 3] piešķir sarakstu [1, 2, 3] mainīgajam my_list.  


elif - šis atslēgvārds tiek izmantots, lai pārbaudītu papildu nosacījumus pēc if un pirms else. Tas ļauj izveidot vairākas nosacījumu pārbaudes vienā if-elif-else blokā. Piemēram:
x = 10  

Alt kodi - tie ir speciāli simboli, kurus var ievadīt, izmantojot tastatūras kombinācijas ar Alt taustiņu. Šie kodi ļauj ievadīt dažādus simbolus un rakstzīmes, kas nav tieši pieejami uz tastatūras. Piemēri Alt kodiem ietver:
Alt + 1 → ☺
Alt + 26 → →
Alt + 10003 → ✓
Alt + 10007 → ✗

citi KeyboardInterrupt - šis ir izņēmums, kas tiek izsaukts, kad lietotājs nospiež Ctrl + C vai citu tastatūras kombināciju, lai pārtrauktu programmas izpildi. Šis izņēmums var tikt apstrādāts ar try-except bloku, lai veiktu kādas darbības, piemēram, izvadīt ziņojumu vai veikt tīrīšanu, pirms programma tiek pārtraukta. Piemēram:
try:
    while True:
        pass  # Programma turpinās darboties, līdz lietotājs nospiež Ctrl + C
except KeyboardInterrupt:
    print("Programma tika pārtraukta ar tastatūras kombināciju.")   
 try-except bloks tiek izmantots, lai apstrādātu izņēmumus, kas var rasties programmas izpildes laikā. Šajā gadījumā mēs izmantojam try-except bloku, lai apstrādātu KeyboardInterrupt izņēmumu, kas tiek izsaukts, kad lietotājs nospiež Ctrl + C vai citu tastatūras kombināciju, lai pārtrauktu programmas izpildi. Ja šis izņēmums tiek izsaukts, programma izvadīs ziņojumu "Programma tika pārtraukta ar tastatūras kombināciju." un pēc tam tiks pārtraukta. 
 todo - šis ir komentārs, kas tiek izmantots, lai atzīmētu uzdevumus vai lietas, kas vēl jāizdara programmā. To var izmantot, lai atgādinātu sev vai citiem izstrādātājiem par nepieciešamajiem uzlabojumiem, kļūdu labojumiem vai papildu funkcionalitāti, kas jāievieš nākotnē. Piemēram:
   
  choise = input("Izvēlies numuru: ")  # TODO: Pievienot validāciju, lai pārbaudītu, vai ievadītais numurs ir derīgs un atbilst piedāvātajām opcijām. Šis komentārs atgādina izstrādātājam, ka ir nepieciešams pievienot papildu funkcionalitāti, lai pārbaudītu lietotāja ievadi un nodrošinātu, ka tā atbilst gaidītajam formātam vai vērtībām. Tas palīdzēs uzlabot programmas stabilitāti un lietotāja pieredzi, jo nepareiza ievade tiks apstrādāta un lietotājs saņems atbilstošu ziņojumu vai norādījumus, kā ievadīt pareizu numuru. 

if - šis atslēgvārds tiek izmantots, lai pārbaudītu nosacījumu un izpildītu noteiktu koda bloku, ja nosacījums ir True. Piemēram:
age = int(input("Ievadi vecumu: ")) 

elif - šis atslēgvārds tiek izmantots, lai pārbaudītu papildu nosacījumus pēc if un pirms else. Tas ļauj izveidot vairākas nosacījumu pārbaudes vienā if-elif-else blokā. Piemēram:
if age < 18:    
    print("Tu esi nepilngadīgs.")
elif age < 65:
    print("Tu esi pieaugušais.")
else:
    print("Tu esi senioru vecumā.")

else - šis atslēgvārds tiek izmantots, lai izpildītu noteiktu koda bloku, ja visi iepriekšējie nosacījumi if un elif ir False. Piemēram:
if age < 18:    
    print("Tu esi nepilngadīgs.")
elif age < 65:
    print("Tu esi pieaugušais.")
else:
    print("Tu esi senioru vecumā.") 

    lower() - šī metode tiek izmantota, lai pārvērstu visus burtus string tipa mainīgajā uz mazajiem burtiem. Piemēram: 

    and 
    ternary operator - šis operators ļauj īsi izteikt nosacījumu un atgriezt vērtību atkarībā no nosacījuma rezultāta. Tas tiek izmantots formā: value_if_true if condition else value_if_false. Piemēram:
x = 10
result = "Liels" if x > 5 else "Mazs"  # Ja x ir lielāks par 5, result būs "Liels", pretējā gadījumā result būs "Mazs". Šis operators ļauj rakstīt kompaktāku kodu, kad nepieciešams izvēlēties starp divām vērtībām atkarībā no nosacījuma rezultāta. Tas ir īpaši noderīgi, lai izvairītos no garām if-else struktūrām un padarītu kodu vieglāk lasāmu.