# # Busca Linear
#
# def busca_linear(vetor, valor):
#     for i in range(len(vetor)):
#         if vetor[i] == valor:
#             return i
#     return -1
#
# numeros = [10, 20, 30, 40, 50]
# # Busca o indice do número que esta buscando
# print(busca_linear(numeros, 30))  # Saída: 2


# # Busca Binária
# def busca_binaria(vetor, valor):
#     inicio = 0
#     fim = len(vetor) - 1
#
#     while inicio <= fim:
#         meio = (inicio + fim) // 2
#         if vetor[meio] == valor:
#             return meio
#         elif vetor[meio] < valor:
#             inicio = meio + 1
#         else:
#             fim = meio - 1
#     return -1
#
# ordenado = [10, 20, 30, 40, 50]
# print(busca_binaria(ordenado, 40))  # Saída: 3


# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# Acesso a elementos
# print(matriz[0][1])
#
# # Percorrer matriz com for:
# for linha in matriz:
#     for elemento in linha:
#         print(elemento)


#
# # Soma de duas matrizes:
# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]
# soma = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]
# print(soma)


# Operações Básicas com Strings
# Concatenação
#
# nome = "Maria"
# sobrenome = "Silva"
# nome_completo = nome + " " + sobrenome
#
# # Fatiamento
# frase = "Olá, mundo!"
# print(frase[0:3])  # Saída: Olá
#


# Iteração:
# nome = "Sandeison"
# for letra in nome:
#     print(letra)



# Exemplo: Contar vogais em uma matriz de palavras
matriz = [
    ["maçã", "banana"],
    ["uva", "kiwi"]
]

vogais = "aeiou"
contador = 0

for linha in matriz:
    for palavra in linha:
        for letra in palavra:
            if letra.lower() in vogais:
                contador += 1

print("Total de vogais:", contador)
