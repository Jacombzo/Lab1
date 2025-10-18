print("Kalkulator pokazujący wyniki podstawowych działań między dwiema liczbami.")

#nie wiem dokładnie, czy dodać zabezpieczenie przed wprowadzeniem złej wartości, ale dla pewności dodaje
while True:
    try:
        x = float(input("Podaj 1 liczbę: ").replace(',', '.'))
        y = float(input("Podaj 2 liczbę: ").replace(',', '.'))
        break
    except ValueError:
        print("Podana liczba jest błędna (przykład 3.2 lub 2,5).")

print(f"1. {x} + {y} = {x + y}")
print(f"2.  {x} - {y} = {x - y}")
print(f"3.  {x} * {y} = {x * y}")
print(f"4.  {x} / {y} = {x / y}")
print(f"5.  {x} ** {y} = {x ** y}")