def percorrer_lista(lista):
    """
    Função que recebe uma lista como argumento e percorre todos os seus elementos,
    imprimindo cada um na tela.
    """
    for elemento in lista:
        print(elemento)

# Teste da função
if __name__ == "__main__":
    numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
    print("Percorrendo a lista:")
    percorrer_lista(numeros)