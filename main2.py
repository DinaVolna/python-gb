from array import array
import math

#1

print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))



#2

my_array = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(my_array):
  if my_array[i].replace('+', '').isdigit() == True:
    my_array.insert(i, '"')
    my_array.insert(i + 2, '"')
    if len(str(my_array[i+1])) < 2:
      my_array[i + 1] = '0' + my_array[i+1]
    i += 2
  if i >= len(my_array):
    break
  i += 1
print(my_array)

b = ''
for elem in my_array:
  b = b + ' ' + elem
print(b)




#4

workers = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
index = 0
work = ''
for element in workers:
  workers[index] = element.lower()
  index += 1
index = 0

for element in workers:
  list_from_elem = element.split(' ')
  list_from_elem.pop()
  for i in list_from_elem:
    if work == '':
      work = work + ' ' + i[0].upper() + i.replace(i[0],'', 1)
    else:
      work = work + ' ' + i
  name = element.split(' ')[len(element.split(' '))-1]
  workers[index] = work + ', ' + name[0].upper() + name.replace(name[0],'', 1)
  work = ''
  index += 1
for i in workers:
  print(i)




#5

prices = [57.8, 46.51, 97.41, 52.03, 45.32, 54.61, 20.08, 67.39, 24.00, 89.33, 2.3]
all_prices = ''

for i in prices:
  rub = math.floor(i)
  pen = round((i - rub)*100)
  if len(str(pen)) < 2:
    pen = '0' + str(pen)
  if len(str(rub)) < 2:
    rub = '0' + str(rub)
  if prices.index(i) != len(prices)-1:
    all_prices = all_prices + str(rub) + ' руб ' + str(pen) + ' коп' + ', '
  else:
    all_prices = all_prices + str(rub) + ' руб ' + str(pen) + ' коп' 
print(all_prices)

print('id: ' + str(id(prices)))
prices.sort()
print('По возрастанию: ')
print('id: '+ str(id(prices)))
for i in prices:
  rub = math.floor(i)
  pen = round((i - rub)*100)
  if len(str(pen)) < 2:
    pen = '0' + str(pen)
  if len(str(rub)) < 2:
    rub = '0' + str(rub)
  print(str(rub) + ' руб ' + str(pen) + ' коп')

print('По убыванию: ')
prices_2 = prices.copy()
prices_2 = sorted(prices_2, reverse = True)
for i in prices_2:
  rub = math.floor(i)
  pen = round((i - rub)*100)
  if len(str(pen)) < 2:
    pen = '0' + str(pen)
  if len(str(rub)) < 2:
    rub = '0' + str(rub)
  print(str(rub) + ' руб ' + str(pen) + ' коп')

print('Самые дорогие: ')
for i in prices_2:
  if prices_2.index(i) > 4:
    prices_2.remove(i)
  else:
    rub = math.floor(i)
    pen = round((i - rub)*100)
    if len(str(pen)) < 2:
      pen = '0' + str(pen)
    if len(str(rub)) < 2:
      rub = '0' + str(rub)
    print(str(rub) + ' руб ' + str(pen) + ' коп')
