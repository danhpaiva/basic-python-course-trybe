# Built-Ins Variables

# List
party_listt = ["Ana", "João", "Paiva", "Agatha", "Maria"]

print(party_listt)

# Adding element to the list
party_listt.append("Maurício")

print(party_listt)

# Remove Element from List
party_listt.remove("Ana")

print(party_listt)

# Get first list item

print(party_listt[0])

# Take last element without knowing the position
print(party_listt[-1])

# List with different types of data

varied_listt = ["Daniel", 27, 1.70]

print()

# Tupla
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
print(tupla1)

tupla3 = tupla1 + tupla2
print(tupla3)

# Dictionary - Key to Value Mapping

personal_data = {"name": "Batman", "city": "Gothan"}
print(personal_data)

personal_data["Car"] = "Batmovel"
print(personal_data)

del personal_data["city"]
print(personal_data)