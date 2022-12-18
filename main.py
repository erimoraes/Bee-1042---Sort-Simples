#Bee 1042 - Sort Simples
'''
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, 
uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada:

A entrada contem três números inteiros.
Saída

Imprima a saída conforme foi especificado.'''

valores = list(map(int, input().split()))

v1 = valores[0]
v2 = valores[1]
v3 = valores[2]

valores.sort()

print(f'{valores[0]:.0f}\n{valores[1]:.0f}\n{valores[2]:.0f}\n\n{v1:.0f}\n{v2:.0f}\n{v3:.0f}')
