# ESERCIZIO: Studenti corsi universitari con insiemi (set)

# Studenti di ciascun corso
corso_A = {"Mario", "Luca", "Anna", "Giulia", "Paolo"}
corso_B = {"Luca", "Giulia", "Sara", "Marco", "Paolo"}

print("Corso A:", corso_A)
print("Corso B:", corso_B)
print()

# Chi frequenta entrambi i corsi (intersezione)
entrambi = corso_A & corso_B
print("Entrambi i corsi:", entrambi)

# Solo corso A
solo_A = corso_A - corso_B
print("Solo corso A:", solo_A)

# Solo corso B
solo_B = corso_B - corso_A
print("Solo corso B:", solo_B)

# Almeno un corso (unione)
almeno_uno = corso_A | corso_B
print("Almeno un corso:", almeno_uno)

# Studenti unici totali
totali = len(corso_A | corso_B)
print("Studenti unici totali:", totali)
