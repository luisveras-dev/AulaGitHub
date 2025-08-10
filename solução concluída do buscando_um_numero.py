def buscar_numero(numero, lista):
    """
    Função que recebe um número e uma lista. A função deve buscar o número na lista
    e retornar True se o encontrar e False caso contrário.
    """
    for elemento in lista:
        if elemento == numero:
            return True
    return False

# Teste da função
if __name__ == "__main__":
    numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
    
    # Testes
    print(f"Buscar 42: {buscar_numero(42, numeros)}")
    print(f"Buscar 100: {buscar_numero(100, numeros)}")
    print(f"Buscar 1000000000: {buscar_numero(1000000000, numeros)}")