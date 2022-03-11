from array import array
import random

#1

en_nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
ru_nums = ['Ноль', 'Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь', 'Восемь', 'Девять', 'Десять']

def num_translate(user_num):
  num_index = en_nums.index(user_num.lower())
  if user_num == user_num[0].upper() + user_num.replace(user_num[0], '', 1):
    print(ru_nums[num_index][0].upper() + ru_nums[num_index].replace(ru_nums[num_index][0], '', 1))
  else:
    print(ru_nums[num_index].lower())
    
  print(num_index)
  
num_translate(input('Введите число, которое хотите перевести: '))


#2

name = ''
d = {}
keys = {}

def thesaurus(names):
  names = names.split(',')
  #print(names)
  for name in names:
    i = name[0].upper()
    #d['i'] = d['i'], 'name'
    d.setdefault(i, []).append(name)
  list_d = list(d.keys())
  list_d.sort()
  for i in list_d:
    print(i, ':', d[i])

thesaurus(input('Введите имена, которое хотите отсортировать, через запятую без пробелов: '))




#4

# def thesaurus(names):
#   names = names.split(',')
#   print(names)
#   for name in names:
#     i = name[0].upper()
#     surname = (name.split(' ')[1])[0].upper()
#     print(surname)
#     #d['i'] = d['i'], 'name'
#     d.setdefault(i, []).append(name)
#     keys = {surname: d[0]}
#     #d.setdefault(i, []).append(name)
#     #keys.setdefault(i, []).append(d)
#     print(keys)



# thesaurus(input('Введите имена, которое хотите отсортировать, через запятую без пробелов: '))




#5

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(n, repeat):
  n = int(n)
  i = 0
  if repeat.lower() == 'да':
    while i != n:
      joke = nouns[random.randint(0, 4)] + ' ' + adverbs[random.randint(0, 4)] + ' ' + adjectives[random.randint(0, 4)]
      print(joke)
      i += 1
  elif repeat.lower() == 'нет':
    num = 4
    while i != n:
      ran_nouns = nouns[random.randint(0, num)]
      ran_adverbs = adverbs[random.randint(0, num)]
      ran_adjectives = adjectives[random.randint(0, num)]
      joke = ran_nouns + ' ' + ran_adverbs + ' ' + ran_adjectives
      nouns.remove(ran_nouns)
      adverbs.remove(ran_adverbs)
      adjectives.remove(ran_adjectives)
      num -=1
      print(joke)
      i += 1
  else: 
    print('неверное значение')
  
get_jokes(input('Введите количество шуток, нужное вам: '),
          input('Разрешать повторы слов?(да/нет): '))
