def inverter_lista(lista):
    """
    Função que recebe uma lista e retorna uma nova lista com os elementos na ordem inversa.
    """
    lista_invertida = []
    
    # Percorre a lista de trás para frente
    for i in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])
    
    return lista_invertida

# Teste da função
if __name__ == "__main__":
    numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
    resultado = inverter_lista(numeros)
    
    print(f"Lista original: {numeros}")
    print(f"Lista invertida: {resultado}")
    
# Saída esperada:
# Lista original: [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
# Lista invertida: [9, 13, 2, 9, 444, 7, 101010, 13, 1000000000, 5, 999999, 42, 3, 88888, 1, 1234567, 56, 7654321, 2, 987654321]    