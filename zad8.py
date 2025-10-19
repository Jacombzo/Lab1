print("Program rozwiązujący równanie kwadratowe ax^2 + bx + c = 0")

while True:
    try:
        a = float(input("Podaj wartość a: ").replace(',' , '.'))
        b = float(input("Podaj wartość b: ").replace(',' , '.'))
        c = float(input("Podaj wartość c: ").replace(',' , '.'))
        break
    except ValueError:
        print("Podana wartość nie jest prawidłowa (przykład: 2,8 lub 5.3)")

if a != 0:
    delta = (b ** 2) - 4 * a * c
    if delta < 0:
        print("Brak miejsc zerowych (delta < 0)")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Rozwiązaniem równania jest x = {round(x , 2)}")
    else:
        pierwiastek = delta ** 0.5
        x1 = (-b + pierwiastek) / (2 * a)
        x2 = (-b - pierwiastek) / (2 * a)
        print(f"Rozwiązaniami równania są wartości x = {round(x1 , 2)} lub x = {round(x2 , 2)}")
else:
    print("Podane wartości nie tworzą funkcji kwadratowej")

print("(Wynik zaokrąglany jest do 2 miejsc po przecinku)")