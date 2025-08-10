def encontrar_menor_numero(lista):
    """
    Função que recebe uma lista de números e retorna o menor número encontrado nela.
    """
    if not lista:
        return None
    
    menor = lista[0]
    for numero in lista:
        if numero < menor:
            menor = numero
    
    return menor

# Teste da função
if __name__ == "__main__":
    numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
    resultado = encontrar_menor_numero(numeros)
    print(f"O menor número da lista é: {resultado}")