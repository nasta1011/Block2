tick = int(input('Введите количество билетов, которые вы хотите приобрести '))
a = list(map(int, input('Укажите через пробел возраст посетителей: ').split()))
s = 0

for i in range(tick):
    if a[i] < 18:
        s = s + 0
    elif 18 <= a[i] <= 25:
        s = s + 990
    elif a[i] > 25:
        s = s + 1390

if len(a) > 3:
    s = int(s*0.9)
print('Стоимость вашего заказа составляет: ',s, ' рублей')