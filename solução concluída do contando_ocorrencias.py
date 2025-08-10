def contar_ocorrencias(lista, valor):
    """
    Função que recebe uma lista e um valor. A função deve contar quantas vezes
    esse valor aparece na lista e retornar o total.
    """
    contador = 0
    for elemento in lista:
        if elemento == valor:
            contador += 1
    
    return contador

# Teste da função
if __name__ == "__main__":
    numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
    
    # Testes
    print(f"Ocorrências do número 2: {contar_ocorrencias(numeros, 2)}")
    print(f"Ocorrências do número 13: {contar_ocorrencias(numeros, 13)}")
    print(f"Ocorrências do número 9: {contar_ocorrencias(numeros, 9)}")
    print(f"Ocorrências do número 100: {contar_ocorrencias(numeros, 100)}")