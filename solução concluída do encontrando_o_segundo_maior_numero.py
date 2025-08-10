def encontrar_segundo_maior_numero(lista):
    """
    Função que retorna o segundo maior número de uma lista.
    Considera que a lista pode ter números duplicados.
    """
    if len(lista) < 2:
        return None
    
    # Remove duplicatas e ordena em ordem decrescente
    numeros_unicos = list(set(lista))
    numeros_unicos.sort(reverse=True)
    
    if len(numeros_unicos) < 2:
        return None
    
    return numeros_unicos[1]

# Teste da função
if __name__ == "__main__":
    numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
    resultado = encontrar_segundo_maior_numero(numeros)
    print(f"O segundo maior número da lista é: {resultado}")