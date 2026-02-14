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


# virkņu savienošana - Python neveic automātisku tipu konvertēšanu, tāpēc, ja mēģināsim savienot virkni ar skaitli, tas radīs kļūdu. Mēs varam izmantot funkciju int() vai float(), lai konvertētu virkni uz skaitli, ja tas ir iespējams.
print("5" + "3")  # This will concatenate the strings and output "53"
# print("5"+3)    # This will raise a TypeError because you cannot concatenate a string and an integer
print (int("5") + 3)  # This will convert the string "5" to an integer and then add it to 3, resulting in 


# Robežgadījumi - Python ir dažādi datu tipi, un katram no tiem ir savas īpašības un ierobežojumi. Piemēram, int tips var saturēt ļoti lielus skaitļus, bet float tips var saturēt tikai noteiktu precizitāti. Ja mēs mēģinām izmantot skaitli, kas pārsniedz int tipa robežas, tas var radīt kļūdu.

