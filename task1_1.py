 # Завдання1.1
# Користувачем вводиться тризначний код спеціальності. Закодом на монітор виводиться назва спеціальності, за якою відбувається підготовкафахівцівна факультеті інформаційних і прикладних технологій Донецького національного університету імені Василя Стуса:
# Код:Назва спеціальності
# 029Інформаційна, бібліотечна та архівна справа
# 052Політологія
# 061Журналістика
# 105Прикладна фізика та наноматеріали
# 111Математика
# 113 Прикладна математика
# 122Комп’ютерні науки
# 125Кібербезпека
# 281Публічне управління та адміністрування

x = input("Введіть номер вашої спеціальності: ");
if (x =="029"):
  print("факультет:Інформаційна, бібліотечна та архівна справа");
elif (x == "052"):
  print("факультет:Політологія");
elif (x =="061"):
  print("факультет:Журналістика");
elif (x == "102"):
  print("факультет:Прикладна фізика та наноматеріали");
elif (x == "111"):
  print("факультет:Математика");
elif (x == "113"):
  print("факультет:Прикладна математика");
elif (x == "122"):
  print("факультет:Комп’ютерні науки");
elif (x == "125"):
  print("факультет:Кібербезпека");
elif (x == "281"):
  print("факультет:Публічне управління та адміністрування");
else:
  print("Такой спельности не существует, попробуйде еще раз");