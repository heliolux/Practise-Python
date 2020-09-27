# Przelicznik cm na metry i cale
cm = int(input("Podaj długość w cm: "))
cm2m = cm/100
cm2c = cm/0.394
print("Długość {} cm to {} metrów i {:.3f} cali".format(cm, cm2m,cm2c))

# Przelicznik kilogramów na gramy i funty
kg = int(input("Podaj ilość kg: "))
kg2grams = kg * 1000
kg2funt = kg * 2.4419
print("Waga {}kg to {}g lub {:.4f} funty".format(kg,kg2grams,kg2funt))