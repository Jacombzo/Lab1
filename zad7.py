print("Program rozwiązujący równanie liniowe ax + b = 0")

while True:
    try:
        a = float(input("Podaj wartość a: ").replace(',' , '.'))
        b = float(input("Podaj wartość b: ").replace(',' , '.'))
        break
    except ValueError:
        print("Podana wartość nie jest prawidłowa (przykład: 2,8 lub 5.3)")

if a != 0:
    x = -b / a
    print(f"Rozwiązaniem równania jest x = {round(x , 2)}")
elif b == 0:
    print("Równanie ma nieskończenie wiele rozwiązań")
else:
    print(f"Sprzeczność (brak rozwiązań)")
print("(Wynik zaokrąglany jest do 2 miejsc po przecinku)")