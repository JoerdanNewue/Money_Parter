print("Кассир оптимально выдаст вам сдачу")
change = int(input(print("укажите величину остатка в копейках")))
print(str(change) + " копеек")
a = 50
av = 0
lowchange = change
while lowchange >= a:
    av = av + 1
    lowchange = lowchange - 50
print(str(av) + "раз по полтине")