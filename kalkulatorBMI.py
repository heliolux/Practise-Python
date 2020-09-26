# Obliczanie wskaźnika BMI
print("Wskaźnik masy ciała (ang. body mass index, BMI")
print('----------------------------------------------')
print()
print("W celu poznania wskaźnika BMI podaj dane")
waga = float(input("Ile ważysz? (w kg): "))
wzrost = float(input("Jaki masz wzrost? (w cm): "))/100
BMI = waga / (wzrost ** 2)
print("Wskaźnik BMI wynosi:", round(BMI,2))
if BMI <= 16.99:
  print("Wychudzenie")
if 17 <= BMI <= 18.49:
  print("Niedowaga")
if 18.5 <= BMI <= 24.99:
  print("Wartość prawidłowa")
if 25 <= BMI <= 29.99:
  print("Nadwaga")
if 30 <= BMI <= 34.99:
  print("I stopień otyłości")
if 35 <= BMI <= 39.99:
  print("II stopień otyłości")
if BMI >=40:
  print("Skrajna otyłość")