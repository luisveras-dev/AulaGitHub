def calcular_media(lista):
    """
    Função que recebe uma lista de números e retorna a média aritmética desses valores.
    """
    if not lista:
        return 0
    
    soma = 0
    for numero in lista:
        soma += numero
    
    media = soma / len(lista)
    return media

# Teste da função
if __name__ == "__main__":
    numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
    resultado = calcular_media(numeros)
    print(f"A média aritmética da lista é: {resultado:.2f}")
    print(f"Total de números: {len(numeros)}")
    print(f"Soma total: {sum(numeros)}")