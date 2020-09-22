# Lista
lista_convidados = ["Ana", "João", "Paiva", "Agatha", "Maria"]

print(lista_convidados)

# Adicionando elemento na lista
lista_convidados.append("Maurício")

print(lista_convidados)

# Remover Elemento da Lista
lista_convidados.remove("Ana")

print(lista_convidados)

# Pegar primeiro elemento da lista

print(lista_convidados[0])

# Pegar último elemento sem saber a posição
print(lista_convidados[-1])

# Lista variada

lista_variada = ["Daniel", 27, 1.70]

print(lista_variada)

# Tupla
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
print(tupla1)

tupla3 = tupla1 + tupla2
print(tupla3)

# Dicionário - Mapeamento de Chave para valor

dados_pessoais = {"nome": "Batman", "cidade": "Gothan"}
print(dados_pessoais)

dados_pessoais["Veículo"] = "Batmovel"
print(dados_pessoais)

del dados_pessoais["cidade"]
print(dados_pessoais)