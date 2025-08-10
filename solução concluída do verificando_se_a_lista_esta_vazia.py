def verificar_lista_vazia(lista):
    """
    FunÃ§Ã£o que recebe uma lista e retorna True se ela estiver vazia
    e False caso contrÃ¡rio.
    """
    return len(lista) == 0

# Teste da funÃ§Ã£o
if __name__ == "__main__":
    # Testes
    lista_vazia = []
    lista_com_elementos = [1, 2, 3]
    
    print(f"Lista vazia estÃ¡ vazia? {verificar_lista_vazia(lista_vazia)}")
    print(f"Lista com elementos estÃ¡ vazia? {verificar_lista_vazia(lista_com_elementos)}")
    
    # Teste adicional
    numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
    print(f"Lista de nÃºmeros está vazia? {verificar_lista_vazia(numeros)}")