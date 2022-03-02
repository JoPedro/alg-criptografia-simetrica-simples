from collections import deque

def criptografar(input):
    input = deque(input)

    alfabeto   = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    chave      = ['d', 'r', 'w', 'l', 'y', 'z', 'f', 'k', 'j', 'o', 'u', 'c', 'n', 'a', 't', 'q', 'i', 'b', 'm', 'x', 'p', 'g', 'v', 'h', 'e', 's']

    # Substituição
    for i in range(0, len(input)):
        k = 0
        for j in range(0, len(alfabeto)):
            if input[i] == alfabeto[j]:
                input[i] = chave[k]
                break
            k = k+1

    # Permutação em pares
    for i in range(0, len(input) - 1):
        input[i], input[i+1] = input[i+1], input[i]

    # Segunda permutação (inverter a ordem)
    j = len(input) - 1
    for i in range(0, len(input) // 2):
        input[i], input[j] = input[j], input[i]
        j = j - 1

    # Rotação
    input.rotate(1)

    # Segunda substituição
    for i in range(0, len(input)):
        k = 0
        for j in range(0, len(alfabeto)):
            if input[i] == alfabeto[j]:
                input[i] = chave[k]
                break
            k = k+1
            
    string = ''

    for letra in input:
        string = string + letra   

    return string

def descriptografar(input):
    input = deque(input)

    alfabeto   = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    chave      = ['d', 'r', 'w', 'l', 'y', 'z', 'f', 'k', 'j', 'o', 'u', 'c', 'n', 'a', 't', 'q', 'i', 'b', 'm', 'x', 'p', 'g', 'v', 'h', 'e', 's']

    # Substituição
    for i in range(0, len(input)):
        k = 0
        for j in range(0, len(chave)):
            if input[i] == chave[j]:
                input[i] = alfabeto[k]
                break
            k = k+1

    # Permutação em pares
    for i in range(0, len(input) - 1):
        input[i], input[i+1] = input[i+1], input[i]

    # Segunda permutação (restaurar a ordem inicial)
    j = len(input) - 1
    for i in range(0, len(input) // 2):
        input[i], input[j] = input[j], input[i]
        j = j - 1

    # Rotação
    input.rotate(1)

    # Segunda substituição
    for i in range(0, len(input)):
        k = 0
        for j in range(0, len(chave)):
            if input[i] == chave[j]:
                input[i] = alfabeto[k]
                break
            k = k+1
            
    string = ''

    for letra in input:
        string = string + letra   

    return string 

input = input()

input_cript = criptografar(input)
input_descript = descriptografar(input_cript)

print(input_cript)
print(input_descript)