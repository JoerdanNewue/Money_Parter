print("Кассир оптимально выдаст вам сдачу")
change = int(input(print("укажите величину остатка в копейках")))
if change < 0:
    print("такого быть не может")
while change < 0:
    change = int(input(print("укажите величину остатка в копейках")))
a = 50
av = 0
b = 10
bv = 0
c = 5
cv = 0
d = 1
dv = 0
lowchange = change
while lowchange >= a:
    av = av + 1
    lowchange = lowchange - 50
while lowchange >= b:
    bv = bv + 1
    lowchange = lowchange - 10
while lowchange >= c:
    cv = cv + 1
    lowchange = lowchange - 5
while lowchange >= d:
    dv = dv + 1
    lowchange = lowchange - 1
print("Сдача " + str(av) + " ПятидесятиКопеечных +" + str(bv) + " ДесятиКопеечных +")
print(str(cv) + " ПятиКопеечных +" + str(dv) + " ОдноКопеечных ")
