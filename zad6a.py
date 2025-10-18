import random

cena_paliwa = float(input("Podaj cenę paliwa w zł: "))
droga = int(random.randint(1, 1000))
spalanie = float(input("Podaj średnie spalanie w litach na 100 km: "))

print(f"Zużycie paliwa przy trasie {droga} km wyniesie ok. {round((spalanie / 100) * droga , 2)} l.")
print(f"Koszt przy trasie {droga} km wyniesie ok. {round(((spalanie / 100) * droga) * cena_paliwa , 2)} zł.")