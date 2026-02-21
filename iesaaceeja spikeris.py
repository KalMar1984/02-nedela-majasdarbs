# =====================================================
# 🧠 PYTHON IESĀCĒJA ŠPIKERIS — VS CODE EDITION
# =====================================================

# ================================
# 📦 MAINĪGIE
# ================================
# x = 5              → vesels skaitlis (int)
# y = 3.14           → decimālskaitlis (float)
# name = "Anna"      → teksts (string)
# ok = True          → loģiska vērtība (bool)

# type(x)            → parāda tipu


# ================================
# 🖨️ IZVADE
# ================================
# print("Sveiki")
# print(x, y, name)

# f-string (ieteicamais veids)
# print(f"Rezultāts = {x}")


# ================================
# ⌨️ IEVADE
# ================================
# input() vienmēr atgriež STRING

# text = input("Ievadi tekstu: ")
# num  = int(input("Ievadi veselu skaitli: "))
# val  = float(input("Ievadi skaitli: "))


# ================================
# 🛡️ KĻŪDU APSTRĀDE
# ================================v
# try:
#     x = float(input("Skaitlis: "))
# except ValueError:
#     print("Nav skaitlis!")
#     exit()


# ================================
# 🔢 ARITMĒTIKA
# ================================
# +  saskaitīšana
# -  atņemšana
# *  reizināšana
# /  dalīšana
# // veselā dalīšana
# %  atlikums
# ** pakāpe

# piem:
# 7 // 2 → 3
# 7 % 2  → 1


# ================================
# 🔍 SALĪDZINĀŠANA
# ================================
# ==  vienāds
# !=  nav vienāds
# >   lielāks
# <   mazāks
# >=  lielāks vai vienāds
# <=  mazāks vai vienāds


# ================================
# 🔀 NOSACĪJUMI
# ================================
# if x > 0:
#     print("pozitīvs")
# elif x == 0:
#     print("nulle")
# else:
#     print("negatīvs")


# ================================
# 🔁 CIKLI
# ================================

# while — kamēr nosacījums patiess
# while x < 5:
#     print(x)
#     x += 1

# for — iterācija
# for i in range(5):
#     print(i)

# range(start, stop, step)


# ================================
# 📋 SARAKSTI (LIST)
# ================================
# nums = [1, 2, 3]

# nums.append(4)
# nums.remove(2)
# len(nums)

# for n in nums:
#     print(n)


# ================================
# 🔤 STRING OPERĀCIJAS
# ================================
# s = "Python"

# s.lower()
# s.upper()
# s.strip()
# s.replace("Py", "My")
# len(s)

# s[0]      → pirmais simbols
# s[-1]     → pēdējais


# ================================
# 🧾 F-STRING FORMATĒŠANA
# ================================
# x = 3.14159

# print(f"{x:.2f}")     → 3.14
# print(f"{x:.3f}")     → 3.142
# print(f"{x:10.2f}")   → platums + precizitāte


# ================================
# 🧱 KONSTANTES
# ================================
# LIELIE_BURTI = konstante
# KM_TO_MI = 0.621371


# ================================
# 🧰 FUNKCIJAS
# ================================
# def sveiciens(vards):
#     return f"Sveiks {vards}"

# print(sveiciens("Anna"))


# ================================
# 📦 IMPORTI
# ================================
# import math
# math.sqrt(9)

# from math import sqrt


# ================================
# 📂 FAILU LASĪŠANA
# ================================
# with open("fails.txt") as f:
#     data = f.read()

# with open("fails.txt","w") as f:
#     f.write("teksts")


# ================================
# 🧪 ĀTRA TESTĒŠANA VS CODE
# ================================
# Terminālī:
# python fails.py
# python3 fails.py

# Ctrl + ` → atver termināli


# ================================
# 📝 TODO KOMENTĀRI
# ================================
# TODO: uzrakstīt funkciju
# TODO: pārbaudīt ievadi
# TODO: pievienot ciklu

# VS Code izceļ TODO sarakstā


# ================================
# 🧭 TIPISKA PROGRAMMAS STRUKTŪRA
# ================================
# konstantes
# ↓
# print izvēlne
# ↓
# input
# ↓
# try/except
# ↓
# if/elif
# ↓
# aprēķins
# ↓
# f-string izdruka


# ================================
# 🛑 PROGRAMMAS BEIGAS
# ================================
# exit()


# =====================================================
# BEIGAS — ŠIS IR ŠPIKERIS, NEVIS IZPILDĀMS KODS
# =====================================================
